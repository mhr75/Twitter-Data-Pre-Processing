import pandas as pd
data = pd.read_csv('tweeter3_data.csv')
sop = []
bol = False
for index, row in data.iterrows():
    user = row['user_id']
    bool = False
    pos=[]
    pos.append(index)
    for index2,row2 in data.iterrows():
        if(index < index2):
            user2 = row2['user_id']
            if(user == user2):
                pos.append(index2)
                if(row['location'] != row2['location']):
                    #print(index,index2)
                    bool = True
                    print('yes')

    if(bool==True):
        bol=True
        sop = pos.copy()
    #print(sop)
if(bol == True):
    print('ye')
    print(sop)
df= data.loc[sop]
print(df)
df.to_csv('final_outcome.csv', index=False)