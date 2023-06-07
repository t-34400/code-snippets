class BottleNeckBlock(nn.Module):
    def __init__(self, input_size, output_size, hidden_size, stride=1, dropout_rate=0.3):
        super(BottleNeckBlock, self).__init__()
        self.cnn = nn.Sequential(
            nn.Conv1d(input_size, hidden_size, kernel_size=1, stride=stride, bias=False),
            nn.BatchNorm1d(hidden_size),
            nn.ReLU(),
            nn.Conv1d(hidden_size, hidden_size, kernel_size=3, stride=stride, padding=1, bias=False),
            nn.BatchNorm1d(hidden_size),
            nn.ReLU(),
            nn.Dropout(dropout_rate),
            nn.Conv1d(hidden_size, output_size, kernel_size=1, stride=stride, bias=False),
            nn.BatchNorm1d(output_size),
        )

        self.shortcut = nn.Sequential()
        if stride != 1 or input_size != output_size:
            self.shortcut = nn.Sequential(
                nn.Conv1d(input_size, output_size, kernel_size=1, stride=stride, bias=False),
                nn.BatchNorm1d(output_size)
            )

    def forward(self, x):
        residual = x
        out = self.cnn(x)
        out += self.shortcut(residual)
        out = F.relu(out)
        return out
