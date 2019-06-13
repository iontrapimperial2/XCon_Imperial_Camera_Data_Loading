#include "camera_loading_gui.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    Camera_loading_gui w;
    w.show();

    return a.exec();
}
