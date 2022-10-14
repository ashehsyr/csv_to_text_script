import sys
import csv_to_txt_for_app

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
from PyQt5.uic import loadUi

from main_gui import Ui_Form

class Window(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        #self.connectSignalsSlots()
    
        

    def connectSignalsSlots(self):
        self.action_Exit.triggered.connect(self.close)

    def findAndReplace(self):
        dialog = FindReplaceDialog(self)
        dialog.exec()

    def run(self):
        csv_to_txt_for_app.convert_file(str(self.input_field.text()), str(self.output_field.text()))

class FindReplaceDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ui/find_replace.ui", self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())