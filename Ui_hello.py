# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\python-code\hello.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(558, 423)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/sunqq/Desktop/88_1089442_6f0f53b1f2d201a.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(True)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 50, 54, 12))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(450, 90, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 130, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(260, 50, 54, 12))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(120, 50, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(330, 50, 54, 12))
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(450, 170, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(450, 210, 75, 23))
        self.pushButton_4.setAutoRepeat(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(450, 320, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(50, 130, 191, 231))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.toolButton = QtWidgets.QToolButton(Dialog)
        self.toolButton.setGeometry(QtCore.QRect(450, 360, 37, 18))
        self.toolButton.setObjectName("toolButton")

        self.retranslateUi(Dialog)
        self.pushButton_4.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "hello测试窗体"))
        self.label.setText(_translate("Dialog", "测试文字"))
        self.pushButton.setText(_translate("Dialog", "读数"))
        self.pushButton_2.setText(_translate("Dialog", "去皮"))
        self.label_2.setText(_translate("Dialog", "TextLabel"))
        self.label_3.setText(_translate("Dialog", "TextLabel"))
        self.pushButton_3.setText(_translate("Dialog", "另存"))
        self.pushButton_4.setText(_translate("Dialog", "退出"))
        self.toolButton.setText(_translate("Dialog", "..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

