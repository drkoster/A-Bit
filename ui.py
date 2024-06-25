import sys
import __version__
import subprocess
import os

from subprocess import Popen, PIPE
from datetime import datetime

from PyQt5.QtCore import QSize, QMetaObject,QCoreApplication, QRect
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QPlainTextEdit, QMainWindow, QMessageBox, QFileDialog


#   ui.py
#   Author: Dennis Koster
#   Ui implementation for A-Bit create with qt-designer
#   Its an argument wrapper for the Abit.py application showing output and results in a textDialog
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
        Dialog.resize(1298, 539)
        self.button_create = QPushButton(Dialog)
        self.button_create.setObjectName(u"button_create")
        self.button_create.setGeometry(QRect(80, 480, 141, 31))
        self.label_version = QLabel(Dialog)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setGeometry(QRect(20, 10, 131, 16))
        self.label_source = QLabel(Dialog)
        self.label_source.setObjectName(u"label_source")
        self.label_source.setGeometry(QRect(20, 50, 47, 14))
        self.label_target = QLabel(Dialog)
        self.label_target.setObjectName(u"label_target")
        self.label_target.setGeometry(QRect(20, 170, 47, 14))
        self.lineEdit_target = QLineEdit(Dialog)
        self.lineEdit_target.setObjectName(u"lineEdit_target")
        self.lineEdit_target.setGeometry(QRect(20, 190, 491, 20))
        self.lineEdit_source = QLineEdit(Dialog)
        self.lineEdit_source.setObjectName(u"lineEdit_source")
        self.lineEdit_source.setGeometry(QRect(20, 70, 491, 20))
        self.button_verify = QPushButton(Dialog)
        self.button_verify.setObjectName(u"button_verify")
        self.button_verify.setGeometry(QRect(280, 480, 141, 31))
        self.plainResult = QPlainTextEdit(Dialog)
        self.plainResult.setObjectName(u"plainResult")
        self.plainResult.setGeometry(QRect(550, 50, 721, 461))
        self.plainResult.setAcceptDrops(False)
        self.label_status = QLabel(Dialog)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setGeometry(QRect(550, 30, 47, 14))
        self.button_source_select = QPushButton(Dialog)
        self.button_source_select.setObjectName(u"button_source_select")
        self.button_source_select.setGeometry(QRect(20, 100, 141, 31))
        self.button_select_target_dir = QPushButton(Dialog)
        self.button_select_target_dir.setObjectName(u"button_select_target_dir")
        self.button_select_target_dir.setGeometry(QRect(20, 220, 141, 31))
        self.button_select_target_file = QPushButton(Dialog)
        self.button_select_target_file.setObjectName(u"button_select_target_file")
        self.button_select_target_file.setGeometry(QRect(180, 220, 151, 31))
        self.retranslateUi(Dialog)

        self.button_create.clicked.connect(self.createButtonHandler)
        self.button_verify.clicked.connect(self.verifyButtonHandler)
        self.button_select_target_dir.clicked.connect(self.selectTargetDirHandler)
        self.button_select_target_file.clicked.connect(self.selectTargetFileHandler)
        self.button_source_select.clicked.connect(self.selectSourceDirHandler)

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
        self.button_verify.setEnabled(False)
        self.label_status.setText(QCoreApplication.translate("Dialog", u"Status", None))
        self.button_source_select.setText(QCoreApplication.translate("Dialog", u"Select Directory", None))
        self.button_select_target_dir.setText(QCoreApplication.translate("Dialog", u"Select Directory", None))
        self.button_select_target_file.setText(QCoreApplication.translate("Dialog", u"Select hash file", None))


    def createButtonHandler(self):
        if (os.path.isdir(self.lineEdit_target.text())):
            if(self.lineEdit_target.text()[-1] != "/"):
                self.lineEdit_target.setText(self.lineEdit_target.text()+"/")
            now = datetime.now()
            date_name = now.strftime("%d-%m-%Y_%H:%M:%S")
            date_name = date_name+".md5"
            self.lineEdit_target.setText(self.lineEdit_target.text()+date_name)
            
        self.buildCreateArguments()

    def verifyButtonHandler(self):
        self.buildVerifyArguments()

    def selectSourceDirHandler(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.Directory)
        file_dialog.setAcceptMode(QFileDialog.AcceptOpen)

        selected_dir = QFileDialog.getExistingDirectory()
        self.lineEdit_source.setText(selected_dir)

    # Enable verification button on succes
    def selectTargetDirHandler(self):
        selected_dir = QFileDialog.getExistingDirectory()
        if (os.path.exists(selected_dir)):
            self.lineEdit_target.setText(selected_dir)
            self.button_verify.setEnabled(True)

    # Enable verification button on succes
    def selectTargetFileHandler(self):
        selected_file, _filter = QFileDialog.getOpenFileName()
        if (os.path.exists(selected_file)):
            self.lineEdit_target.setText(selected_file)
            self.button_verify.setEnabled(True)


    # first build arguments list, then call subprocess
    def startAbit(self, arguments):
        p = subprocess.Popen(arguments, stdout=PIPE, bufsize=10)
        with p.stdout:
            for line in iter(p.stdout.readline, b''):
                print(line)
                self.plainResult.appendPlainText(line.decode("utf-8"))
        p.wait()


    # Creates arguments list to call Abit.py for creating hash file
    def buildCreateArguments(self):
        arguments = "python Abit.py --create"
        source = self.lineEdit_source.text()
        if source == "":
            self.showWarningDialog("Please select source directory")
            return
        
        arguments = arguments+(" --starting_dir "+source)

        target = self.lineEdit_target.text()
        if target == "":
            self.showWarningDialog("Please specify target file to save\n created hashes in.")
            return

        arguments=arguments+(" --output "+target)
        print(arguments)
        self.startAbit(arguments)


    # Creates arguments list to call Abit.py for verification
    def buildVerifyArguments(self):
        arguments = ["python", "Abit.py", "--verify"]
        source = self.lineEdit_source.text()
        if source == "":
            self.showWarningDialog("Please select source directory")
            return
        
        arguments = arguments+(" --starting_dir "+source)

        target = self.lineEdit_target.text()
        if target == "":
            self.showWarningDialog("Please specify target file or directory")
            return

        arguments=arguments+(" --input "+target)
        self.startAbit(arguments)


    def showWarningDialog(self, message):
        warningDialog = QMessageBox()
        warningDialog.setWindowTitle("Warning")
        warningDialog.setText(message)
        warningDialog.setIcon(QMessageBox.Icon.Warning)
        warningDialog.exec()

def main():
    abitApp = QApplication([])
    abitWindow = MainWindow()
    abitWindow.show()    
    sys.exit(abitApp.exec())

if __name__ == "__main__":
    main()