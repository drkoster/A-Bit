import sys
import __version__
import subprocess

from subprocess import Popen, PIPE

from PyQt5.QtCore import QSize, QMetaObject,QCoreApplication, QRect
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QPlainTextEdit, QMainWindow


#   ui.py
#   Author: Dennis Koster
#   Ui implementation for A-Bit create with qt-designer
#
#   To run: python .\ui.py 

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Abit_Dialog()
        self.ui.setupUi(self)

class Abit_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1100, 441)
        self.button_create = QPushButton(Dialog)
        self.button_create.setObjectName(u"button_create")
        self.button_create.setGeometry(QRect(60, 360, 121, 31))
        self.label_version = QLabel(Dialog)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setGeometry(QRect(20, 10, 131, 16))
        self.label_source = QLabel(Dialog)
        self.label_source.setObjectName(u"label_source")
        self.label_source.setGeometry(QRect(20, 30, 47, 14))
        self.label_target = QLabel(Dialog)
        self.label_target.setObjectName(u"label_target")
        self.label_target.setGeometry(QRect(20, 100, 47, 14))
        self.lineEdit_target = QLineEdit(Dialog)
        self.lineEdit_target.setObjectName(u"lineEdit_target")
        self.lineEdit_target.setGeometry(QRect(20, 120, 371, 20))
        self.lineEdit_source = QLineEdit(Dialog)
        self.lineEdit_source.setObjectName(u"lineEdit_source")
        self.lineEdit_source.setGeometry(QRect(20, 50, 371, 20))
        self.button_verify = QPushButton(Dialog)
        self.button_verify.setObjectName(u"button_verify")
        self.button_verify.setGeometry(QRect(220, 360, 121, 31))
        self.plainResult = QPlainTextEdit(Dialog)
        self.plainResult.setObjectName(u"plainResult")
        self.plainResult.setGeometry(QRect(460, 50, 631, 381))
        self.plainResult.setAcceptDrops(False)
        self.label_status = QLabel(Dialog)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setGeometry(QRect(460, 30, 47, 14))
        self.retranslateUi(Dialog)

        self.button_create.clicked.connect(self.createButtonHandler)

        QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"A-Bit", None))
        self.button_create.setText(QCoreApplication.translate("Dialog", u"Create", None))
        self.label_version.setText(QCoreApplication.translate("Dialog", u"Version: "+__version__.__version__, None))
        self.label_source.setText(QCoreApplication.translate("Dialog", u"Source:", None))
        self.label_target.setText(QCoreApplication.translate("Dialog", u"Target:", None))
        self.lineEdit_target.setPlaceholderText(QCoreApplication.translate("Dialog", u"Select directory or hash file", None))
        self.lineEdit_source.setPlaceholderText(QCoreApplication.translate("Dialog", u"Source directory to create or verify hashes for", None))
        self.button_verify.setText(QCoreApplication.translate("Dialog", u"Verify", None))
        self.label_status.setText(QCoreApplication.translate("Dialog", u"Status", None))

    def createButtonHandler(self):
        p = subprocess.Popen(["python", "Abit.py", "-h"], stdout=PIPE, bufsize=1)
        #p = Popen(["python Abit.py", "-h"], stdout=PIPE, bufsize=1)
        with p.stdout:
            for line in iter(p.stdout.readline, b''):
                print(line)
                self.plainResult.appendPlainText(line.decode("utf-8"))
        p.wait() # wait for the subprocess to exit


def main():
    abitApp = QApplication([])
    abitWindow = MainWindow()
    abitWindow.show()
    
    
    sys.exit(abitApp.exec())


if __name__ == "__main__":
    main()