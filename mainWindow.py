# -*- coding: utf-8 -*-
#!/usr/bin/python

import sys
import argparse
from read_pc_json import get_pc_list, check_all_ip, process_files
from PySide2.QtWidgets import (
    QMainWindow, QHBoxLayout, QWidget, QApplication, QListWidgetItem
)
from PySide2.QtCore import Slot
from sidebar_widget import SidebarWidget
from configure_sidebar import build_orders_section, build_state_section
from pc_zone import PcZone
from pc_widget import ON, OFF, EX, WT

class ControlCommandView(QMainWindow):
    @Slot()
    def on_login_successful(self):
        print("Login exitoso. Conexion de señal probada jejejeje")
        QApplication.instance().quit
        return True

    def __init__(self, rooms, db_manager):
        super(ControlCommandView, self).__init__()
        self.setWindowTitle("System Administrator")

        # Widget principal
        self.mainWidget = QWidget()
        self.setCentralWidget(self.mainWidget)
        self.layout = QHBoxLayout(self.mainWidget)
        self.setFixedSize(1400,768)

        # Integrar el sidebar
        self.sidebar = SidebarWidget()
        state_section = build_state_section()
        order_section = build_orders_section()
        self.sidebar.addSection(state_section)
        self.sidebar.addSection(order_section)
        self.layout.addWidget(self.sidebar, 1) # Ajustar tamaño
        # Conectar la señal buttonClicked de SidebarWidget con el método handleButtonClicked de MainWindow
        self.sidebar.sections[0].buttonClicked.connect(self.handleButtonClicked)

        # Carga datos
        self.db_manager = db_manager
        self.rooms = rooms

        # Integra el PcZone
        self.pcZone = PcZone(self.rooms)
        self.layout.addWidget(self.pcZone, 4) # Ajustar tamaño

    def handleButtonClicked(self, buttonText):
        print("Button clicked:", buttonText)
        # Obtener la pestaña actualmente seleccionada en la PcZone
        current_tab_index = self.pcZone.tab_widget.currentIndex()
        room_widget = self.pcZone.tab_widget.widget(current_tab_index)

        # Ejecutar la acción correspondiente en la pestaña actual
        if buttonText == "Power ON ALL":
            room_widget.updateAllPcsState(ON)
        elif buttonText == "Power OFF ALL":
            room_widget.updateAllPcsState(OFF)
        elif buttonText == "ACTIVATE EXAM MODE":
            room_widget.updateAllPcsState(EX)
        elif buttonText == "DESACTIVATE EXAM MODE":
            room_widget.updateAllPcsState(ON)
        elif buttonText == "Execute a command for all PCs":
            room_widget.executeCommandInAll()




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process multiple files and add their data to the system")
    parser.add_argument('files', metavar="FILE", type=str, nargs='+', help='input files to be processed')
    args = parser.parse_args()

    file_paths = args.files
    data_list = process_files(file_paths)

    app = QApplication(sys.argv)
    mainWindow = ControlCommandView(data_list)
    mainWindow.show()
    sys.exit(app.exec_())