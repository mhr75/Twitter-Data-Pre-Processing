import pandas as pd
data = pd.read_csv('tweeter2_data.csv')
ids = data["user_id"]
df = data[ids.isin(ids[ids.duplicated()])]
df.to_csv('tweeter3_data.csv', index=False)