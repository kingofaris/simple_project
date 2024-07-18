from src.plugin_interface import PluginInterface
from PyQt6.QtWidgets import QWidget
from .ui_main import Ui_Form
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QImage, QPixmap
import cv2
import  sys

class Controller(QWidget):
    def __init__(self, model):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.model = model
        self.set_stylesheet()
        self.vrb_initiation()
        self.connect_signal()

    def connect_signal(self):
        self.ui.pushButton_strm.clicked.connect(self.chose_divice)

    def vrb_initiation(self):
        self.cap = None
        self.camera_start = False
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)

    def set_stylesheet(self):
        #frame
        self.ui.frame.setStyleSheet(self.model.style_frame_main())
        self.ui.frame_2.setStyleSheet(self.model.style_frame_object())
        self.ui.frame_3.setStyleSheet(self.model.style_frame_object())

        #pushbutton
        self.ui.pushButton_strm.setStyleSheet(self.model.style_pushbutton())
        self.ui.pushButton_pause.setStyleSheet(self.model.style_pushbutton())
        self.ui.pushButton_stop.setStyleSheet(self.model.style_pushbutton())
        self.ui.pushButton_clear.setStyleSheet(self.model.style_pushbutton())

        #label
        self.ui.label.setStyleSheet(self.model.style_label())
        # self.ui.label_2.setStyleSheet(self.model.style_label())

    def chose_divice(self):
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            print("Your camera can't open yet")
        else:
            print("your camera succesfuly opened")
        self.timer.start(10)
        self.camera_start = True

    def update_frame(self):
        if self.cap is not None and self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret :
                h, w, ch = frame.shape
                btyes_per_line = ch * w
                img_stream = QImage(frame.data, w, h, btyes_per_line, QImage.Format.Format_BGR888)
                video = QPixmap.fromImage(img_stream)


                self.ui.label.setPixmap(video)
                self.ui.label.setScaledContents(True)




class Streaming_only(PluginInterface):
    def __init__(self):
        super().__init__()
        self.widget = None
        self.description = "This is a plugins application"

    def set_plugin_widget(self, model):
        self.widget = Controller(model)
        return self.widget

    def set_icon_apps(self):
        return "icon.png"

    def change_stylesheet(self):
        self.widget.set_stylesheet()

