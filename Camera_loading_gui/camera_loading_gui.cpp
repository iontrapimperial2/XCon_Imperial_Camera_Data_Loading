#include "camera_loading_gui.h"
#include "ui_camera_loading_gui.h"

Camera_loading_gui::Camera_loading_gui(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::Camera_loading_gui)
{
    ui->setupUi(this);
}

Camera_loading_gui::~Camera_loading_gui()
{
    delete ui;
}
