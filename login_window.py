# -*- coding: utf-8 -*-
#!/usr/bin/python

from PySide2.QtWidgets import QDialog, QLabel, QLineEdit, QComboBox, QPushButton, QVBoxLayout
from PySide2.QtCore import Signal, QDateTime

class LoginWindow(QDialog):
    open_register = Signal()
    login_successful = Signal()

    def __init__(self, db_manager):
        super(LoginWindow, self).__init__()
        self.db_manager = db_manager
        self.setWindowTitle("Login")

        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton("Login")
        self.register_button = QPushButton("Register")

        
        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.register_button)

        self.setLayout(layout)

        self.login_button.clicked.connect(self.authenticate_user)
        self.register_button.clicked.connect(self.open_register_window)

    def authenticate_user(self):
        username = self.username_input.text()
        password = self.password_input.text()

        user_data = self.db_manager.get_user_by_id_or_username(None, username)
        if password == user_data["password"]:
            self.hide() # Cerrar ventana de inicio de sesión
            self.login_successful.emit() # Abrir MainWindow

            # Actualizar last_login_timestamp
            current_datetime = QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss")
            self.db_manager.update_user_null(user_data["id"], None, current_datetime)
            return

    def open_register_window(self):
        self.hide()
        self.open_register.emit()