# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 14:36:24 2019

@author: IonTrap/YWu
"""

import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog
import random
import pyqtgraph as pg
import numpy as np
import pandas as pd

from camera_loading_gui import Ui_Camera_loading_gui

class window(Ui_Camera_loading_gui):
    
    def __init__(self, dialog):
        Ui_Camera_loading_gui.__init__(self)
        self.setupUi(dialog)
        
        self.filename = ''
        
        
        
        #-- Push Buttons -----------------------------------------------------#
        self.pushButton_Browse.clicked.connect(self.Browse_data)
        self.pushButton_Load.clicked.connect(self.import_data)
        
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
        with open(filename) as inputfile:
            df = pd.read_csv(inputfile, header = None)
            df.drop(df.columns[-1], axis=1, inplace=True)  #delete last column
            df.drop(df.columns[0], axis=1, inplace=True)           #delete first column
        #plt.figure()
            print('load success')
        plot = np.array(df)
        self.plot_pic.setImage(plot, autoRange = True, autoLevels = True, autoHistogramRange = True)
        

            
        
        #self.show_pic.gca().invert_yaxis()                               #inverts y axis for correct orientation
        
        #self.show_pic.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    
    dialog = QtWidgets.QMainWindow()
    
    programm = window(dialog)
    dialog.show()
    
    sys.exit(app.exec_())