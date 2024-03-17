import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Generate synthetic access logs
np.random.seed(0)
num_samples = 1000
resource_ids = np.random.randint(1, 1000, size=num_samples)
user_ids = np.random.randint(1, 100, size=num_samples)

access_logs = pd.DataFrame({'resource_id': resource_ids, 'user_id': user_ids})

# Generate synthetic content features (e.g., embeddings)
num_resources = 1000
content_embeddings = np.random.rand(num_resources, 100)  # Example embeddings (100-dimensional)

similarity_matrix = cosine_similarity(content_embeddings)
