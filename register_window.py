# -*- coding: utf-8 -*-
#!/usr/bin/python

from PySide2.QtWidgets import QDialog,QMessageBox,QLabel, QLineEdit, QComboBox, QPushButton, QVBoxLayout
from PySide2.QtSql import QSqlQuery
from PySide2.QtCore import Signal
from password_dialog import PasswordDialog

class RegisterWindow(QDialog):
    registration_completed = Signal()

    def __init__(self, db_manager):
        super(RegisterWindow, self).__init__()
        self.db_manager = db_manager
        self.setWindowTitle("Register")

        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.role_label = QLabel("Role:")
        self.role_input = QComboBox()
        self.role_input.addItem("Administrator")
        self.role_input.addItem("Professor")
        self.role_input.addItem("Student")
        self.register_button = QPushButton("Register")

        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.role_label)
        layout.addWidget(self.role_input)
        layout.addWidget(self.register_button)

        self.setLayout(layout)

        self.register_button.clicked.connect(self.register_user)

    def register_user(self):
        username = self.username_input.text()
        password = self.password_input.text()
        role = self.role_input.currentText()

        if role == "Administrator":
            role = "admin"
        elif role == "Professor":
            role = "professor"
        elif role == "Student":
            role = "student"
        else:
            role = None

        if role == "admin":
            password_dialog = PasswordDialog()
            if password_dialog.exec_() == QDialog.Accepted:
                # Continuar con registro
                success = self.db_manager.create_new_user(username, password, role)
                if success: 
                    print("User registered successfully.")
                    self.hide()
                    self.registration_completed.emit()
                    return True
                else:
                    print("Error registering user")
                    QMessageBox.critical(self, "Error in register", "A error in query")
                    return False
            else:
                QMessageBox.warning(self, "Error in register", "Incorrect password for admin.")
                return
        else:
            success = self.db_manager.create_new_user(username, password, role)
            if success: 
                print("User registered successfully.")
                self.hide()
                self.registration_completed.emit()
                return True
            else:
                print("Error registering user")
                QMessageBox.critical(self, "Error in register", "A error in query")
                return False

        