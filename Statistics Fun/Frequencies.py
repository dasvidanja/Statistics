#Frequency Table: Frequency, Cumulative Frequency, Relative Frequency, Cumulative Relative Frequency
'''Problem: Cumulative & relative Frequencies :) '''

import numpy as np 

#The data reppresents similar groups in each category  (1,2,3,...)
#The first & second colum (list) reppresent measurments from the distinct groups
# category 1: [group A,group B]
data = {1: [12,0], 
        2: [8,18],
        3: [2,2],
        4: [2,2],
        5: [1,1],
        6: [0,1],
        9: [0,1] }
#Check out data
print(data)

#Cumulative Frequencies group A
cum_freq=[]
temp =0.0
for x in data.values():
    temp +=x[0]
    cum_freq.append(temp)
print(cum_freq)

#Relative Frequencies group A 
rel_freq=[]
temp =0.0
for x in data.values():
    temp =x[0]/25
    rel_freq.append(temp)
print(rel_freq)

#Cumulative Relative Frequencies group A 
cum_rel_freq=[]
temp =0.0
for x in data.values():
    temp +=x[0]/25
    cum_rel_freq.append(temp)
print(cum_rel_freq)

#Cumulative Frequencies group B
cum_freq=[]
temp =0.0
for x in data.values():
    temp +=x[1]
    cum_freq.append(temp)
print(cum_freq)

#Relative Frequencies group A 
rel_freq=[]
temp =0.0
for x in data.values():
    temp =x[1]/25
    rel_freq.append(temp)
print(rel_freq)

#Cumulative Relative Frequencies group A 
cum_rel_freq=[]
temp =0.0
for x in data.values():
    temp +=x[1]/25
    cum_rel_freq.append(temp)
print(cum_rel_freq)
