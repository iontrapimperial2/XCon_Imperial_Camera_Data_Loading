# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 14:36:24 2019

@author: IonTrap/YWu
"""

import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog
import csv
import pyqtgraph as pg
import numpy as np
import pandas as pd

from camera_loading_gui import Ui_Camera_loading_gui

class window(Ui_Camera_loading_gui):
    
    def __init__(self, dialog):
        Ui_Camera_loading_gui.__init__(self)
        self.setupUi(dialog)
        
        self.filename = ''
        
        
        self.start_col = 0
        self.end_col = 0
        self.start_row = 0
        self.end_row = 0
        self.pic_width = 0
        self.pic_num = 1
        
        #-- Push Buttons -----------------------------------------------------#
        self.pushButton_Browse.clicked.connect(self.Browse_data)
        self.pushButton_Load.clicked.connect(self.import_data)
        self.pushButton_show.clicked.connect(self.show_kinetic)
        
        #-- Pic show -----------------------------------------------------#
        self.show_pic = pg.PlotItem()
        self.plot_pic = pg.ImageView(view = self.show_pic)
        self.plot_pic.view.invertY(False)
        #self.show_pic.showAxis('top')
        #self.show_pic.hideAxis('bottom')
        
        
        self.show_pic.setAspectLocked(True)
        self.gridLayout_pic.addWidget(self.plot_pic)
        self.plot_pic.getHistogramWidget().setHistogramRange(0,512)
        

        
        
        self.vline = pg.InfiniteLine(angle = 90, movable = False)
        self.hline = pg.InfiniteLine(angle = 0, movable = False)
        self.show_pic.addItem(self.vline, ignoreBounds = True)
        self.show_pic.addItem(self.hline, ignoreBounds = True)
        self.plot_pic.show()
        
        
    def Browse_data(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog    
        self.filename_load, _ = QFileDialog.getOpenFileName(None,"import data", "","all files (*);; asc files (*.asc);; txt files (*.txt)", options=options)
        
        if self.filename_load:
            self.lineEdit_Browse.setText(self.filename_load)
    
    def import_data(self):
        ### read filename
        self.filename = str(self.lineEdit_Browse.text())

        ### load and prepare data
        try:
            self.Load_data(self.filename)
        except FileNotFoundError:
            print('nothing found to that name')
        except UnicodeDecodeError:
            print('not a suitable file format selected')
        
    def Load_data(self,filename):

                    
       # try:
        a = filename.rfind('.')
        with open(filename[:a] + '_cam_settings.txt') as file:
            cam_settings = list(csv.reader(file))
        if 'Kinetic' in str(cam_settings):
            self.start_row = int(str(cam_settings[14])[14:-2])

            self.end_row = int(str(cam_settings[15])[12:-2])

            self.pic_width = self.end_row - self.start_row + 1
            self.pic_num = int(str(cam_settings[10])[26:-2])
            print(self.pic_num)
            print(self.pic_width)
            self.comboBox_image_num.addItems(list(str(i) for i in range(0,self.pic_num+1,1)))
            
            with open(filename) as inputfile:
                df = pd.read_csv(inputfile, header = None)
                df.drop(df.columns[-1], axis=1, inplace=True)  #delete last column
                df.drop(df.columns[0], axis=1, inplace=True)           #delete first column
                plot = np.array(df)
                self.plot_pic.setImage(plot, autoRange = True, autoLevels = True, autoHistogramRange = True)
                
            
        else:
            self.comboBox_image_num.clear()
            with open(filename) as inputfile:
                df = pd.read_csv(inputfile, header = None)
                df.drop(df.columns[-1], axis=1, inplace=True)  #delete last column
                df.drop(df.columns[0], axis=1, inplace=True)   #delete first column
                print('load success')
                plot = np.array(df)
                self.plot_pic.setImage(plot, autoRange = True, autoLevels = True, autoHistogramRange = True)
   
        with open(filename) as inputfile:

            df = pd.read_csv(inputfile, header = None)

            a = list(i for i in range(2*self.pic_width, self.pic_num*self.pic_width, 1))
            a = a +list(i for i in range(0, self.pic_width,1))
            #print(a)
            df.drop(a, inplace=True)
            df.drop(df.columns[-1], axis=1, inplace=True)  #delete last column
            df.drop(df.columns[0], axis=1, inplace=True)           #delete first column
            
            #i
            #print(df)
        #plt.figure()
            print('load success')
        #plot = np.array(df)
        #self.plot_pic.setImage(plot, autoRange = True, autoLevels = True, autoHistogramRange = True)
       # except:
        #    print('load error')

    def show_kinetic(self):
        filename = str(self.lineEdit_Browse.text())
        with open(filename) as inputfile:
            if int(self.comboBox_image_num.currentText()) == 0:
                df = pd.read_csv(inputfile, header = None)
                df.drop(df.columns[-1], axis=1, inplace=True)  #delete last column
                df.drop(df.columns[0], axis=1, inplace=True)   #delete first column
                print('load success')
                plot = np.array(df)
                self.plot_pic.setImage(plot, autoRange = True, autoLevels = True, autoHistogramRange = True)
            else:
                df = pd.read_csv(inputfile, header = None)
                df.drop(df.columns[-1], axis=1, inplace=True)  #delete last column
                df.drop(df.columns[0], axis=1, inplace=True)           #delete first column
                num = int(self.comboBox_image_num.currentText())
                a = list((num*self.pic_width, self.pic_num*self.pic_width, 1))
                a = a +list(range(0, (num-1)*self.pic_width,1))
                pic = df.drop(a)
                plot = np.array(pic)
                self.plot_pic.setImage(plot, autoRange = True, autoLevels = True, autoHistogramRange = True)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    
    dialog = QtWidgets.QMainWindow()
    
    programm = window(dialog)
    dialog.show()
    
    sys.exit(app.exec_())