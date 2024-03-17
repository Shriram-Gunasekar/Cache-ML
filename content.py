class ContentBasedCache:
    def __init__(self, similarity_matrix, threshold=0.7):
        self.similarity_matrix = similarity_matrix
        self.threshold = threshold

    def should_cache(self, resource_id, user_id):
        similar_resources = self.similarity_matrix[resource_id]
        most_similar_idx = np.argmax(similar_resources)
        similarity_score = similar_resources[most_similar_idx]
        if similarity_score > self.threshold:
            return True
        else:
            return False

# Initialize Content-Based Cache with similarity matrix
content_cache = ContentBasedCache(similarity_matrix, threshold=0.7)
