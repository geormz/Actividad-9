from PySide2.QtWidgets import QMainWindow, QGraphicsScene
from ui_mainwindow import Ui_MainWindow
from PySide2.QtGui import QPen, QColor, QTransform
from PySide2.QtCore import Slot
from random import randint


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Draw_Button.clicked.connect(self.draw)
        self.ui.Clean_Buttom.clicked.connect(self.clean)

        self.scene=QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)


    def wheelEvent(self, event):
        if event.delta() >0:
            self.ui.graphicsView.scale(1.2,1.2)
        else:
            self.ui.graphicsView.scale(0.8,0.8)

    @Slot()
    def draw(self):
        pen=QPen()
        pen.setWidth(2)
        for i in range (3):
            r=randint(0,255)
            g=randint(0,255)
            b=randint(0,255)
            color=QColor(r,g,b)

            
            origen_x=randint(0,500)
            origen_y=randint(0,500)
            destino_x=randint(0,500)
            destino_y=randint(0,500)

            pen.setColor(color)
            self.scene.addEllipse(origen_x,origen_y,3,3,pen)
            self.scene.addEllipse(destino_x,destino_y,3,3,pen)
            self.scene.addLine(origen_x+3, origen_y+3,destino_x,destino_y,pen)


    @Slot()
    def clean(self):
        self.scene.clear()  
