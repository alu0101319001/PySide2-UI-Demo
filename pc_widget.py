# -*- coding: utf-8 -*-
#!/usr/bin/python

import sys
import os
from read_pc_json import check_all_ip, get_pc_list
from icons_check import check_icons_folder
from options_menu import ExamModeON, PowerOnMenu, PowerOffMenu, WaitingMenu, BaseMenu

from PySide2.QtWidgets import (
    QAction, QMenu, QPushButton, QLabel, QWidget,
    QVBoxLayout,QMessageBox, QApplication,
)
from PySide2.QtGui import (
    QMouseEvent,
    QPixmap,QFont
)
from PySide2.QtCore import (
    QResource, Qt, QPoint
)



# En el fichero donde se debería crear todos los PC necesarios, 
# haciendo uso de esta unidad de widget, se debería ejecutar el script
# donde se recoge la información de cada PC. De esta forma, para la creación
# de cada widgetPC se le es pasado la información de uno de estos, siguiendo 
# un patrón o estructura estilo JSON. De ahí se extraería la información
# necesaria para construir el widget. 

# También, de alguna forma, se debería poder acceder al widget si el ordenador
# cambia de estado y cambiar el icono y, quizás, sus opciones disponibles. 
# ESTADOS ACTUALES: 
#    0 - Apagado
#    1 - Waiting
#    2 - Encendido
#    3 - Exam Mode

# Constante de los estados
ON = 2
OFF = 0
WT = 1
EX = 3

class PcWidget(QWidget):
    def __init__(self, pc_extract, state_changed_callback=None,parent=None):
        super(PcWidget, self).__init__(parent)

        # Por ahora se entenderá al pc_extract en formato de diccionario
        # Seguramente se tendería que realizar una función externa de transformación de JSON a diccionario
        # Pongamos por ahora que el diccionario posee las claves: name, state, ip
        self.pc_name = pc_extract["name"]
        self.pc_state = pc_extract["state"]
        self.pc_ip = pc_extract["ip"] 
        self.pc_data = pc_extract 
        self.state_changed_callback = state_changed_callback


        layout = QVBoxLayout()

        # Se tendría que extraer su estado actual, por ahora de defecto se deja el off
        self.computer_icon = QLabel()
        icon_path = self.current_state()
        if icon_path:
            self.computer_icon.setPixmap(QPixmap(icon_path).scaledToWidth(50))
        else:
            print("Icon path not found.")
        layout.addWidget(self.computer_icon)

        # Se tendría que extraer el nombre, ahora tendrá uno por defecto
        computer_name = QLabel(self.pc_name)
        computer_name.setFont(QFont("Arial",10))
        layout.addWidget(computer_name)

        self.setLayout(layout)


    def current_state(self):
        icons_folder = check_icons_folder()
        if icons_folder:
            if self.pc_state == 0:
                icon_path = os.path.join(icons_folder, "computer-off.png")
            elif self.pc_state == 2:
                icon_path = os.path.join(icons_folder, "computer-network.png")
            elif self.pc_state == 1:
                icon_path = os.path.join(icons_folder, "computer.png")
            elif self.pc_state == 3:
                icon_path = os.path.join(icons_folder, "computer--pencil.png")
            else:
                icon_path = os.path.join(icons_folder, "cross.png")
            return icon_path
        else:
            return None
        
    def set_state_changed_callback(self, callback):
        self.state_changed_callback = callback
        
    def updateState(self, new_state):
        self.pc_state = new_state
        self.updateIcon()
        if self.state_changed_callback:
            self.state_changed_callback(new_state)

    def updateIcon(self):
        icon_path = self.current_state()
        if icon_path:
            self.computer_icon.setPixmap(QPixmap(icon_path).scaledToWidth(50))
        else:
            print("Icon path not found")
    
    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            self.show_options_menu()

    def show_options_menu(self): 
        if self.pc_state == 0:
            menu = PowerOffMenu(self.pc_data)
            menu.actionSelected.connect(self.handle_menu_action)
            menu.exec_(self.mapToGlobal(QPoint(0,0)))
        elif self.pc_state == 1:
            menu = WaitingMenu(self)
            menu.actionSelected.connect(self.handle_menu_action)
            menu.exec_(self.mapToGlobal(QPoint(0,0)))
        elif self.pc_state == 2:
            menu = PowerOnMenu(self.pc_data, self)
            menu.actionSelected.connect(self.handle_menu_action)
            menu.exec_(self.mapToGlobal(QPoint(0,0)))
        elif self.pc_state == 3:
            menu = ExamModeON(self.pc_data, self)
            menu.actionSelected.connect(self.handle_menu_action)
            menu.exec_(self.mapToGlobal(QPoint(0,0)))
        else:
            menu = BaseMenu(self.pc_data, self)
            menu.actionSelected.connect(self.handle_menu_action)
            menu.exec_(self.mapToGlobal(QPoint(0,0)))

    def handle_menu_action(self, action):
        if action == "exam_mode_on":
            self.updateState(EX)
        elif action == "shutdown":
            self.updateState(OFF)
        elif action == "exam_mode_off":
            self.updateState(ON)
        elif action == "power_on":
            self.updateState(ON)

    def execute_command(self, command):
        print("Here should execute the command in this pc: {}:{}".format(self.pc_name, self.pc_ip))
        return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Introduce the json file as argument.")
        sys.exit(1)

    json_file = sys.argv[1]
    data = get_pc_list(json_file)
    check_all_ip(data)

    app = QApplication(sys.argv)
    computer_widget = PcWidget(data[0])
    computer_widget.show()

    sys.exit(app.exec_())