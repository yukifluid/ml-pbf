import os
import pandas as pd
import torch
import torch_geometric
from torch_geometric.nn.pool import radius_graph
from calc import calc_density
from config import Config

class PBFSimple(torch_geometric.data.Dataset):
    def __init__(self, dataset_type: str) -> None:
        self._dataset_type = dataset_type
        self._name = __class__.__name__
        self._url = f"file:./datasets/{self._name}/{self._dataset_type}.zip"
        self._num_scenes = {"train": 20, "valid": 5, "test": 5}[self._dataset_type]
        self._num_timesteps = 150

        os.makedirs(f"./{self._name}/processed/{self._dataset_type}", exist_ok=True)

        super().__init__(self._name)

    @property
    def raw_file_names(self) -> list[str]:
        raw_files = [f"{self._dataset_type}/{i}" for i in range(self._num_scenes)]
        return raw_files

    @property
    def processed_file_names(self) -> list[str]:
        processed_files = [f"{self._dataset_type}/{i}.pth" for i in range(self._num_scenes * self._num_timesteps)]
        return processed_files

    def download(self) -> None:
        zip_file = torch_geometric.data.download_url(self._url, self.raw_dir)
        torch_geometric.data.extract_zip(zip_file, self.raw_dir)
        os.unlink(zip_file)

    def process(self) -> None:
        idx = 0

        for scene_dir in self.raw_paths:
            config = Config(f"{scene_dir}/config.json", torch.device("cpu"))
            reader = pd.read_csv(f"{scene_dir}/data.csv", chunksize=config.num_particles)

            for df in reader:
                vol     = torch.tensor(df["vol"].values, dtype=torch.float32)
                mid_pos = torch.tensor(df[["mid_pos.x", "mid_pos.y", "mid_pos.z"]].values, dtype=torch.float32)
                mid_vel = torch.tensor(df[["mid_vel.x", "mid_vel.y", "mid_vel.z"]].values, dtype=torch.float32)
                dp      = torch.tensor(df[["dp.x", "dp.y", "dp.z"]].values, dtype=torch.float32)

                # vertex features
                edge_index = radius_graph(mid_pos, config.h, loop=True)
                m = config.rho_0 * vol
                rho = calc_density(config.rho_0, config.h, vol, mid_pos, edge_index)
                vertex_features = torch.cat((m.view(-1, 1), rho.view(-1, 1), mid_vel), axis=1)

                # edge features 
                edge_index = radius_graph(mid_pos, config.h, loop=False)
                i = edge_index[1] 
                j = edge_index[0]

                r_ij = mid_pos[i] - mid_pos[j]
                r = torch.linalg.norm(r_ij, axis=1)
                edge_features = torch.cat((r_ij, r.view(-1, 1)), axis=1)

                data = torch_geometric.data.Data(V=vertex_features, E=edge_features, N=edge_index, y=dp, vol=vol, mid_pos=mid_pos, mid_vel=mid_vel, num_boundary_particles=config.num_boundary_particles, rho_0=config.rho_0, h=config.h, dt=config.dt)

                torch.save(data, os.path.join(self.processed_paths[idx]))
                idx += 1

    def len(self) -> int:
        length = len(self.processed_paths)
        return length

    def get(self, i: int) -> torch_geometric.data.Data:
        data = torch.load(self.processed_paths[i])
        return data