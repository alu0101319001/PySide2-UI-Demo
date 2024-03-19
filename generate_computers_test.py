# -*- coding: utf-8 -*-
#!/usr/bin/python
import sys
import json
import random
from datetime import datetime

def version_1():
    if len(sys.argv) < 2:
            print("Introduce the json file name")
            sys.exit(1)


    pcs = []
    json_name = sys.argv[1]
    for i in range(1,21):
        name = "PC{}".format(i)
        state = random.choice([0,1,2])
        ip_address = "192.168.0.{}".format(i)
        pc = {
            "name": name,
            "state": state,
            "ip": ip_address
        }
        pcs.append(pc)

    with open(json_name, "w") as f:
        json.dump(pcs, f, indent=4)

    print("JSON file generated as {}".format(json_name))

def version_2():
    def generate_random_ip():
        return ".".join(str(random.randint(0, 255)) for _ in range(4))

    computers = []
    for _ in range(20):
        location = f"Location_{random.randint(1, 10)}.{random.randint(1, 5)}"  # Generar ubicación en formato [sala].[edificio]
        
        computer = {
            "tag_name": f"PC_{random.randint(1, 100)}",
            "status": random.choice(['ON', 'OFF', 'EXM', 'WAI', 'WRN', 'MIS']),
            "location": location,
            "branch": f"Branch_{random.randint(1, 5)}",
            "ip": generate_random_ip(),
            "serial_number": f"SN_{random.randint(1000, 9999)}",
            "last_maintenance_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "last_login_timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        computers.append(computer)

    # Guardar los datos en un archivo JSON
    with open("computers_data.json", "w") as file:
        json.dump(computers, file, indent=4)

version_2()
     

