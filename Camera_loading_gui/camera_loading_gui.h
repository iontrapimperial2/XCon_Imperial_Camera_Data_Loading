#ifndef CAMERA_LOADING_GUI_H
#define CAMERA_LOADING_GUI_H

#include <QMainWindow>

namespace Ui {
class Camera_loading_gui;
}

class Camera_loading_gui : public QMainWindow
{
    Q_OBJECT

public:
    explicit Camera_loading_gui(QWidget *parent = nullptr);
    ~Camera_loading_gui();

private:
    Ui::Camera_loading_gui *ui;
};

#endif // CAMERA_LOADING_GUI_H
