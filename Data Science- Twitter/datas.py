import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import csv
import math

data = pd.read_csv('cln_txt_DOT.csv')
#print(data)              656 x 16383
df = pd.DataFrame(data)
df1 = df.dropna(how='any', axis=1)
#print(df1)  # 656 x 10; excluding coordinates and cln_txt
data_cln_txt = data['cln_txt'].copy()
df1['cln_txt'] = data_cln_txt
df1.to_csv('tweeter_data_loc.csv', index=False)

#print(df1) # 6566 x 11 inluding cln_txt
#for col in df1.columns:
#    print(col)   # checking column names
#print(df1.head(10))
#df2 = df1[df1.duplicated(subset=["user_id"], keep=False)]
#df2 = df1.loc[(df1.groupby('user_id').count()> 1).sum(axis=1), :]
#print(df2['user_id'])
