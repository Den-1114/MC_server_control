import os

versions = {
    "1.20.5": "paper_1.20.5.jar",
    "1.20.4": "paper_1.20.4.jar",
    "1.20.3": "paper_1.20.3.jar",
    "1.20.2": "paper_1.20.2.jar",
    "1.20.1": "paper_1.20.1.jar",
    "1.20": "paper_1.20.jar",
    "1.19.4": "paper_1.19.4.jar",
}

print(""" __  __ _                            __ _                                  
|  \/  (_)_ __   ___  ___ _ __ __ _ / _| |_   ___  ___ _ ____   _____ _ __ 
| |\/| | | '_ \ / _ \/ __| '__/ _` | |_| __| / __|/ _ \ '__\ \ / / _ \ '__|
| |  | | | | | |  __/ (__| | | (_| |  _| |_  \__ \  __/ |   \ V /  __/ |   
|_|  |_|_|_| |_|\___|\___|_|  \__,_|_|  \__| |___/\___|_|    \_/ \___|_|   
  ___ ___  _ __ | |_ _ __ ___ | |                                          
 / __/ _ \| '_ \| __| '__/ _ \| |                                          
| (_| (_) | | | | |_| | | (_) | |                                          
 \___\___/|_| |_|\__|_|  \___/|_|                                          """)

print("Welcome to Minecraft Server Control!")
print("Warning: Before you run this script, make sure you have Java installed.")

server_version = input("Which version do you want to use? (1.19.4, 1.20, 1.20.1, 1.20.2, 1.20.3, 1.20.4, 1.20.5) : ")
try:
    server_ram = int(input("How many MB RAM do you want to use? : "))
except ValueError:
    server_ram = 4096

user_version = server_version
user_ram = server_ram

os.system(f"java -Xmx{user_ram}M -Xms{user_ram}M -jar {versions[user_version]}")