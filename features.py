def extract_features(df):
    df['hour_of_day'] = df['timestamp'].dt.hour
    df['day_of_week'] = df['timestamp'].dt.dayofweek
    resource_popularity = df['resource_id'].value_counts().to_dict()
    df['resource_popularity'] = df['resource_id'].map(resource_popularity)
    return df

access_logs = pd.read_csv('access_logs.csv')
access_logs['timestamp'] = pd.to_datetime(access_logs['timestamp'])
access_logs = extract_features(access_logs)
