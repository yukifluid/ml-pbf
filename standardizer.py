import torch
import torch_geometric

class Standardizer:
    def __init__(self, V_dim: int, E_dim: int, y_dim: int, train_loader: torch_geometric.loader.DataLoader, device: torch.device) -> None:
        num_batchs = len(train_loader) 

        batch_V_mean = torch.empty((num_batchs, V_dim), dtype=torch.float32).to(device)
        batch_E_mean = torch.empty((num_batchs, E_dim), dtype=torch.float32).to(device) 
        batch_y_mean = torch.empty((num_batchs, y_dim), dtype=torch.float32).to(device) 

        batch_V_std = torch.empty((num_batchs, V_dim), dtype=torch.float32).to(device) 
        batch_E_std = torch.empty((num_batchs, E_dim), dtype=torch.float32).to(device) 
        batch_y_std = torch.empty((num_batchs, y_dim), dtype=torch.float32).to(device) 

        for i, batch in enumerate(train_loader):
            batch_V_mean[i] = torch.mean(batch.V, axis=0) 
            batch_E_mean[i] = torch.mean(batch.E, axis=0) 
            batch_y_mean[i] = torch.mean(batch.y[batch.num_boundary_particles:], axis=0) 

            batch_V_std[i] = torch.std(batch.V, axis=0) 
            batch_E_std[i] = torch.std(batch.E, axis=0) 
            batch_y_std[i] = torch.std(batch.y[batch.num_boundary_particles:], axis=0) 

        self.V_mean = torch.mean(batch_V_mean, axis=0)
        self.E_mean = torch.mean(batch_E_mean, axis=0)
        self.y_mean = torch.mean(batch_y_mean, axis=0)

        self.V_std = torch.mean(batch_V_std, axis=0)
        self.E_std = torch.mean(batch_E_std, axis=0)
        self.y_std = torch.mean(batch_y_std, axis=0)

    def standardize(self, V: torch.Tensor, E: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
        V_z = (V - self.V_mean) / self.V_std
        E_z = (E - self.E_mean) / self.E_std
        y_z = (y - self.y_mean) / self.y_std
        return V_z, E_z, y_z

    def standardize_V_E(self, V: torch.Tensor, E: torch.Tensor) -> torch.Tensor:
        V_z = (V - self.V_mean) / self.V_std
        E_z = (E - self.E_mean) / self.E_std
        return V_z, E_z

    # def inverse(self, V_z: torch.Tensor, E_z: torch.Tensor, y_z: torch.Tensor) -> torch.Tensor:
    #     V = V_z * self.V_std + self.V_mean
    #     E = E_z * self.E_std + self.E_mean
    #     y = y_z * self.y_std + self.y_mean
    #     return V, E, y

    def inverse_y(self, y_z: torch.Tensor) -> torch.Tensor:
        y = y_z * self.y_std + self.y_mean
        return y
        
        