import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Generate synthetic access logs
np.random.seed(0)
num_samples = 1000
start_date = datetime(2022, 1, 1)
end_date = datetime(2022, 1, 31)

timestamps = [start_date + timedelta(days=np.random.randint(0, 31), hours=np.random.randint(0, 23)) for _ in range(num_samples)]
resource_ids = np.random.randint(1, 1000, size=num_samples)
user_ids = np.random.randint(1, 100, size=num_samples)

access_logs = pd.DataFrame({'timestamp': timestamps, 'resource_id': resource_ids, 'user_id': user_ids})
access_logs.to_csv('access_logs.csv', index=False)
