# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'camera_loading_gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Camera_loading_gui(object):
    def setupUi(self, Camera_loading_gui):
        Camera_loading_gui.setObjectName("Camera_loading_gui")
        Camera_loading_gui.resize(827, 660)
        self.centralWidget = QtWidgets.QWidget(Camera_loading_gui)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 791, 584))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 741, 81))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 2, 0, 1, 1)
        self.pushButton_Browse = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_Browse.setObjectName("pushButton_Browse")
        self.gridLayout_2.addWidget(self.pushButton_Browse, 1, 0, 1, 1)
        self.lineEdit_Browse = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_Browse.setObjectName("lineEdit_Browse")
        self.gridLayout_2.addWidget(self.lineEdit_Browse, 1, 1, 1, 1)
        self.pushButton_Load = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Load.sizePolicy().hasHeightForWidth())
        self.pushButton_Load.setSizePolicy(sizePolicy)
        self.pushButton_Load.setObjectName("pushButton_Load")
        self.gridLayout_2.addWidget(self.pushButton_Load, 1, 2, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 3, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 90, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem4, 3, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 460, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem6, 4, 0, 1, 1)
        self.gridLayout_pic = QtWidgets.QGridLayout()
        self.gridLayout_pic.setSpacing(6)
        self.gridLayout_pic.setObjectName("gridLayout_pic")
        self.gridLayout.addLayout(self.gridLayout_pic, 4, 1, 1, 1)
        Camera_loading_gui.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(Camera_loading_gui)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 827, 21))
        self.menuBar.setObjectName("menuBar")
        Camera_loading_gui.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(Camera_loading_gui)
        self.mainToolBar.setObjectName("mainToolBar")
        Camera_loading_gui.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(Camera_loading_gui)
        self.statusBar.setObjectName("statusBar")
        Camera_loading_gui.setStatusBar(self.statusBar)

        self.retranslateUi(Camera_loading_gui)
        QtCore.QMetaObject.connectSlotsByName(Camera_loading_gui)

    def retranslateUi(self, Camera_loading_gui):
        _translate = QtCore.QCoreApplication.translate
        Camera_loading_gui.setWindowTitle(_translate("Camera_loading_gui", "Camera_loading_gui"))
        self.groupBox.setTitle(_translate("Camera_loading_gui", "Load"))
        self.pushButton_Browse.setText(_translate("Camera_loading_gui", "Browse"))
        self.pushButton_Load.setText(_translate("Camera_loading_gui", "Load"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Camera_loading_gui = QtWidgets.QMainWindow()
    ui = Ui_Camera_loading_gui()
    ui.setupUi(Camera_loading_gui)
    Camera_loading_gui.show()
    sys.exit(app.exec_())

