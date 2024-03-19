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

class AuthenticationWindow(QWidget):
    def __init__(self):
        super(AuthenticationWindow, self).__init__()
        self.setWindowTitle("Authenticate")
        self.setGeometry(100,100,400,200)

        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.login_btn = QPushButton("Login")
        self.register_btn = QPushButton("Register")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("User:"))
        layout.addWidget(self.username_input)
        layout.addWidget(QLabel("Password:"))
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_btn)
        layout.addWidget(self.register_btn)

        self.setLayout(layout)

        self.login_btn.clicked.connect(self.login)
        self.register_btn.clicked.connect(self.register)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Verificar credenciales en BBDD
        if username == "user" and password == "pass":
            QMessageBox.information(self, "Login", "Successful login!!")
            # Abrir aqui app principal
        else:
            QMessageBox.warning(self, "Error", "Incorrect credentials.")

    def register(self):
        # Lógica para registrar nuevos usuarios a la BBDD
        QMessageBox.information(self, "Register","Successful register!!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AuthenticationWindow()
    window.show()
    sys.exit(app.exec_())