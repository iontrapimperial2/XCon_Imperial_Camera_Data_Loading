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
        self.pic_height = 0
        self.pic_num = 1
        
        #-- Push Buttons -----------------------------------------------------#
        self.pushButton_Browse.clicked.connect(self.Browse_data)
        self.pushButton_Load.clicked.connect(self.import_data)
        self.pushButton_show.clicked.connect(self.show_kinetic)
        

        
        #-- plots -----------------------------------------------------#
        self.image = pg.GraphicsLayoutWidget()
        self.image.ci.layout.setColumnStretchFactor(0, 2)
        self.image.ci.layout.setColumnStretchFactor(1, 1)
        self.image.ci.layout.setRowStretchFactor(0, 1)
        self.image.ci.layout.setRowStretchFactor(1, 2)
        self.gridLayout_pic.addWidget(self.image)
        
        self.plot_image = self.image.addPlot(1, 0, rowspan=1, colspan=1)
        self.plot_image.setAspectLocked()

        self.projection_top = self.image.addPlot(0, 0, rowspan=1, colspan=1)
        self.projection_top.showGrid(x = True, y = True, alpha = 0.75) 
        self.projection_top.setXLink(self.plot_image)

        
        self.projection_side = self.image.addPlot(1, 1, rowspan=1, colspan=1)
        self.projection_side.showGrid(x = True, y = True, alpha = 0.75)
        self.projection_side.setYLink(self.plot_image)
        
        self.plot_timestamp = self.image.addPlot(0, 1, rowspan=1, colspan=1)
        self.plot_timestamp.hideAxis('bottom')
        self.plot_timestamp.hideAxis('left')
        
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
        try:
            a = filename.rfind('.')
            self.plot_image.clear()  # clear the plot before new plot
            self.projection_side.clear()
            self.projection_top.clear()
            with open(filename[:a] + '_cam_settings.txt') as file:
                cam_settings = list(csv.reader(file))
                
            if 'Kinetic' in str(cam_settings):
                self.comboBox_image_num.clear()
                self.start_row = int(str(cam_settings[14])[14:-2])
    
                self.end_row = int(str(cam_settings[15])[12:-2])
                self.start_col = int(str(cam_settings[12])[17:-2])
    
                self.end_col = int(str(cam_settings[13])[15:-2])
    
                self.pic_width = self.end_row - self.start_row + 1
                self.pic_height = self.end_col - self.start_col + 1
                self.pic_num = int(str(cam_settings[10])[26:-2])
                print(self.pic_num)
                print(self.pic_width)
                print(self.pic_height)
                self.comboBox_image_num.addItems(list(str(i) for i in range(0,self.pic_num+1,1)))
                
                with open(filename) as inputfile:
                    df = pd.read_csv(inputfile, header = None)
                    df.drop(df.columns[-1], axis=1, inplace=True)  #delete last column
                    df.drop(df.columns[0], axis=1, inplace=True)           #delete first column
                    plot = np.flip(np.array(df), axis = 0)
                    img = pg.ImageItem(np.rot90(plot,3), autoRange = True, autoLevels = True, autoHistogramRange = True)
                    self.plot_image.addItem(img)
                    
                    ##plot cross on pixel of highest count if check box is checked##
                    if self.checkBox_show_max.isChecked():
                        a = np.array(df).ravel()
                        b = max(a)
                        r = []
                        c = []
                        for row in range(df.shape[0]): 
                            for col in range(df.shape[1]):
                                if df.iat[row,col] == b:
                                    print(row, col)
                                    r.append(row+ 0.5)
                                    c.append(col+ 0.5)
                        data = r, c
                        print(data)
                        self.plot_image.plot(c,r, symbol = 'x', symbolBrush = (209,111,111,255))
                    else:
                        None
                    
                    ##Projection Plots##
                    self.pic_width = self.end_row - self.start_row + 1
                    self.pic_height = self.end_col - self.start_col + 1
                    col_pro = list(df.sum(axis = 0))
                    row_pro = list(df.sum(axis = 1))
                    col = list(np.arange(0.5, self.pic_height + 0.5, 1))
                    row = list(np.arange(0.5, self.pic_num*self.pic_width + 0.5, 1))
                    self.projection_top.plot(col,col_pro, pen='r')
                    self.projection_side.plot(row_pro,row, pen = 'r')
                    
                
            else:
                self.comboBox_image_num.clear()
                with open(filename) as inputfile:
                    df = pd.read_csv(inputfile, header = None)
                    df.drop(df.columns[-1], axis=1, inplace=True)  #delete last column
                    df.drop(df.columns[0], axis=1, inplace=True)   #delete first column
                    plot = np.flip(np.array(df), axis = 0)
                    img = pg.ImageItem(np.rot90(plot,3), autoRange = True, autoLevels = True, autoHistogramRange = True)
                    self.plot_image.addItem(img)
                    
                    ##plot cross on pixel of highest count if check box is checked##
                    if self.checkBox_show_max.isChecked():
                        a = np.array(df).ravel()
                        b = max(a)
                        r = []
                        c = []
                        for row in range(df.shape[0]): 
                            for col in range(df.shape[1]):
                                if df.iat[row,col] == b:
                                    print(row, col)
                                    r.append(row+ 0.5)
                                    c.append(col+ 0.5)
                        data = r, c
                        print(data)
                        self.plot_image.plot(c,r, symbol = 'x', symbolBrush = (209,111,111,255))
                    
                    else:
                        None
                    
                    ##Projection Plots##                        
                    self.start_row = int(str(cam_settings[10])[14:-2])
    
                    self.end_row = int(str(cam_settings[11])[12:-2])
                    self.start_col = int(str(cam_settings[8])[17:-2])
            
                    self.end_col = int(str(cam_settings[9])[15:-2])
            
                    self.pic_width = self.end_row - self.start_row + 1
                    self.pic_height = self.end_col - self.start_col + 1
                    col_pro = list(df.sum(axis = 0))
                    row_pro = list(df.sum(axis = 1))
                    col = list(np.arange(0.5, self.pic_height + 0.5, 1))
                    row = list(np.arange(0.5, self.pic_width + 0.5, 1))
                    self.projection_top.plot(col,col_pro, pen='r')
                    self.projection_side.plot(row_pro,row, pen = 'r')



            print('load success')
        except:
            print('load error')

#-- shows each picture in kinetic series separately -----------------------------------------------------#
    def show_kinetic(self):
        filename = str(self.lineEdit_Browse.text())
        self.plot_image.clear()
        self.projection_side.clear()
        self.projection_top.clear()
        with open(filename) as inputfile:
            try:
                df1 = pd.read_csv(inputfile, header = None)
                df1.drop(df1.columns[-1], axis=1, inplace=True)  #delete last column
                df1.drop(df1.columns[0], axis=1, inplace=True)   #delete first column
                if int(self.comboBox_image_num.currentText()) == 0:
                    plot = np.flip(np.array(df1), axis = 0)
                    img = pg.ImageItem(np.rot90(plot,3), autoRange = True, autoLevels = True, autoHistogramRange = True)
                    self.plot_image.addItem(img)
                    
                    ##plot cross on pixel of highest count if check box is checked##
                    if self.checkBox_show_max.isChecked():
                        a = np.array(df1).ravel()
                        b = max(a)
                        r = []
                        c = []
                        for row in range(df1.shape[0]): 
                            for col in range(df1.shape[1]):
                                if df1.iat[row,col] == b:
                                    print(row, col)
                                    r.append(row+ 0.5)
                                    c.append(col+ 0.5)
                        data = r, c
                        print(data)
                        self.plot_image.plot(c,r, symbol = 'x', symbolBrush = (209,111,111,255))
                    else:
                        None
                    
                    ##Projection Plots##
                    self.pic_width = self.end_row - self.start_row + 1
                    self.pic_height = self.end_col - self.start_col + 1
                    col_pro = list(df1.sum(axis = 0))
                    row_pro = list(df1.sum(axis = 1))
                    col = list(np.arange(0.5, self.pic_height + 0.5, 1))
                    row = list(np.arange(0.5, self.pic_num*self.pic_width + 0.5, 1))
                    self.projection_top.plot(col,col_pro, pen='r')
                    self.projection_side.plot(row_pro,row, pen = 'r')
                    
                else:
                    num = int(self.comboBox_image_num.currentText())
                    a = list(range(num*self.pic_width, (self.pic_num*self.pic_width), 1))
                    b = a +list(range(0, (num-1)*self.pic_width,1))
                    pic = df1.drop(b)
                    plot = np.flip(np.array(pic), axis = 0)
                    img = pg.ImageItem(np.rot90(plot,3), autoRange = True, autoLevels = True, autoHistogramRange = True)
                    self.plot_image.addItem(img)
                    
                    ##plot cross on pixel of highest count if check box is checked##
                    if self.checkBox_show_max.isChecked():
                        a = np.array(pic).ravel()
                        b = max(a)
                        r = []
                        c = []
                        for row in range(pic.shape[0]): 
                            for col in range(pic.shape[1]):
                                if pic.iat[row,col] == b:
                                    print(row, col)
                                    r.append(row+ 0.5)
                                    c.append(col+ 0.5)
                        data = r, c
                        print(data)
                        self.plot_image.plot(c,r, symbol = 'x', symbolBrush = (209,111,111,255))
                    else:
                        None
                    
                    ##Projection Plots##
                    self.pic_width = self.end_row - self.start_row + 1
                    self.pic_height = self.end_col - self.start_col + 1
                    col_pro = list(pic.sum(axis = 0))
                    row_pro = list(pic.sum(axis = 1))
                    col = list(np.arange(0.5, self.pic_height + 0.5, 1))
                    row = list(np.arange(0.5, self.pic_width + 0.5, 1))
                    self.projection_top.plot(col,col_pro, pen='r')
                    self.projection_side.plot(row_pro,row, pen = 'r')
                
                
                print('load success')
            except:
                print('not a kinetic image')



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    
    dialog = QtWidgets.QMainWindow()
    
    programm = window(dialog)
    dialog.show()
    
    sys.exit(app.exec_())