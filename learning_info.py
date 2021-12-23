class LearningInfo:
    def __init__(self) -> None:
        self.losses = []

    def append(self, loss: float) -> None:
        self.losses.append(loss)