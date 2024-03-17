def should_cache(resource_id, hour_of_day, day_of_week, resource_popularity):
    prediction = clf.predict([[hour_of_day, day_of_week, resource_popularity]])[0]
    return prediction == 1

# Example usage
resource_id_to_cache = 123
hour_of_day = 15
day_of_week = 2
resource_popularity = 50

if should_cache(resource_id_to_cache, hour_of_day, day_of_week, resource_popularity):
    print(f'Resource {resource_id_to_cache} should be cached.')
else:
    print(f'Resource {resource_id_to_cache} should not be cached.')
