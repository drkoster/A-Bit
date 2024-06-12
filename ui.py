import sys

from PyQt5.QtCore import QSize, QMetaObject,QCoreApplication, QRect
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QPlainTextEdit, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Abit_Dialog()
        self.ui.setupUi(self)

class Abit_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(922, 515)
        self.button_create = QPushButton(Dialog)
        self.button_create.setObjectName(u"button_create")
        self.button_create.setGeometry(QRect(60, 360, 121, 31))
        self.label_version = QLabel(Dialog)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setGeometry(QRect(10, 490, 47, 14))
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
        self.plainTextEdit = QPlainTextEdit(Dialog)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(460, 50, 441, 381))
        self.plainTextEdit.setAcceptDrops(False)
        self.label_status = QLabel(Dialog)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setGeometry(QRect(460, 30, 47, 14))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"A-Bit", None))
        self.button_create.setText(QCoreApplication.translate("Dialog", u"Create", None))
        self.label_version.setText(QCoreApplication.translate("Dialog", u"Version: ", None))
        self.label_source.setText(QCoreApplication.translate("Dialog", u"Source:", None))
        self.label_target.setText(QCoreApplication.translate("Dialog", u"Target:", None))
        self.lineEdit_target.setPlaceholderText(QCoreApplication.translate("Dialog", u"Select directory or hash file", None))
        self.lineEdit_source.setPlaceholderText(QCoreApplication.translate("Dialog", u"Source directory to create or verify hashes for", None))
        self.button_verify.setText(QCoreApplication.translate("Dialog", u"Verify", None))
        self.label_status.setText(QCoreApplication.translate("Dialog", u"Status", None))
    # retranslateUi

def main():
    abitApp = QApplication([])
    abitWindow = MainWindow()
    abitWindow.show()
    
    
    sys.exit(abitApp.exec())

if __name__ == "__main__":
    main()