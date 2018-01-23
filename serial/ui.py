# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import sys
import serial
import PyQt5
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication
from Ui_ui import Ui_MainWindow
class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot(str)
    def on_comboBox_activated(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        # TODO: not implemented yet
        #raise NotImplementedError
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        #print('hello world')
        self.Calc()
        #测试输出
    @pyqtSlot(int)
    def on_comboBox_2_activated(self, index):
        """
        Slot documentation goes here.
        
        @param index DESCRIPTION
        @type int
        """
        #TODO: not implemented yet
        #raise NotImplementedError
    def Calc(self):
        price=int(self.lineEdit.text())
        str1=str(price*2)
        self.lineEdit.setText(str1)
        self.textBrowser.setText(str1)
        listItem=['qwe', 'rty', 'tyu']
        #self.listView.append('123')
        #listView.append(listItem[2])
        #self.listView.appendRow('234')
        print('help', str1)
        print(listItem)
        #print(help(print))
        #self.label.setText(str1)
        #self.results_window.setText(total_price_string)   
     
if __name__ == "__main__":
        app = QApplication(sys.argv)
        dlg =MainWindow()
        dlg.show()
        sys.exit(app.exec_()) 
