# -*- coding: utf-8 -*-
#!/usr/bin/python

import sys
import argparse
from PySide2.QtWidgets import QApplication
from bbdd import DatabaseManager
from login_window import LoginWindow
from register_window import RegisterWindow
from read_pc_json import process_files
from mainWindow import ControlCommandView


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process multiple files and add their data to the system")
    parser.add_argument('files', metavar="FILE", type=str, nargs='+', help='input files to be processed')
    args = parser.parse_args()

    file_paths = args.files
    data_list = process_files(file_paths)

    app = QApplication([])

    # Crear las tablas al iniciar la aplicación
    db_manager = DatabaseManager()
    db_manager.create_table_from_schema('schema.sql', "CREATE TABLE IF NOT EXISTS user")

    # Ventanas
    login_window = LoginWindow(db_manager)
    register_window = RegisterWindow(db_manager)
    main_window = ControlCommandView(data_list,db_manager)

    # Señales
    login_window.open_register.connect(register_window.show)  # Corregir aquí
    register_window.registration_completed.connect(login_window.show)  # Corregir aquí
    # login_window.login_successful.connect(main_window.on_login_successful)
    login_window.login_successful.connect(QApplication.instance().quit)


    login_window.show()

    app.exec_()