# -*- coding: utf-8 -*-
#!/usr/bin/python

import sys
from read_pc_json import get_pc_list, check_all_ip
from room_widget import RoomWidget
from PySide2.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QStackedLayout,
    QWidget, QTabWidget
)

class PcZone(QWidget):
    def __init__(self, rooms_list):
        super(PcZone, self).__init__()
        self.setWindowTitle("PC Zone")
        self.layout = QVBoxLayout(self)

        self.tab_widget = QTabWidget()
        self.layout.addWidget(self.tab_widget)

        self.rooms_list = rooms_list
        count = 0
        for room_data in self.rooms_list:
            count += 1
            room_widget = RoomWidget(room_data)
            self.tab_widget.addTab(room_widget, "Room {}".format(count))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Introduce the json file as argument.")
        sys.exit(1)

    json_file = sys.argv[1]
    data = get_pc_list(json_file)
    check_all_ip(data)

    rooms_list = [data, data, data]

    app = QApplication(sys.argv)
    computer_zone = PcZone(rooms_list)
    computer_zone.show()
    sys.exit(app.exec_())

    

