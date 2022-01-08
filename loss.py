import torch
import torch_geometric
from torch_geometric.nn.pool import radius_graph
from standardizer import Standardizer
from calc import calc_density, calc_divergence

class VectorMSE(torch.nn.Module):
    # def __init__(self) -> None:
    #     super().__init__()
    def __init__(self, c) -> None:
        super().__init__()
        self.c = c

    # 流体粒子のみで損失を計算
    # def forward(self, pred: torch.Tensor, batch: torch_geometric.data.Data, standardizer: Standardizer) -> torch.Tensor:
    #     loss = torch.mean(torch.sum(torch.pow(batch.y[batch.num_boundary_particles:]-pred[batch.num_boundary_particles:], 2.0), axis=1))
    #     return loss

    def forward(self, pred: torch.Tensor, y, standardizer: Standardizer) -> torch.Tensor:
        loss = torch.mean(torch.pow(y-pred, 2.0)) + self.c * torch.mean(torch.abs(pred))
        return loss

    # def forward(self, pred: torch.Tensor, batch: torch_geometric.data.Data) -> torch.Tensor:
    #     loss = torch.mean(torch.sum(torch.pow(batch.y[batch.num_boundary_particles:] - pred[batch.num_boundary_particles:], 2.0), axis=1))
    #     return loss

class Composition(torch.nn.Module):
    def __init__(self, alpha: float, beta: float, gamma: float):
        super().__init__()

        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma

    def forward(self, pred: torch.Tensor, batch: torch_geometric.data.Data, standardizer: Standardizer) -> torch.Tensor:
        loss1 = torch.mean(torch.sum((batch.y-pred)**2, axis=1))

        batch.y = standardizer.inverse_y(batch.y)
        batch.mid_pos[batch.num_boundary_particles:] += batch.y[batch.num_boundary_particles:]
        edge_index = radius_graph(batch.mid_pos, batch.h, loop=True)
        rho = calc_density(batch.rho_0, batch.h, batch.vol, batch.mid_pos, edge_index)
        cmp = rho / batch.rho_0 - 1.0
        loss2 = torch.mean(torch.abs(cmp))

        batch.mid_vel[batch.num_boundary_particles:] += batch.y[batch.num_boundary_particles:] / batch.dt
        div = calc_divergence(batch.rho_0, batch.h, batch.vol, batch.mid_pos, batch.mid_vel, edge_index)
        loss3 = torch.mean(torch.abs(div))
        
        loss = self.alpha * loss1 + self.beta * loss2 + self.gamma * loss3
        return loss