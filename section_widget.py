# -*- coding: utf-8 -*-
#!/usr/bin/python

import sys
from PySide2.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QStackedLayout,
    QWidget, QTabWidget, QPushButton, QListWidget, QListWidgetItem,
    QLabel, QFrame
)
from PySide2.QtCore import (
    QSize, Qt, QObject, Signal
)

class SectionWidget(QWidget):
    buttonClicked = Signal(str)  # Definir la señal buttonClicked como una señal que emite un texto

    def __init__(self, title, parent=None):
        super(SectionWidget, self).__init__(parent)
        layout = QVBoxLayout()

        # Titulo de seccion
        titleLabel = QLabel(title)
        titleLabel.setAlignment(Qt.AlignCenter)
        titleLabel.setMinimumSize(200,30)
        titleLabel.setMaximumSize(200,30)
        layout.addWidget(titleLabel)

        # Linea horizontal debajo del titulo
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        layout.addWidget(line)

        self.setLayout(layout)

    
    def addButton(self, buttonText, buttonFunction):
        button = QPushButton(buttonText)
        # button.clicked.connect(lambda: buttonFunction()) # Ejecuta el print provisional
        button.clicked.connect(lambda: self.emitButtonClicked(buttonText))
        self.layout().addWidget(button)

    def emitButtonClicked(self, buttonText):
        # Emitir la señal y mostrar un mensaje de depuración
        self.buttonClicked.emit(buttonText)
        print("Button clicked:", buttonText)