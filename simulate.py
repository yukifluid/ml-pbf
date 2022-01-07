import sys
import torch
import torch_geometric
from dataset import PBFSimple
from standardizer import Standardizer
from network import GNS
from simulator import SupervisedSimulator

if len(sys.argv) < 5:
    print("input model, config, out, measure", file=sys.stderr)
    exit(1)

model_name = sys.argv[1]
config_file = sys.argv[2]
output_file = sys.argv[3]
measurement_file = sys.argv[4]

model_path = f"./model/{model_name}/params.pth"

device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
# train_dataset = PBFSimple(dataset_type="train")
# train_loader = torch_geometric.loader.DataLoader(train_dataset, batch_size=1, shuffle=True)

# V_dim = train_dataset[0].V.shape[1]
V_dim = 1
# E_dim = train_dataset[0].E.shape[1]
E_dim = 4
hidden_dim = 64
y_dim = 3

# standardizer = Standardizer(V_dim, E_dim, y_dim, train_loader, device)

model = GNS(V_dim, E_dim, hidden_dim, y_dim).to(device)

model.load_state_dict(torch.load(model_path))

# simulator = SupervisedSimulator(model, standardizer, device)
simulator = SupervisedSimulator(model, device)
simulator.reset(config_file)
simulator.run(output_file, measurement_file)