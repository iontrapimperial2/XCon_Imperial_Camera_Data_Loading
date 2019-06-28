# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 16:45:08 2019

@author: IonTrap/JMHeinrich
"""
import matplotlib.pyplot as plt   
import pandas as pd
import numpy as np

#df = pd.read_csv('C:/Users/IonTrap/code/python/XCon_Imperial_Camera_2/test.txt', header = None)

a = 'C:/Users/iontrap/Documents/iontrap/code/python/XCon_Imperial_Camera_2/Single_ion/Exposure_test/Exposure20.txt'
#df = pd.read_csv(a, header = None)

#def load_file(filname):
df = pd.read_csv(a, header = None)
df.drop(df.columns[-1], axis=1, inplace=True)  #delete last column
df.drop(df.columns[0], axis=1, inplace=True)           #delete first column
#print(df)
a = np.array(df)

b = a.ravel()

#c = [i if i >= np.mean(b) else 0 for i in b.all()]
d = max(b)
#print(c)#
r = []
c = []
for row in range(df.shape[0]): 
    for col in range(df.shape[1]):
        if df.iat[row,col] == d:
            print(row, col)
            r.append(row)
            c.append(col)
             
e = 1.5*np.mean(b)
new_data = []
for i in b:
    if i < e:        
        #df = df.replace(i,0)
        new_data.append(0)

    else:
        new_data.append(i)

#df = np.reshape(new_data, (512,512))
plt.figure()
plt.imshow(df)
plt.plot(c,r,'rx')

plt.gca().invert_yaxis()                               #inverts y axis for correct orientation
plt.show()


#b = 'C:/Users/IonTrap/code/python/XCon_Imperial_Camera_Data_Loading/test.txt'
#c = 'C:/Users/IonTrap/code/python/XCon_Imperial_Camera_Data_Loading/test1.txt'

#load_file(a)

#load_file(b)
#load_file(c)
    
    