import torch


class Regression(torch.nn.Module):
    def __init__(self, n_feature, n_hidden, n_output):
        super().__init__()
        self.hidden = torch.nn.Linear(n_feature, n_hidden)
        self.predict = torch.nn.Linear(n_hidden, n_output)

    def forward(self, input_batch: torch.Tensor) -> torch.Tensor:
        hidden = torch.nn.ReLU()(self.hidden(input_batch))
        return self.predict(hidden)
