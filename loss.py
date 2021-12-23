import torch

class VectorMSE(torch.nn.Module):
    def __init__(self) -> None:
        super().__init__()

    def forward(self, y: torch.Tensor, pred: torch.Tensor) -> torch.Tensor:
        loss = torch.mean(torch.sum((y-pred)**2, axis=1))
        return loss