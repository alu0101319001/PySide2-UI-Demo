# -*- coding: utf-8 -*-
#!/usr/bin/python

import json
import sys
from ip_validation import validate_ip_address

# Carga el JSON y lo transforma en una lista de diccionarios con la información
# de cada PC
def get_pc_list(json_file):
    # Leer el JSON
    try:
        with open(json_file, "r") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print("File {} not found.".format(json_file))
        sys.exit(1)
    except json.JSONDecodeError:
        print("File {} is not a valid JSON".format(json_file))
        sys.exit(1)

# Recorre toda la lista y checkea que cada IP sea válida
def check_all_ip(data):
    for pc in data:
        try:
            if not validate_ip_address(pc["ip"]):
                print("Not all IPs are valid. Check JSON file.")
                return False
        except ValueError as e:
            print("IP format not valid: {}.\nCause:{}".format(pc["ip"],e))
            return False
    print("All IPs are valid. Good job!")
    return True

def process_files(file_paths):
    data_list = []
    for file_path in file_paths:
        data = get_pc_list(file_path)
        check_all_ip(data)
        data_list.append(data)
    return data_list

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Introduce the json file as argument.")
        sys.exit(1)

    json_file = sys.argv[1]
    data = get_pc_list(json_file)
    check_all_ip(data)
    





