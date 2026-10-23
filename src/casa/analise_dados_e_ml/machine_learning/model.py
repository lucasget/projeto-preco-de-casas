import torch
from torch import nn
class RedeNeuralV2(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer_1 = nn.Linear(in_features = 13, out_features = 64)
        self.relu1 = nn.ReLU()
        self.layer_2 = nn.Linear(in_features = 64, out_features = 64)
        self.relu2 = nn.ReLU()
        self.layer_3 = nn.Linear(in_features = 64, out_features = 32)
        self.relu3 = nn.ReLU()
        self.layer_4 = nn.Linear(in_features = 32, out_features = 1)
    def forward(self, x):
        x = self.relu1(self.layer_1(x))
        x = self.relu2(self.layer_2(x))
        x = self.relu3(self.layer_3(x))
        x = self.layer_4(x)
        return x