import torch
import torch_geometric
from graph import Graph

class Encoder(torch.nn.Module):
    def __init__(self, V_dim: int, E_dim: int, hidden_dim: int) -> None:
        super().__init__()

        self.V_mlp = torch.nn.Sequential(
            torch.nn.Linear(V_dim     , hidden_dim), torch.nn.LeakyReLU(),
            torch.nn.Linear(hidden_dim, hidden_dim), torch.nn.LeakyReLU(),
            torch.nn.Linear(hidden_dim, hidden_dim), torch.nn.LeakyReLU(),
            torch.nn.Linear(hidden_dim, hidden_dim), torch.nn.LayerNorm(hidden_dim)
        )

        self.E_mlp = torch.nn.Sequential(
            torch.nn.Linear(E_dim     , hidden_dim), torch.nn.LeakyReLU(),
            torch.nn.Linear(hidden_dim, hidden_dim), torch.nn.LeakyReLU(),
            torch.nn.Linear(hidden_dim, hidden_dim), torch.nn.LeakyReLU(),
            torch.nn.Linear(hidden_dim, hidden_dim), torch.nn.LayerNorm(hidden_dim)
        )

    def forward(self, graph: Graph) -> Graph:
        latent_V = self.V_mlp(graph.V)
        latent_E = self.E_mlp(graph.E)

        latent_graph = Graph(latent_V, latent_E, graph.N)

        return latent_graph

class Processor(torch_geometric.nn.MessagePassing):
    def __init__(self, hidden_dim: int) -> None:
        super().__init__(aggr="add")

        self.message_mlp = torch.nn.Sequential(
            torch.nn.Linear(3*hidden_dim, hidden_dim), torch.nn.LeakyReLU(),
            torch.nn.Linear(hidden_dim  , hidden_dim), torch.nn.LeakyReLU(),
            torch.nn.Linear(hidden_dim  , hidden_dim), torch.nn.LeakyReLU(),
            torch.nn.Linear(hidden_dim  , hidden_dim), torch.nn.LayerNorm(hidden_dim)
        )

        self.update_mlp = torch.nn.Sequential(
            torch.nn.Linear(2*hidden_dim, hidden_dim), torch.nn.LeakyReLU(),
            torch.nn.Linear(hidden_dim  , hidden_dim), torch.nn.LeakyReLU(),
            torch.nn.Linear(hidden_dim  , hidden_dim), torch.nn.LeakyReLU(),
            torch.nn.Linear(hidden_dim  , hidden_dim), torch.nn.LayerNorm(hidden_dim)
        )

        self.latent_E = None

    def forward(self, graph: Graph) -> Graph:
        latent_V = self.propagate(V=graph.V, E=graph.E, edge_index=graph.N)
        latent_graph = Graph(latent_V, self.latent_E, graph.N)
        return latent_graph

    def message(self, V_i: torch.Tensor, V_j: torch.Tensor, E: torch.Tensor) -> torch.Tensor:
        message = self.message_mlp(torch.cat((V_i, V_j, E), axis=1))
        self.latent_E = message
        return message

    def update(self, agg_messages: torch.Tensor, V: torch.Tensor) -> torch.Tensor:
        latent_verts = self.update_mlp(torch.cat((agg_messages, V), axis=1))
        return latent_verts

class Decoder(torch.nn.Module):
    def __init__(self, hidden_dim: int, out_dim: int) -> None:
        super().__init__()

        self.V_mlp = torch.nn.Sequential(
            torch.nn.Linear(hidden_dim, hidden_dim), torch.nn.LeakyReLU(),
            torch.nn.Linear(hidden_dim, hidden_dim), torch.nn.LeakyReLU(),
            torch.nn.Linear(hidden_dim, hidden_dim), torch.nn.LeakyReLU(),
            torch.nn.Linear(hidden_dim, out_dim)
        )

    def forward(self, graph: Graph) -> torch.Tensor:
        out = self.V_mlp(graph.V) 
        return out

class GNS(torch.nn.Module):
    def __init__(self, V_dim: int, E_dim: int, hidden_dim: int, out_dim: int) -> None:
        super().__init__()

        self.encoder = Encoder(V_dim, E_dim, hidden_dim)

        self.processor1 = Processor(hidden_dim)
        self.processor2 = Processor(hidden_dim)
        self.processor3 = Processor(hidden_dim)

        self.decoder = Decoder(hidden_dim, out_dim)

    def forward(self, graph: Graph) -> torch.Tensor:
        latent_graph = self.encoder(graph) 

        latent_graph = latent_graph + self.processor1(latent_graph)
        latent_graph = latent_graph + self.processor2(latent_graph)
        latent_graph = latent_graph + self.processor3(latent_graph)

        out = self.decoder(latent_graph)
        return out