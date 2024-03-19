# -*- coding: utf-8 -*-
#!/usr/bin/python

import sys
from read_pc_json import get_pc_list, check_all_ip
from show_command_dialog import show_command_dialog
from pc_widget import PcWidget
from PySide2.QtWidgets import (
    QWidget, QGridLayout, QApplication
)

class RoomWidget(QWidget):
    def __init__(self, room_data, parent=None):
        super(RoomWidget, self).__init__(parent)

        self.room_data = room_data
        self.init_ui()

    def init_ui(self):
        grid_layout = QGridLayout()
        grid_layout.setSpacing(10)

        for i, pc_data in enumerate(self.room_data):
            row = i//4
            column = i%4
            pc_widget = PcWidget(pc_data)
            grid_layout.addWidget(pc_widget, row, column)

        self.setLayout(grid_layout)

    def updateAllPcsState(self, new_state):
        # Iterar sobre todos los PcWidget 
        for pc_widget in self.findChildren(PcWidget):
            pc_widget.updateState(new_state)

    def executeCommandInAll(self):
        command = show_command_dialog("Aceptado a:{}".format(self.parent()), self)
        for pc_widget in self.findChildren(PcWidget):
            pc_widget.execute_command(command)




if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Introduce the json file as argument.")
        sys.exit(1)

    json_file = sys.argv[1]
    data = get_pc_list(json_file)
    check_all_ip(data)

    app = QApplication(sys.argv)

    room_widget = RoomWidget(data)
    room_widget.show()

    sys.exit(app.exec_())
