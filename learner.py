import time
from matplotlib.pyplot import axis
import torch
import torch_geometric
from learning_info import LearningInfo
from graph import Graph

class Learner:
    def __init__(self, standardizer, model, criterion, optimizer, device: torch.device) -> None:
    # def __init__(self, model, criterion, optimizer, device: torch.device) -> None:
        self._standardizer = standardizer
        self._model        = model
        self._criterion    = criterion
        self._optimizer    = optimizer
        self._device       = device

    def learn(self, train_loader: torch_geometric.loader.DataLoader, valid_loader: torch_geometric.loader.DataLoader, num_epochs: int) -> LearningInfo:
        train_info = LearningInfo()
        valid_info = LearningInfo()

        for epoch in range(num_epochs):
            epoch_start_time_s = time.time()

            self.train(train_loader, train_info)
            self.valid(valid_loader, valid_info)

            epoch_end_time_s = time.time()
            epoch_elapsed_time_m = (epoch_end_time_s - epoch_start_time_s) / 60

            print(self._epoch_log(epoch, num_epochs, train_info, valid_info, epoch_elapsed_time_m), flush=True)

        return train_info, valid_info

    def train(self, train_loader: torch_geometric.loader.DataLoader, info: LearningInfo) -> None:
        self._model.train()

        sum_loss = 0

        for batch in train_loader:
            batch = batch.to(self._device)

            V, E, y = self._standardizer.standardize(batch.V, batch.E, batch.y)

            graph = Graph(V, E, batch.N)

            self._optimizer.zero_grad()

            pred = self._model(graph)

            loss = self._criterion(pred[batch.num_boundary_particles:], y[batch.num_boundary_particles:], self._standardizer)
            # loss = self._criterion(pred, batch)

            loss.backward()
            self._optimizer.step()

            sum_loss += loss.item()

        avg_loss = sum_loss / len(train_loader)

        info.append(avg_loss, torch.mean(torch.abs(self._standardizer.inverse_y(pred[batch.num_boundary_particles:])), axis=0))
        # info.append(avg_loss, torch.mean(torch.abs(pred[batch.num_boundary_particles:])).item())

    def valid(self, valid_loader: torch_geometric.loader.DataLoader, info: LearningInfo) -> None:
        self._model.eval()

        sum_loss = 0

        with torch.no_grad():
            for batch in valid_loader:
                batch = batch.to(self._device)
                V, E, y = self._standardizer.standardize(batch.V, batch.E, batch.y)

                graph = Graph(V, E, batch.N)

                pred = self._model(graph)

                loss = self._criterion(pred[batch.num_boundary_particles:], y[batch.num_boundary_particles:], self._standardizer)
                # loss = self._criterion(pred, batch)

                sum_loss += loss.item()

            avg_loss = sum_loss / len(valid_loader)

            info.append(avg_loss, torch.mean(torch.abs(self._standardizer.inverse_y(pred[batch.num_boundary_particles:])), axis=0))
            # info.append(avg_loss, torch.mean(torch.abs(pred[batch.num_boundary_particles:])).item())

    def test(self):
        self.model.eval()
        with torch.no_grad():
            pass

    def _epoch_log(self, epoch: int, num_epochs: int, train_info: LearningInfo, valid_info: LearningInfo, epoch_elapsed: float) -> str:
        log = "epoch: {:5d}/{:5d} | train_loss: {:.10f} | train_dp: {} | valid_loss: {:.10f} | valid_dp: {} | elapsed: {:.3f} min" \
            .format(epoch, num_epochs, train_info.losses[epoch], train_info.dp_abs[epoch], valid_info.losses[epoch], valid_info.dp_abs[epoch], epoch_elapsed)
        return log