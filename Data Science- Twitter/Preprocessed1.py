import pandas as pd
data = pd.read_csv('tweeter_data_loc.csv')
#print(data)
pos = []
for indexer,row in data.iterrows():
    if( row['user_id']==row['tweet_id'] and row['user_id']==row['followers_count'] and row['user_id']==row['favourites_count'] ):
        #print(indexer)
        pos.append(indexer)
        #data = data.drop(data.index[indexer])

print(pos)
data.drop(data.index[pos], inplace=True)
print(data)
data.to_csv('tweeter2_data.csv', index=False)
