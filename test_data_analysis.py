# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 16:45:08 2019

@author: IonTrap/JMHeinrich
"""
import matplotlib.pyplot as plt   
import pandas as pd
#import numpy as np

#df = pd.read_csv('C:/Users/IonTrap/code/python/XCon_Imperial_Camera_2/test.txt', header = None)

a = 'C:/Users/IonTrap/code/python/XCon_Imperial_Camera_2/section_test2.txt'
df = pd.read_csv(a, header = None)

def load_file(filname):
    df = pd.read_csv(filname, header = None)
    df.drop(df.columns[-1], axis=1, inplace=True)  #delete last column
    df.drop(df.columns[0], axis=1, inplace=True)           #delete first column
    print(df)
    plt.figure()
    plt.imshow(df)
    plt.gca().invert_yaxis()                               #inverts y axis for correct orientation
    plt.show()


#b = 'C:/Users/IonTrap/code/python/XCon_Imperial_Camera_Data_Loading/test.txt'
#c = 'C:/Users/IonTrap/code/python/XCon_Imperial_Camera_Data_Loading/test1.txt'

load_file(a)

#load_file(b)
#load_file(c)
    
    