class LearningInfo:
    def __init__(self) -> None:
        self.losses = []
        self._n = 0

    def append(self, loss: float) -> None:
        self.losses.append(loss)
        self._n += 1

    def __len__(self) -> int:
        return self._n