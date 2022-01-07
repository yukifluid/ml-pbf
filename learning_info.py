class LearningInfo:
    def __init__(self) -> None:
        self.losses = []
        self.dp_abs = []
        self._n = 0

    def append(self, loss: float, dp_abs: float) -> None:
        self.losses.append(loss)
        self.dp_abs.append(dp_abs)
        self._n += 1

    def __len__(self) -> int:
        return self._n