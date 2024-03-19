# -*- coding: utf-8 -*-
#!/usr/bin/python

import sys
from section_widget import SectionWidget
from PySide2.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QStackedLayout,
    QWidget, QTabWidget, QPushButton, QListWidget, QListWidgetItem,
    QScrollArea
)
from PySide2.QtCore import (
    QSize
)

class SidebarWidget(QWidget):
    def __init__(self):
        super(SidebarWidget, self).__init__()
        layout = QVBoxLayout(self)
        
        # ScrollArea para manejar muchas secciones
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        layout.addWidget(self.scrollArea)
        
        # Contenedor para las secciones dentro del ScrollArea
        self.sectionsContainer = QWidget()
        self.sectionsLayout = QVBoxLayout()
        self.sectionsContainer.setLayout(self.sectionsLayout)
        
        self.scrollArea.setWidget(self.sectionsContainer)

        # Lista para mantener un seguimiento de las secciones
        self.sections = []
        
    def addSection(self, section):
        self.sections.append(section)
        self.sectionsLayout.addWidget(section)

    def printButtonName(self, buttonText):
        print(buttonText)

    def executeScript1(self):
        print("Ejecutando Script 1")

    def openDialog2(self):
        print("Abriendo dialogo 2")

if __name__ == "__main__":
    app = QApplication([])
    
    sidebar = SidebarWidget()

    # Crear y añadir la primera sección
    section1 = SectionWidget("Sección 1")
    section1.addButton("Botón 1.1", sidebar.printButtonName("Button 1.1"))
    section1.addButton("Botón 1.2", sidebar.printButtonName("Button 1.2"))
    sidebar.addSection(section1)

    # Crear y añadir la segunda sección
    section2 = SectionWidget("Sección 2")
    section2.addButton("Botón 2.1", sidebar.printButtonName("Button 2.1"))
    section2.addButton("Botón 2.2", sidebar.printButtonName("Button 2.1"))
    sidebar.addSection(section2)

    mainWindow = QMainWindow()
    mainWindow.setCentralWidget(sidebar)
    mainWindow.resize(200, 400)
    mainWindow.show()

    sys.exit(app.exec_())