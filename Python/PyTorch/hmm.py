import torch
import torch.nn as nn
import torch.optim as optim

class HMM(nn.Module):
    def __init__(self, num_states, num_observations):
        super(HMM, self).__init__()
        self.num_states = num_states
        self.num_observations = num_observations

        # Transition matrix
        self.transitions = nn.Parameter(torch.randn(num_states, num_states))

        # Emission matrix
        self.emissions = nn.Parameter(torch.randn(num_states, num_observations))

    def forward(self, observations):
        num_sequences, sequence_length = observations.shape
        num_states = self.num_states

        # Initialize the alpha and beta matrices
        alpha = torch.zeros(num_sequences, sequence_length, num_states)
        beta = torch.zeros(num_sequences, sequence_length, num_states)

        # Forward algorithm
        alpha[:, 0] = self.emissions[:, observations[:, 0]]
        for t in range(1, sequence_length):
            alpha[:, t] = torch.matmul(alpha[:, t - 1], self.transitions) * self.emissions[:, observations[:, t]]

        # Backward algorithm
        beta[:, sequence_length - 1] = 1.0
        for t in range(sequence_length - 2, -1, -1):
            beta[:, t] = torch.matmul(self.transitions, (self.emissions[:, observations[:, t + 1]] * beta[:, t + 1]))

        # Compute the marginal probabilities
        gamma = alpha * beta / torch.sum(alpha * beta, dim=2, keepdim=True)

        # Decode the most likely states
        _, predicted_labels = gamma.max(dim=2)

        return predicted_labels

# Define the training data
observations = torch.tensor([0, 1, 1, 0, 0])  # Observations

# Create the HMM model
num_states = 4
num_observations = 2
model = HMM(num_states, num_observations)

# Define the loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.1)

# Training loop
num_epochs = 100
for epoch in range(num_epochs):
    # Forward pass
    logits = model(observations.unsqueeze(0))
    loss = criterion(logits.view(-1, num_states), observations.unsqueeze(0).view(-1))

    # Backward pass and optimization
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    # Print the loss for monitoring
    if (epoch + 1) % 10 == 0:
        print(f"Epoch {epoch+1}/{num_epochs}, Loss: {loss.item()}")

# Predict the labels for new observations
predicted_labels = model(observations.unsqueeze(0))
print("Predicted Labels:", predicted_labels.squeeze())
