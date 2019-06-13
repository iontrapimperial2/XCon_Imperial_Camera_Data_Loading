# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 16:45:08 2019

@author: IonTrap/JMHeinrich
"""
import matplotlib.pyplot as plt   
import pandas as pd
#import numpy as np

#df = pd.read_csv('C:/Users/IonTrap/code/python/XCon_Imperial_Camera_2/test.txt', header = None)


#class show_pic():
#    def __init__(self):
#        self.df = None

def load_file(filname):
    df = pd.read_csv(filname, header = None)
    Num_cols = len(df.columns)                             #no. of columns
    df.drop(df.columns[Num_cols-1], axis=1, inplace=True)  #delete last column
    df.drop(df.columns[0], axis=1, inplace=True)           #delete first column
    plt.figure()
    plt.imshow(df)
    plt.gca().invert_yaxis()                               #inverts y axis for correct orientation
    
    plt.show()

a = 'C:/Users/IonTrap/code/python/XCon_Imperial_Camera_2/test.txt'
b = 'C:/Users/IonTrap/code/python/XCon_Imperial_Camera_Data_Loading/test.txt'
c = 'C:/Users/IonTrap/code/python/XCon_Imperial_Camera_Data_Loading/test1.txt'

load_file(a)
load_file(b)
load_file(c)
    
    