# -*- coding: utf-8 -*-
#!/usr/bin/python

import sys
import json
from PySide2.QtWidgets import (
    QMessageBox, QApplication
)
from PySide2.QtSql import (
    QSqlDatabase, QSqlQuery
)

parent_widget = QApplication.activeWindow()

class DatabaseManager:
    def __init__(self):
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("admin_database.db")

        if not self.db.open():
            QMessageBox.critical(parent_widget, "Conexion error", "Not possible to open the database")
            return None
        
    ### CREATE TABLES ### 
    def create_table_from_schema(self, schema_file, query_name):
        with open(schema_file, 'r') as file:
            schema_queries = file.read()
            queries = schema_queries.split(';') # Separar consultas por ';'
            for query in queries:
                if query_name in query:
                    query = query.strip() # Elimina espacios en blanco
                    if query.endswith(';'):
                        query = query[:-1] # Elimina ';' al final si existe
                    success = QSqlQuery().exec_(query)
                    break
                else:
                    success = False
        if success:
            QMessageBox.information(parent_widget, "Table created", "The query '{}' was succesful.".format(query_name))
            return True
        else:
            QMessageBox.critical(parent_widget, "Error in table creation", "The query '{}' could not be resolved.".format(query_name))  
            return False 

    ### CREATE ENTRIES ###
    def create_new_user(self, username, password, role, 
                        email=None, avatar_path=None,
                        nickname=None, first_name=None,last_name=None):
        query = QSqlQuery()
        query.prepare(""" 
            INSERT INTO user (username, password, email, role, avatar_path, nickname, first_name, last_name)
            VALUES (:username,:password,:email,:role,:avatar_path,:nickname,:first_name,:last_name)
        """)
        query.bindValue(":username", username)
        query.bindValue(":password", password)
        query.bindValue(":role", role)
        query.bindValue(":email", email)
        query.bindValue(":avatar_path", avatar_path)
        query.bindValue(":nickname", nickname)
        query.bindValue(":first_name", first_name)
        query.bindValue(":last_name", last_name)
        if not query.exec_():
            error_message = query.lastError().text()
            QMessageBox.critical(parent_widget, "Error", "Failed to register user: {}".format(error_message))
            return False
        return True

    
    def create_new_computer(self, tag_name, status, location,
                            branch=None, ip=None, serial_number=None,
                            last_maintenance_date=None):
        query = QSqlQuery()
        query.prepare("""
            INSERT INTO computer (tag_name, status, location, branch, ip, serial_number, last_maintenance_date)
            VALUES (:tag_name,:status,:location,:branch,:ip,:serial_number,:last_maintenance_date)
        """)
        query.bindValue(":tag_name",tag_name)
        query.bindValue(":status",status)
        query.bindValue(":location",location)
        query.bindValue(":branch",branch)
        query.bindValue(":ip",ip)
        query.bindValue(":serial_number",serial_number)
        query.bindValue(":last_maintenance_date",last_maintenance_date)
        if not query.exec_():
            error_message = query.lastError().text()
            print(error_message)
            # QMessageBox.critical(parent_widget, "Error", "Failed to register user: {}".format(error_message))
            return False
        return True
    
    def create_new_access(self, user_id, computer_id, login_timestamp):
        query = QSqlQuery()
        query.prepare("INSERT INTO access (user_id, computer_id, login_timestamp) VALUES (:user_id,:computer_id,:login_timestamp)")
        query.bindValue(":user_id",user_id)
        query.bindValue(":computer_id",computer_id)
        query.bindValue(":login_timestamp", login_timestamp)
        success = query.exec_()
        return {"success": success}
    
    ### ACCESS DATA ###
    def get_user_by_id_or_username(self, user_id=None, username=None):
        query = QSqlQuery()

        if user_id is not None:
            query.prepare("SELECT * FROM user WHERE id = :user_id")
            query.bindValue(":user_id", user_id)
        elif username is not None:
            query.prepare("SELECT * FROM user WHERE username = :username")
            query.bindValue(":username", username)
        else:
            QMessageBox.critical(parent_widget, "Error in get_user", "A search filter must be given (user_id or username)")
            return None # Ambos paramentros None
        
        success = query.exec_()
        if success:
            user_data = {}
            if query.next():
                user_data["id"] = query.value(0)
                user_data["username"] = query.value(1)
                user_data["password"] = query.value(2)
                user_data["email"] = query.value(3)
                user_data["role"] = query.value(4)
                user_data["last_login_timestamp"] = query.value(5)
                user_data["avatar_path"] = query.value(6)
                user_data["nickname"] = query.value(7)
                user_data["first_name"] = query.value(8)
                user_data["last_name"] = query.value(9)

                return user_data
        else:
            QMessageBox.critical(parent_widget, "Error in get_user", "A problem happened in the query.")  
            return False 
        
    def get_computer_by_id_or_tagname_ip_location(self, computer_id=None, tag_name=None, ip=None, location=None):
        query = QSqlQuery()

        if computer_id is not None:
            query.prepare("SELECT * FROM computer WHERE id = :computer_id")
            query.bindValue(":computer_id", computer_id)
        elif (tag_name and location) is not None:
            query.prepare("SELECT * FROM computer WHERE tag_name = :tag_name AND location = :location")
            query.bindValue(":tag_name", tag_name)
            query.bindValue(":location", location)
        elif (ip and location) is not None:
            query.prepare("SELECT * FROM computer WHERE ip = :ip AND location = :location")
            query.bindValue(":ip", ip)
            query.bindValue(":location", location)
        else:
            QMessageBox.critical(parent_widget, "Error in get_computer", "A search filter must be given (computer_id or tagname+location or ip+location)")  
            return False 

        success = query.exec_()
        if success:
            computer_data = {}
            if query.next():
                computer_data["id"] = query.value(0)
                computer_data["tag_name"] = query.value(1)
                computer_data["status"] = query.value(2)
                computer_data["location"] = query.value(3)
                computer_data["branch"] = query.value(4)
                computer_data["ip"] = query.value(5)
                computer_data["serial_number"] = query.value(6)
                computer_data["last_maintenance_date"] = query.value(7)
                computer_data["last_login_timestamp"] = query.value(8)

                return computer_data
        else:
            QMessageBox.critical(parent_widget, "Error in get_user", "A problem happened in the query.")  
            return False 
        
    def get_access_by_id(self, access_id):
        query = QSqlQuery()
        
        query.prepare("SELECT * FROM access WHERE id = :access_id")
        query.bindValue(":access_id", access_id)
        success = query.exec_()
        if success:
            access_data = {}
            if query.next():
                access_data["id"] = query.value(0)
                access_data["user_id"] = query.value(1)
                access_data["computer_id"] = query.value(2)
                access_data["login_timestamp"] = query.value(3)
                access_data["logout_timestmap"] = query.value(4)

                return access_data
        else:
            QMessageBox.critical(parent_widget, "Error in get_access", "A problem happened in the query.")
            return False
        
    def get_access_by_computerid(self, computer_id):
        query = QSqlQuery()
        
        query.prepare("SELECT * FROM access WHERE computer_id = :computer_id")
        query.bindValue(":computer_id", computer_id)
        success = query.exec_()
        if success:
            access_data = {}
            if query.next():
                access_data["id"] = query.value(0)
                access_data["user_id"] = query.value(1)
                access_data["computer_id"] = query.value(2)
                access_data["login_timestamp"] = query.value(3)
                access_data["logout_timestmap"] = query.value(4)

                return access_data
        else:
            QMessageBox.critical(parent_widget, "Error in get_access", "A problem happened in the query.")
            return False
        

    ### UPDATE ENTRIES ###
    def update_user_null(self, user_id, email=None, last_login_timestamp=None, avatar_path=None,
                         nickname=None, first_name=None, last_name=None):
        query = QSqlQuery()
        query.prepare("""
            UPDATE user SET
                      email = :email,
                      last_login_timestamp = :last_login_timestamp,
                      avatar_path = :avatar_path,
                      nickname = :nickname,
                      first_name = :first_name,
                      last_name = :last_name
                      WHERE id = :user_id
        """)
        query.bindValue(":email", email)
        query.bindValue(":last_login_timestamp", last_login_timestamp)
        query.bindValue(":avatar_path", avatar_path)
        query.bindValue(":nickname", nickname)
        query.bindValue(":first_name", first_name)
        query.bindValue(":last_name", last_name)
        query.bindValue(":user_id", user_id)

        success = query.exec_()
        if success:
            return self.get_user_by_id_or_username(user_id)
        else:
            QMessageBox.critical(parent_widget, "Error in update_user_null", "A problem happened in the query.")
            return False

    def update_user_not_null(self, user_id, username, password, role):
        query = QSqlQuery()
        query.prepare("""
            UPDATE user SET
                      username = :username,
                      password = :password,
                      role = :role
                      WHERE id = :user_id
        """)
        query.bindValue(":username", username)
        query.bindValue(":password", password)
        query.bindValue(":role", role)
        query.bindValue(":user_id", user_id)

        success = query.exec_()
        if success:
            return self.get_user_by_id_or_username(user_id)
        else:
            QMessageBox.critical(parent_widget, "Error in update_user_not_null", "A problem happened in the query.")
            return False
        
    def update_computer_null(self, computer_id, branch=None,ip=None,serial_number=None,
                             last_maintenance_date=None, last_login_timestamp=None):
        query = QSqlQuery()
        query.prepare("""
            UPDATE computer SET
                      branch = :branch,
                      ip = :ip,
                      serial_number = :serial_number,
                      last_maintenance_date = :last_maintenance_date,
                      last_login_timestamp = :last_login_timestamp
                      WHERE id = :compuert_id
        """)
        query.bindValue(":branch", branch)
        query.bindValue(":ip", ip)
        query.bindValue(":serial_number", serial_number)
        query.bindValue(":last_maintenance_date", last_maintenance_date)
        query.bindValue(":last_login_timestamp", last_login_timestamp)

        success = query.exec_()
        if success:
            return self.get_computer_by_id_or_tagname_ip_location(computer_id)
        else:
            QMessageBox.critical(parent_widget, "Error in update_computer_null", "A problem happened in the query.")
            return False
        
    def update_computer_not_null(self, computer_id, tag_name, status, location):
        query = QSqlQuery()
        query.prepare("""
            UPDATE computer SET
                      tag_name = :tag_name,
                      status = :status,
                      location = :location
                      WHERE id = :computer_id
        """)
        query.bindValue(":tag_name", tag_name)
        query.bindValue(":status", status)
        query.bindValue(":location", location)
        query.bindValue(":computer_id", computer_id)

        success = query.exec_()
        if success:
            return self.get_computer_by_id_or_tagname_ip_location(computer_id)
        else:
            QMessageBox.critical(parent_widget, "Error in update_computer_not_null", "A problem happened in the query.")
            return False
        
    def update_access(self, computer_id, logout_timestamp):
        query = QSqlQuery()
        query.prepare("""
            UPDATE access SET
                      logout_timestamp = :logout_timestamp
                      WHERE computer_id = :computer_id
        """)
        query.bindValue(":logout_timestamp", logout_timestamp)
        query.bindValue(":computer_id", computer_id)

        success = query.exec_()
        if success:
            return self.get_access_by_computerid(computer_id)
        else:
            QMessageBox.critical(parent_widget, "Error in update_access", "A problem happened in the query.")
            return False
        
    ### DELETE QUERIES ###
    def delete_user_by_id(self, user_id):
        query = QSqlQuery()
        query.prepare("DELETE FROM user WHERE id = :user_id")
        query.bindValue(":user_id", user_id)

        success = query.exec_()
        return success
    
    def delete_computer_by_id(self, computer_id):
        query = QSqlQuery()
        query.prepare("DELETE FROM computer WHERE id = :computer_id")
        query.bindValue(":computer_id", computer_id)
        
        success = query.exec_()
        return success
    
    def delete_access_by_id(self, access_id):
        query = QSqlQuery()
        query.prepare("DELETE FROM computer WHERE id = :access_id")
        query.bindValue(":access_id", access_id)

        success = query.exec_()
        return success
                
    
    ### USEFUL QUERIES ### 
    def get_user_id_by_username(self, username):
        query = QSqlQuery()
        query.prepare("SELECT id FROM user WHERE username = :username")
        query.bindValue(":username", username)
        query.exec_()

        user_id = None
        if query.next():
            user_id = query.value(0)

        return user_id # SI NO LO ENCUENTRA DA NONE, CUIDADO CON ESO
    
    def get_computer_id_by_tagname(self, tag_name):
        query = QSqlQuery()
        query.prepare("SELECT id FROM computer WHERE tag_name = :tag_name")
        query.bindValue(":tag_name", tag_name)
        query.exec_()

        computer_id = None
        if query.next():
            computer_id = query.value(0)
        
        return computer_id # SI NO LO ENCUENTRA DA NONE, CUIAITO
    
    def create_room_by_json(self, json_file):
        with open(json_file, "r") as file:
            computers_data = json.load(file)
        
        for computer in computers_data:
            self.create_new_computer(computer["tag_name"], computer["status"], 
                                     computer["location"], computer["branch"],
                                     computer["ip"], computer["serial_number"],
                                     computer["last_maintenance_date"])

    def execute_query(self, query_string):
        query = QSqlQuery()
        success = query.exec_(query_string)
        if success:
            print("Query executed successfully.")
            while query.next():
                record = ""
                for i in range(query.record().count()):
                    record += str(query.value(i)) + " | "
                print(record)
        else:
            print("Error executing query.")

    
    ### INTERESTING QUERIES ###
    def get_computer_by_state(self, state):
        query = QSqlQuery()
        query.prepare("SELECT * FROM computer WHERE state = :state")
        query.bindValue(":state", state)
        query.exec_()

        computers = []
        while query.next():
            computer_data = {
                "id": query.value(0),
                "tag_name": query.value(1),
                "status": query.value(2),
                "location": query.value(3),
                "branch": query.value(4),
                "ip": query.value(5),
                "serial_number": query.value(6),
                "last_maintenance_date": query.value(7),
                "last_login_timestamp": query.value(8)
            }
            computers.append(computer_data)

        return computers






if __name__ == "__main__":
    db_manager = DatabaseManager()

    db_manager.execute_query("SELECT * FROM user")
    db_manager.execute_query("SELECT * FROM computer")


