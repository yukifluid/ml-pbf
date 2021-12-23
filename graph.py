import torch

class Graph:
    def __init__(self, V: torch.Tensor, E: torch.Tensor, N: torch.Tensor) -> None:
        self.V = V
        self.E = E
        self.N = N

    def __iadd__(self, other: "Graph"):
        self.V += other.V
        self.E += other.E
        return self