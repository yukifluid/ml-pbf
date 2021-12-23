import random
import numpy as np
import torch
import torch_geometric
from dataset import PBFSimple

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