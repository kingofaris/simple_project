# Form implementation generated from reading ui file 'ui_widget.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(742, 775)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(parent=Form)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(parent=self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.frame_2)
        self.label.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(parent=self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_strm = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButton_strm.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_strm.setObjectName("pushButton_strm")
        self.verticalLayout_2.addWidget(self.pushButton_strm)
        self.pushButton_pause = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButton_pause.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_pause.setObjectName("pushButton_pause")
        self.verticalLayout_2.addWidget(self.pushButton_pause)
        self.pushButton_stop = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButton_stop.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.verticalLayout_2.addWidget(self.pushButton_stop)
        self.pushButton_clear = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButton_clear.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.verticalLayout_2.addWidget(self.pushButton_clear)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.frame_3)
        self.horizontalLayout_2.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_strm.setText(_translate("Form", "Streaming"))
        self.pushButton_pause.setText(_translate("Form", "Pause"))
        self.pushButton_stop.setText(_translate("Form", "Stop"))
        self.pushButton_clear.setText(_translate("Form", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
