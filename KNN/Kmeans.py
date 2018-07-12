#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 15:02:38 2018

@author: luohaozheng
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import copy
x=list()
y=list()
fp=open('datapoint.csv','r')
title=fp.readline()
for line in fp:
    l1=line.split(',')
    x.append(float(l1[0]))
    y.append(float(l1[1]))
data=pd.DataFrame({'x':x,'y':y})
k = 3
# centroids[i] = [x, y]
cent = {1:[-1,0],2:[0.5,1],3:[1,-1]}
colmap = {1: 'r', 2: 'b', 3: 'y'}

def assignment(data, cent):
    list2=[]
    for i in cent.keys():
        cent_distance_cols='{}'.format(i)
        list2.append(cent_distance_cols)
        data[cent_distance_cols] = (np.sqrt((data['x'] - cent[i][0]) ** 2 + (data['y'] - cent[i][1]) ** 2))
        data['closest'] = data.loc[:, list2].idxmin(axis=1)
        data['closest'] = data['closest'].map(lambda x: int(x))
        data['color']=data['closest'].map(lambda x: colmap[x])
    return data

data= assignment(data, cent)
def update(cent):
    for i in cent.keys():
            cent[i][0] = np.mean(data[data['closest'] == i]['x'])
            cent[i][1] = np.mean(data[data['closest'] == i]['y'])
            if all(np.isnan(cent[i]))==True:
                cent[i][0]=old[i][0]
                cent[i][1]=old[i][1]
    return cent
n=0
Done= True
while Done:
    old=copy.deepcopy(cent)
    cent = update(cent)
    data= assignment(data, cent)
    for j in cent.keys():
        if (abs(old[j][0]-cent[j][0])>0.1) or (abs(old[j][1]-cent[j][1])>0.1):
            break
        elif ((abs(old[j][0]-cent[j][0])<=0.1) or (abs(old[j][1]-cent[j][1])<=0.1))and j==3:
            Done=False
        else:
            continue
    n+=1 

for i in cent.keys():
    plt.scatter(*cent[i], color=colmap[i])
fig = plt.figure(figsize=(5, 5))
plt.scatter(data['x'], data['y'], color=data['color'], alpha=0.5, edgecolor='k')
plt.xlim(-2,2)
plt.ylim(-2,2)
plt.show()
print('you should run '+str(n) +' times')




