import sys
import random
import numpy as np
import matplotlib.pyplot as plt
import torch
import torch_geometric
from dataset import PBFSimple, Simple3D
from standardizer import Standardizer
from network import GNS
from loss import VectorMSE, Composition
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

# train_dataset = PBFSimple(dataset_type="train")
# valid_dataset = PBFSimple(dataset_type="valid")
# test_dataset  = PBFSimple(dataset_type="test")

train_dataset = Simple3D(dataset_type="train")
valid_dataset = Simple3D(dataset_type="valid")
test_dataset  = Simple3D(dataset_type="test")

train_loader = torch_geometric.loader.DataLoader(train_dataset, batch_size=1, shuffle=True)
valid_loader = torch_geometric.loader.DataLoader(valid_dataset, batch_size=1, shuffle=False)
test_loader  = torch_geometric.loader.DataLoader(test_dataset, batch_size=1, shuffle=False)

V_dim = train_dataset[0].V.shape[1]
E_dim = train_dataset[0].E.shape[1]
hidden_dim = 64
y_dim = 3

# standardizer = Standardizer(V_dim, E_dim, y_dim, train_loader, device)

model = GNS(V_dim, E_dim, hidden_dim, y_dim).to(device)

if len(sys.argv) == 2:
    criterion = VectorMSE()
elif len(sys.argv) == 5:
    criterion = Composition(float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]))

optimizer = torch.optim.Adam(model.parameters(), lr=0.0001)

# learner = Learner(standardizer, model, criterion, optimizer, device)
learner = Learner(model, criterion, optimizer, device)
train_info, valid_info = learner.learn(train_loader, valid_loader, num_epochs=10)

model_path = f"./model/{sys.argv[1]}/params.pth"
torch.save(model.state_dict(), model_path)

epoch = np.arange(len(train_info))
fig, ax = plt.subplots()
ax.plot(epoch, train_info.losses, label="train")
ax.plot(epoch, valid_info.losses, label="valid")
ax.set_title("learning curve")
ax.set_xlabel("epoch")
ax.set_ylabel("loss")
ax.legend(loc="upper right")
plt.savefig(f"./model/{sys.argv[1]}/learning_curve.png")