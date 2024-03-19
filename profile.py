# -*- coding: utf-8 -*-
#!/usr/bin/python

import sys
from PySide2.QtWidgets import (
    QLineEdit, QWidget, QPushButton, QLabel, QVBoxLayout,
    QMessageBox, QApplication
)
from PySide2.QtCore import (
    Qt
)

class ProfileWindow(QWidget):
    def __init__(self, user):
        super(ProfileWindow, self).__init__()
        self.setWindowTitle("Profile")
        self.setGeometry(100,100,400,200)

        # Acceder a los datos de user registrado
        self.username_label = QLabel("User: " + user.name)
        self.email_input = QLineEdit()
        self.save_btn = QPushButton("Save changes")

        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(QLabel("Email"))
        layout.addWidget(self.email_input)
        layout.addWidget(self.save_btn)

        self.setLayout(layout)

        self.save_btn.clicked.connect(self.save_profile_changes)

    def save_profile_changes(self):
        new_email = self.email_input.text()
        # Guardar cambios en BBDD
        QMessageBox.information(self, "Profile","Succesfuly save changes")