import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget,QVBoxLayout,QTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'CryptoPad'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200
        self.setWindowTitle(self.title)
        self.statusBar().showMessage('Welcome to CryptoPad')
        
        
        #open a new file
        openAct = QAction(QIcon('food.png'), '&open', self)        
        openAct.setShortcut('Ctrl+O')
        openAct.setStatusTip('open a new file')
        
        #save a new file
        saveact=QAction(QIcon("save.png"),"&save",self)
        saveact.setShortcut('Ctrl+s')
        saveact.setStatusTip("save your file")

        #encrypt your file
        encryptact=QAction(QIcon("encrypt.png"),"&encrypt",self)
        encryptact.setShortcut('Ctrl+e')
        encryptact.setStatusTip("encrypt your file")

        #decrypt your file
        decryptact=QAction(QIcon("decrypt.png"),"&decrypt",self)
        decryptact.setShortcut('Ctrl+d')
        decryptact.setStatusTip("decrypt your file")
          
        #delete your file
        deleteact=QAction(QIcon("delete.png"),'&delete',self)
        deleteact.setShortcut("Ctrl+d")
        deleteact.setStatusTip("delete your file")  
        
        #close your file
        closeact=QAction(QIcon('close.png'),"&close",self)
        closeact.setShortcut('Ctrl+c')
        closeact.setStatusTip('close your file')
        closeact.triggered.connect(self.close)


        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        saveMenu=menubar.addMenu('&save')
        encryptMenu=menubar.addMenu('&encrypt')
        deleteMenu=menubar.addMenu('&delete')
        closemenu=menubar.addMenu('&close')
        decryptmenu=menubar.addMenu('&decrypt')

        fileMenu.addAction(openAct)
        saveMenu.addAction(saveact)
        encryptMenu.addAction(encryptact)
        deleteMenu.addAction(deleteact)
        closemenu.addAction(closeact)
        decryptmenu.addAction(decryptact)
        
        #textfield
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
    
    def encrypt(self, parameter_list):
        pass

    def decrypt(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
