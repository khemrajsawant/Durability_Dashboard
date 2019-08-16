# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Khemraj)s
"""
import pandas as pd
import matplotlib.pyplot as plt
import import_data
# Extract microtrips ::
def microtrip(spd):
    cnt = []
    for spd1 in spd:
        if spd1 > 0:
            cnt.append(1)
        else:
            cnt.append(0)
    return cnt

df = import_data.import_data()
speed = df['vehiclespeedvsosig__0x101 (Km/h)']
df['mt_no'] =microtrip(speed)

df['mt_no_gr'] = (df['mt_no'].diff(1) != 0).astype('int').cumsum()
print(df['mt_no_gr'])

plt.plot(df['vehiclespeedvsosig__0x101 (Km/h)'][df['mt_no_gr']==100])

def summary_stats(df,n,mt_num):
    st = df.iloc[:,n][df['mt_no_gr']==mt_num].describe().transpose()
    return st

print(summary_stats(df,1,12))
plt.plot(df['mt_no'])
plt.show()
fig = plt.plot(df['vehiclespeedvsosig__0x101 (Km/h)'][df['mt_no_gr']==10])
