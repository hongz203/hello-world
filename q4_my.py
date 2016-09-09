import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic

class MyDlg:
    def __init__(self):
        self.ui = uic.loadUi("c.ui") # xml -> 객체화
        self.ui.pushButton.clicked.connect( self.btn_click )
        self.ui.show()        
    def btn_click(self):
        num1 = self.ui.lineEdit.text()
        num2 = self.ui.lineEdit_2.text()
        result = int(num1) + int(num2)
        result = "합은: %d" % result
        self.ui.lineEdit_3.setText(result)
        
        
def main():
    app = QApplication(sys.argv)
    dlg = MyDlg()
    app.exec()      #loop queue memory...
    
if __name__ == '__main__':
    main()
    
