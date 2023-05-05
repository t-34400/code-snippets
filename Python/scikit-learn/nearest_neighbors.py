from sklearn.neighbors import NearestNeighbors
import numpy as np

train_coords = np.array([[0, 0, 0], [1, 1, 1], [2, 2, 2], [3, 3, 3]])
train_floats = np.array([[0.1, 0.2], [0.3, 0.4], [0.5, 0.6], [0.7, 0.8]])

test_coords = np.array([[0.5, 0.5, 0.5], [2.5, 2.5, 2.5]])

k = 2
nn = NearestNeighbors(n_neighbors=k, algorithm='auto').fit(train_coords)

_, indices = nn.kneighbors(test_coords)

test_floats = np.mean(train_floats[indices], axis=1)

print(test_floats)