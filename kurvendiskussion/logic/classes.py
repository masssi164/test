from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextOption
from stringparser import termToFloatValues
from PyQt5.QtWidgets import QApplication, QFormLayout, QLineEdit, QTextBrowser, QTextEdit, QVBoxLayout, QWidget
from pprint import pprint


class Structur():
    nullstellen:list
    extrema:list
    function:list
    
    def __init__(self,term) -> None:


class Gui(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kurvendiskussion")
        self.inp =QLineEdit()
        self.inp.returnPressed.connect(self.kurvendiskussion)
        self.document =QTextEdit()
        self.old =self.document.textInteractionFlags()
        self.document.setReadOnly(True)
        self.new =self.document.textInteractionFlags()
        self.document.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByKeyboard)

        self.buildLayout()

        
    def buildLayout(self):
        layout =QVBoxLayout()
        form =QFormLayout()
        form.addRow("&Termeingabe:",self.inp)
        layout.addLayout(form)
        form_2 =QFormLayout()
        form_2.addRow("&Ausgabe:",self.document)
        layout.addLayout(form_2)
        self.setLayout(layout)
        

    
if __name__ == '__main__':
    def guiMain():
        app =QApplication(sys.argv)
        gui =Gui()
        gui.document.setWordWrapMode(QTextOption.WrapMode.NoWrap)
        gui.show()
        print("old:",gui.old)
        print("new:",gui.new)
        app.exec_()
    
    def testMain():
        print("main")
        
    testMain()
    #guiMain()
