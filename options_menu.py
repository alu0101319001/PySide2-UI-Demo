# -*- coding: utf-8 -*-
#!/usr/bin/python

from PySide2.QtWidgets import QMenu, QAction, QLineEdit, QFileDialog, QInputDialog
from PySide2.QtCore import Signal

from show_command_dialog import show_command_dialog

class BaseMenu(QMenu):
    actionSelected = Signal(str)

    def __init__(self, pc_data, parent=None):
        super(BaseMenu, self).__init__(parent)
        self.pc_data = pc_data
        self.init_ui()

    def init_ui(self):
        self.addAction("Show IP", self.show_ip)

    def show_ip(self):
        print("IP: {}".format(self.pc_data["ip"]))

    def shutdown(self):
        self.actionSelected.emit("shutdown")
        print("Shutdowning....")

    def exam_mode_on(self):
        self.actionSelected.emit("exam_mode_on")
        print("ACTIVATE EXAM MODE")
    
    def exam_mode_off(self):
        self.actionSelected.emit("exam_mode_off")
        print("Desactivated EXAM MODE")

    def sync(self):
        print("Sync")

    def send_files(self):
        file_dialog = QFileDialog()
        file_dialog.exec_()
        selected_files = file_dialog.selectedFiles()
        print("Send files:", selected_files)

    def backup(self):
        print("Backup files")

    def power_on(self):
        self.actionSelected.emit("power_on")
        print("POWER ONNNN")

    def run_command(self):
        show_command_dialog("Aceptado a:{}".format(self.parent()), self)


class PowerOnMenu(BaseMenu):
    def __init__(self,pc_data, parent=None):
        super(PowerOnMenu, self).__init__(pc_data,parent)

    def init_ui(self):
        super(PowerOnMenu, self).init_ui()
        self.addAction("Run command...", self.run_command)
        self.addAction("Exam Mode ON", self.exam_mode_on)
        self.addAction("Sync...", self.sync)
        self.addAction("Send...", self.send_files)
        self.addAction("Backup...", self.backup)
        self.addAction("Shutdown", self.shutdown)

    

class WaitingMenu(BaseMenu):
    def __init__(self, parent=None):
        super(WaitingMenu, self).__init__(parent)

    def init_ui(self):
        return super(WaitingMenu, self).init_ui()

class PowerOffMenu(BaseMenu):
    def __init__(self, parent=None):
        super(PowerOffMenu, self).__init__(parent)

    def init_ui(self):
        super(PowerOffMenu, self).init_ui()
        self.addAction("Power ON", self.power_on)


class ExamModeON(BaseMenu):
    def __init__(self,pc_data, parent=None):
        super(ExamModeON, self).__init__(pc_data,parent)

    def init_ui(self):
        super(ExamModeON, self).init_ui()
        self.addAction("Run command...", self.run_command)
        self.addAction("Exam Mode OFF", self.exam_mode_off)
        self.addAction("Sync...", self.sync)
        self.addAction("Send...", self.send_files)
        self.addAction("Backup...", self.backup)
        self.addAction("Shutdown", self.shutdown)

    
    
        # Aqui debería cambiar el json para que mientras un 
        # watchdog quer lo monitorea, detecte el cambio
        # y se ejecute una función de upgrade en los widgets
        # Quizas, no me gusta mucho esta forma. 
        