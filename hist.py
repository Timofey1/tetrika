import pandas as pd
data=pd.read_csv("hist.txt",delimiter="\t",names = ["1","ip","3"])
print(data.ip.value_counts().head())
'''
output:
101.255.10.103     195
36.79.145.227      177
154.157.157.156    176
240.124.194.168    173
126.159.54.179     172
Name: ip, dtype: int64

'''
