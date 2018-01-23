# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication
from Ui_register import Ui_MainWindow
import sys
from reg import Md5calc

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
        macshow2=Md5calc()#类需要初始化
        self.lineEdit.setText(macshow2.macshow())
        self.lineEdit_2.setText(macshow2.id_calc())
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        macshow2=Md5calc()#类需要初始化
        #print(macshow2.id_calc())
        self.lineEdit_3.setText(macshow2.sn_calc())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())        
    
