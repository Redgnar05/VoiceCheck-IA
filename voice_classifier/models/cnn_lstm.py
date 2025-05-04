
# /voice_classifier/models/cnn_latm.py

import torch
import torch.nn as nn

class MiModelo(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 16, kernel_size=3, padding=1)
        self.relu = nn.ReLU()
        self.lstm = nn.LSTM(input_size=16 * 128, hidden_size=32, batch_first=True)
        self.fc = nn.Linear(32, 1)

    def forward(self, x):
        x = self.relu(self.conv1(x))
        x = x.permute(0, 3, 1, 2)
        x = x.reshape(x.size(0), x.size(1), -1)
        x, _ = self.lstm(x)
        x = x[:, -1, :]
        x = self.fc(x)
        return torch.sigmoid(x)




