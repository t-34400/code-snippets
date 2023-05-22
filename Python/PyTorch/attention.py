import torch
import torch.nn as nn

# Attention機構を持つCNNモデルの定義
class AttentionCNN(nn.Module):
    def __init__(self, input_channels, hidden_size, output_size):
        super(AttentionCNN, self).__init__()
        self.hidden_size = hidden_size
        
        # CNNブロック
        self.conv1 = nn.Conv2d(input_channels, hidden_size, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(hidden_size, hidden_size, kernel_size=3, padding=1)
        
        # Attentionブロック
        self.attention = nn.Linear(hidden_size, 1)
        
        # 分類器
        self.fc = nn.Linear(hidden_size, output_size)
        
    def forward(self, x):
        # CNN処理
        x = self.conv1(x)
        x = torch.relu(x)
        x = self.conv2(x)
        x = torch.relu(x)
        
        # Attention処理
        attention_weights = torch.softmax(self.attention(x.view(x.size(0), -1)), dim=1)
        attention_vector = torch.mul(x.view(x.size(0), -1), attention_weights)
        attention_vector = attention_vector.sum(dim=1)
        
        # 分類器
        output = self.fc(attention_vector)
        return output

# ハイパーパラメータの設定
input_channels = 3  # 入力チャンネル数（画像のチャンネル数など）
hidden_size = 64  # CNNの隠れ層サイズ
output_size = 10  # クラス数などの出力サイズ

# 入力データの準備
data = [...]  # 画像データの読み込みや前処理

# データのテンソル化
inputs = torch.tensor(data, dtype=torch.float32)

# モデルの初期化
model = AttentionCNN(input_channels, hidden_size, output_size)

# 損失関数と最適化アルゴリズムの設定
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# モデルの学習
num_epochs = 100

for epoch in range(num_epochs):
    optimizer.zero_grad()
    output = model(inputs)
    
    # 損失の計算やバックプロパゲーション
    loss = criterion(output, targets)
    loss.backward()
    optimizer.step()

    if (epoch+1) % 10 == 0:
        print(f'Epoch: {epoch+1}, Loss: {loss.item()}')
