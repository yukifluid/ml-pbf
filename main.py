import sys
import random
import numpy as np
import torch
import torch_geometric
from dataset import PBFSimple
from standardizer import Standardizer
from network import GNS
from loss import VectorMSE
from learner import Learner

if len(sys.argv) < 2:
    print("input model name", file=sys.stderr)
    exit(1)

device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

SEED = 42
random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)
torch.cuda.manual_seed(SEED)

train_dataset = PBFSimple(dataset_type="train")
valid_dataset = PBFSimple(dataset_type="valid")
test_dataset  = PBFSimple(dataset_type="test")

train_loader = torch_geometric.loader.DataLoader(train_dataset, batch_size=1, shuffle=True)
valid_loader = torch_geometric.loader.DataLoader(valid_dataset, batch_size=1, shuffle=False)
test_loader  = torch_geometric.loader.DataLoader(test_dataset, batch_size=1, shuffle=False)

V_dim = train_dataset[0].V.shape[1]
E_dim = train_dataset[0].E.shape[1]
hidden_dim = 64
y_dim = 3

standardizer = Standardizer(V_dim, E_dim, y_dim, train_loader)

model = GNS(V_dim, E_dim, hidden_dim, y_dim).to(device)

criterion = VectorMSE()

optimizer = torch.optim.Adam(model.parameters(), lr=0.0001)

learner = Learner(standardizer, model, criterion, optimizer, device)
train_info, valid_info = learner.learn(train_loader, valid_loader, num_epochs=100)

model_path = f"./model/{sys.argv[1]}.pth"
torch.save(model.state_dict(), model_path)