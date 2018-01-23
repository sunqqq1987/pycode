# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QApplication

from Ui_hello import Ui_Dialog
class Dialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.label.setText('hello')
        #raise NotImplementedError      

    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.label.setText('gogogo')
        #raise NotImplementedError
  
    
    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_pushButton_4_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
    
    @pyqtSlot()
    def on_toolButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
if __name__ == "__main__":
        app = QApplication(sys.argv)
        dlg =Dialog()
        dlg.show()
        sys.exit(app.exec_())     
