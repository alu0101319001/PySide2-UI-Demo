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

class SessionManager:
    def __init__(self):
        self.logged_in_user = None

    def login_user(self, user):
        self.logged_in_user = user

    def logout_user(self):
        self.logged_in_user = None

    def is_user_logged_in(self):
        return self.logged_in_user is not None