/********************************************************************************
** Form generated from reading UI file 'camera_loading_gui.ui'
**
** Created by: Qt User Interface Compiler version 5.6.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_CAMERA_LOADING_GUI_H
#define UI_CAMERA_LOADING_GUI_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Camera_loading_gui
{
public:
    QWidget *centralWidget;
    QWidget *gridLayoutWidget;
    QGridLayout *gridLayout;
    QVBoxLayout *verticalLayout;
    QGroupBox *groupBox;
    QWidget *gridLayoutWidget_2;
    QGridLayout *gridLayout_2;
    QSpacerItem *horizontalSpacer_3;
    QSpacerItem *horizontalSpacer_2;
    QSpacerItem *horizontalSpacer_4;
    QSpacerItem *horizontalSpacer_5;
    QPushButton *pushButton_Browse;
    QLineEdit *lineEdit;
    QPushButton *pushButton_Load;
    QSpacerItem *verticalSpacer;
    QSpacerItem *horizontalSpacer;
    QSpacerItem *verticalSpacer_2;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *Camera_loading_gui)
    {
        if (Camera_loading_gui->objectName().isEmpty())
            Camera_loading_gui->setObjectName(QStringLiteral("Camera_loading_gui"));
        Camera_loading_gui->resize(827, 660);
        centralWidget = new QWidget(Camera_loading_gui);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        gridLayoutWidget = new QWidget(centralWidget);
        gridLayoutWidget->setObjectName(QStringLiteral("gridLayoutWidget"));
        gridLayoutWidget->setGeometry(QRect(10, 10, 791, 581));
        gridLayout = new QGridLayout(gridLayoutWidget);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        gridLayout->setContentsMargins(0, 0, 0, 0);
        verticalLayout = new QVBoxLayout();
        verticalLayout->setSpacing(6);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));

        gridLayout->addLayout(verticalLayout, 4, 1, 1, 1);

        groupBox = new QGroupBox(gridLayoutWidget);
        groupBox->setObjectName(QStringLiteral("groupBox"));
        gridLayoutWidget_2 = new QWidget(groupBox);
        gridLayoutWidget_2->setObjectName(QStringLiteral("gridLayoutWidget_2"));
        gridLayoutWidget_2->setGeometry(QRect(10, 10, 741, 81));
        gridLayout_2 = new QGridLayout(gridLayoutWidget_2);
        gridLayout_2->setSpacing(6);
        gridLayout_2->setContentsMargins(11, 11, 11, 11);
        gridLayout_2->setObjectName(QStringLiteral("gridLayout_2"));
        gridLayout_2->setContentsMargins(0, 0, 0, 0);
        horizontalSpacer_3 = new QSpacerItem(40, 20, QSizePolicy::Fixed, QSizePolicy::Minimum);

        gridLayout_2->addItem(horizontalSpacer_3, 0, 1, 1, 1);

        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Fixed, QSizePolicy::Minimum);

        gridLayout_2->addItem(horizontalSpacer_2, 0, 2, 1, 1);

        horizontalSpacer_4 = new QSpacerItem(40, 20, QSizePolicy::Fixed, QSizePolicy::Minimum);

        gridLayout_2->addItem(horizontalSpacer_4, 0, 0, 1, 1);

        horizontalSpacer_5 = new QSpacerItem(40, 20, QSizePolicy::Fixed, QSizePolicy::Minimum);

        gridLayout_2->addItem(horizontalSpacer_5, 2, 0, 1, 1);

        pushButton_Browse = new QPushButton(gridLayoutWidget_2);
        pushButton_Browse->setObjectName(QStringLiteral("pushButton_Browse"));

        gridLayout_2->addWidget(pushButton_Browse, 1, 0, 1, 1);

        lineEdit = new QLineEdit(gridLayoutWidget_2);
        lineEdit->setObjectName(QStringLiteral("lineEdit"));

        gridLayout_2->addWidget(lineEdit, 1, 1, 1, 1);

        pushButton_Load = new QPushButton(gridLayoutWidget_2);
        pushButton_Load->setObjectName(QStringLiteral("pushButton_Load"));
        QSizePolicy sizePolicy(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(pushButton_Load->sizePolicy().hasHeightForWidth());
        pushButton_Load->setSizePolicy(sizePolicy);

        gridLayout_2->addWidget(pushButton_Load, 1, 2, 1, 1);


        gridLayout->addWidget(groupBox, 3, 1, 1, 1);

        verticalSpacer = new QSpacerItem(20, 90, QSizePolicy::Minimum, QSizePolicy::Fixed);

        gridLayout->addItem(verticalSpacer, 3, 0, 1, 1);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer, 1, 1, 1, 1);

        verticalSpacer_2 = new QSpacerItem(20, 460, QSizePolicy::Minimum, QSizePolicy::Fixed);

        gridLayout->addItem(verticalSpacer_2, 4, 0, 1, 1);

        Camera_loading_gui->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(Camera_loading_gui);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 827, 21));
        Camera_loading_gui->setMenuBar(menuBar);
        mainToolBar = new QToolBar(Camera_loading_gui);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        Camera_loading_gui->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(Camera_loading_gui);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        Camera_loading_gui->setStatusBar(statusBar);

        retranslateUi(Camera_loading_gui);

        QMetaObject::connectSlotsByName(Camera_loading_gui);
    } // setupUi

    void retranslateUi(QMainWindow *Camera_loading_gui)
    {
        Camera_loading_gui->setWindowTitle(QApplication::translate("Camera_loading_gui", "Camera_loading_gui", 0));
        groupBox->setTitle(QApplication::translate("Camera_loading_gui", "Load", 0));
        pushButton_Browse->setText(QApplication::translate("Camera_loading_gui", "Browse", 0));
        pushButton_Load->setText(QApplication::translate("Camera_loading_gui", "Load", 0));
    } // retranslateUi

};

namespace Ui {
    class Camera_loading_gui: public Ui_Camera_loading_gui {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_CAMERA_LOADING_GUI_H
