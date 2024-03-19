import sys
from PySide2.QtWidgets import (
    QApplication, QDialog, QLineEdit, QPushButton, QVBoxLayout
)

class CommandDialog(QDialog):
    def __init__(self, parent=None):
        super(CommandDialog, self).__init__(parent)
        self.setWindowTitle("Introduce the Command")

        self.layout = QVBoxLayout(self)

        # QLineEdit configuration
        self.edit = QLineEdit(self)
        self.edit.setPlaceholderText("Write the command here...")
        self.layout.addWidget(self.edit)

        # Accept button
        self.btn_accept = QPushButton("Accept", self)
        self.btn_accept.clicked.connect(self.accept)
        self.layout.addWidget(self.btn_accept)

        # Cancel button
        self.btn_cancel = QPushButton("Cancel", self)
        self.btn_cancel.clicked.connect(self.reject)
        self.layout.addWidget(self.btn_cancel)

    def accept(self):
        self.command = self.edit.text()
        super(CommandDialog, self).accept()

    def getCommand(self):
        return self.command


def showCommandDialog(accept_text, cancel_text):
    dialog = CommandDialog()
    if dialog.exec_():
        command = dialog.getCommand()
        print(accept_text, command)
    else:
        print(cancel_text)


