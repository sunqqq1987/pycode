# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\python-code\serial\ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 400)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.comboBox = QtWidgets.QComboBox(self.centralWidget)
        self.comboBox.setGeometry(QtCore.QRect(40, 50, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 50, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 81, 461, 111))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(400, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 50, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralWidget)
        self.comboBox_2.setGeometry(QtCore.QRect(410, 370, 69, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 54, 12))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(120, 30, 54, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(350, 370, 54, 12))
        self.label_3.setObjectName("label_3")
        self.listView = QtWidgets.QListView(self.centralWidget)
        self.listView.setGeometry(QtCore.QRect(20, 200, 321, 192))
        self.listView.setObjectName("listView")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "串口通讯测试（欧姆龙）"))
        self.comboBox.setCurrentText(_translate("MainWindow", "D"))
        self.comboBox.setItemText(0, _translate("MainWindow", "D"))
        self.comboBox.setItemText(1, _translate("MainWindow", "W"))
        self.comboBox.setItemText(2, _translate("MainWindow", "T"))
        self.comboBox.setItemText(3, _translate("MainWindow", "A"))
        self.comboBox.setItemText(4, _translate("MainWindow", "C"))
        self.comboBox.setItemText(5, _translate("MainWindow", "H"))
        self.pushButton.setText(_translate("MainWindow", "读取"))
        self.pushButton_2.setText(_translate("MainWindow", "退出"))
        self.label.setText(_translate("MainWindow", "继电器"))
        self.label_2.setText(_translate("MainWindow", "地址"))
        self.label_3.setText(_translate("MainWindow", "串口号"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

