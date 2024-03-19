# -*- coding: utf-8 -*-
#!/usr/bin/python

from PySide2.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class PasswordDialog(QDialog):
    def __init__(self):
        super(PasswordDialog, self).__init__()
        self.setWindowTitle("Administrator Password Verification")

        self.password_label = QLabel("Enter Administrator Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.confirm_button = QPushButton("Confirm")
        self.cancel_button = QPushButton("Cancel")

        layout = QVBoxLayout()
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.confirm_button)
        layout.addWidget(self.cancel_button)

        self.setLayout(layout)

        self.confirm_button.clicked.connect(self.verify_password)
        self.cancel_button.clicked.connect(self.reject)  # Cerrar el diálogo si se cancela

    def verify_password(self):
        entered_password = self.password_input.text()

        # Lógica para verificar la contraseña del administrador
        correct_password = "iamTHEadmin"  # Contraseña de ejemplo

        if entered_password == correct_password:
            self.accept()  # Aceptar el diálogo si la contraseña es correcta
        else:
            QMessageBox.warning(self, "Error", "Incorrect password. Please try again.")