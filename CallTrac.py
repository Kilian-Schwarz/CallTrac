v_socket = "Lade"
v_os = "Lade"
v_time = "Lade"
v_datetime = "Lade"
v_tabulate = "Lade"
v_termcolor = "Lade"
v_requests = "Lade"
v_json = "Lade"
v_tshark = "Lade"
v_process = "Lade"

i_version = "0.3.1"
 
def loading(v_socket, v_process,v_os, v_time, v_datetime, v_tabulate, v_termcolor, v_requests, v_json, v_tshark):
    os.system('cls')
    print(
    '\nos        :', v_os,
    '\nsocket    :', v_socket,
    '\ntime      :', v_time,
    '\ndatetime  :', v_datetime,
    '\ntabulate  :', v_tabulate,
    '\ntermcolor :', v_termcolor,
    '\nrequests  :', v_requests,
    '\njson      :', v_json,
    '\ntshark    :', v_tshark,
    '\nprocess   :', v_process
    )
    print("\nby Kilian Schwarz : https://github.com/Kilian-Schwarz")

    return v_socket, v_process,v_os, v_time, v_datetime, v_tabulate, v_termcolor, v_requests, v_json, v_tshark

try:
    import os
    v_socket, v_process,v_os, v_time, v_datetime, v_tabulate, v_termcolor, v_requests, v_json, v_tshark = loading(v_socket, v_process,"Fertig", v_time, v_datetime, v_tabulate, v_termcolor, v_requests, v_json, v_tshark )
except:
    v_socket, v_process,v_os, v_time, v_datetime, v_tabulate, v_termcolor, v_requests, v_json, v_tshark = loading(v_socket, v_process,"FEHLER - pip install os", v_time, v_datetime, v_tabulate, v_termcolor, v_requests, v_json, v_tshark )

try:
    from multiprocessing import Process
    v_socket, v_process,v_os, v_time, v_datetime, v_tabulate, v_termcolor, v_requests, v_json, v_tshark = loading(v_socket, "Fertig",v_os, v_time, v_datetime, v_tabulate, v_termcolor, v_requests, v_json, v_tshark )
except:
    v_socket, v_process,v_os, v_time, v_datetime, v_tabulate, v_termcolor, v_requests, v_json, v_tshark = loading(v_socket, "FEHLER - pip install multiprocessing",v_os, v_time, v_datetime, v_tabulate, v_termcolor, v_requests, v_json, v_tshark )

try:
    import socket, subprocess 
    v_socket, v_process,v_os, v_time, v_datetime, v_tabulate, v_termcolor, v_requests, v_json, v_tshark = loading("Fertig", v_process,v_os, v_time, v_datetime, v_tabulate, v_termcolor, v_requests, v_json, v_tshark )
except:
    v_socket, v_process,v_os, v_time, v_datetime, v_tabulate, v_termcolor, v_requests, v_json, v_tshark = loading("FEHLER - pip install socket",v_process, v_os, v_time, v_datetime, v_tabulate, v_termcolor, v_requests, v_json, v_tshark )


try:
    import time 
    v_socket, v_process,v_os, v_time, v_datetime, v_tabulate, v_termcolor, v_requests, v_json, v_tshark = loading(v_socket, v_process,v_os, "Fertig", v_datetime, v_tabulate, v_termcolor, v_requests, v_json, v_tshark )
except:
    v_socket, v_process,v_os, v_time, v_datetime, v_tabulate, v_termcolor, v_requests, v_json, v_tshark = loading(v_socket, v_process,v_os, "FEHLER - pip install time", v_datetime, v_tabulate, v_termcolor, v_requests, v_json, v_tshark )

try:
    from datetime import datetime
    v_socket, v_process,v_os, v_time, v_datetime, v_tabulate, v_termcolor, v_requests, v_json, v_tshark = loading(v_socket, v_process,v_os, v_time, "Fertig", v_tabulate, v_termcolor, v_requests, v_json, v_tshark )
except:
    v_socket, v_process,v_os, v_time, v_datetime, v_tabulate, v_termcolor, v_requests, v_json, v_tshark = loading(v_socket, v_process,v_os, v_time, "FEHLER - pip install datetime", v_tabulate, v_termcolor, v_requests, v_json, v_tshark )

try:
    from tabulate import tabulate
    v_socket, v_process,v_os, v_time, v_datetime, v_tabulate, v_termcolor, v_requests, v_json, v_tshark = loading(v_socket, v_process,v_os, v_time, v_datetime, "Fertig", v_termcolor, v_requests, v_json, v_tshark )
except:
    v_socket, v_process,v_os, v_time, v_datetime, v_tabulate, v_termcolor, v_requests, v_json, v_tshark = loading(v_socket, v_process,v_os, v_time, v_datetime, "FEHLER - pip install tabulate", v_termcolor, v_requests, v_json, v_tshark )

try:
    from termcolor import colored
    v_socket, v_process,v_os, v_time, v_datetime, v_tabulate, v_termcolor, v_requests, v_json, v_tshark = loading(v_socket, v_process,v_os, v_time, v_datetime, v_tabulate, "Fertig", v_requests, v_json, v_tshark )
except:
    v_socket, v_process,v_os, v_time, v_datetime, v_tabulate, v_termcolor, v_requests, v_json, v_tshark = loading(v_socket, v_process,v_os, v_time, v_datetime, v_tabulate, "FEHLER - pip install termcolor", v_requests, v_json, v_tshark )

try:
    import requests
    v_socket, v_process,v_os, v_time, v_datetime, v_tabulate, v_termcolor, v_requests, v_json, v_tshark = loading(v_socket, v_process,v_os, v_time, v_datetime, v_tabulate, v_termcolor, "Fertig", v_json, v_tshark )
except:
    v_socket, v_process,v_os, v_time, v_datetime, v_tabulate, v_termcolor, v_requests, v_json, v_tshark = loading(v_socket, v_process,v_os, v_time, v_datetime, v_tabulate, v_termcolor, "FEHLER - pip install requests", v_json, v_tshark )

try:
    import json
    v_socket, v_process,v_os, v_time, v_datetime, v_tabulate, v_termcolor, v_requests, v_json, v_tshark = loading(v_socket, v_process,v_os, v_time, v_datetime, v_tabulate, v_termcolor, v_requests, "Fertig", v_tshark )
except:
    v_socket, v_process,v_os, v_time, v_datetime, v_tabulate, v_termcolor, v_requests, v_json, v_tshark = loading(v_socket, v_process,v_os, v_time, v_datetime, v_tabulate, v_termcolor, v_requests, "FEHLER - pip install json", v_tshark )
try:
    if os.path.isfile("C:\\Program Files\\Wireshark\\tshark.exe"):
        v_socket, v_process,v_os, v_time, v_datetime, v_tabulate, v_termcolor, v_requests, v_json, v_tshark = loading(v_socket, v_process,v_os, v_time, v_datetime, v_tabulate, v_termcolor, v_requests, v_json, "Fertig" )
    else:
        v_socket, v_process,v_os, v_time, v_datetime, v_tabulate, v_termcolor, v_requests, v_json, v_tshark = loading(v_socket, v_process,v_os, v_time, v_datetime, v_tabulate, v_termcolor, v_requests,v_json , "FEHLER - installire dir wireshark mit dem module tshark" )
except:
    exit
from pathlib import Path


import requests
import json

update = requests.get('https://api.github.com/repos/Kilian-Schwarz/calltrac/releases/latest')
updatejson = update.json()
if i_version != updatejson['tag_name']:
    print('\n\n!!!        ACHTUNG          !!!')
    print('Du hast eine veraltete version!')
    upd = input('Möchtest du Updaten? (y/n)')
    if upd == "y":
        os.system('start https://github.com/Kilian-Schwarz/CallTrac/releases/latest/')
        quit()

Loadings = v_socket + v_os + v_time + v_datetime + v_tabulate + v_termcolor + v_requests + v_json + v_tshark + v_process


if "FEHLER" in Loadings:
    print("\nInstallieren sie die restlichen module")
    input("Drücke Enter zum Fortfahren...")
    quit()
time.sleep(1)


Starttime = datetime.now().strftime("%H-%M-%p") 

clear = lambda: os.system('cls')
os.system("echo -----------------------------------------------------------   ")
os.system('"C:\\Program Files\\Wireshark\\tshark.exe" --list-interfaces')
os.system('ncpa.cpl')
number = input("Bitte Gib die nummer von deinem Internetnetzwerk ein: ")


os.system('title by Kilian Schwarz : https://github.com/Kilian-Schwarz')
os.system('color 0a')
os.system('mode con: cols=71 lines=30')

cmd = r"C:\Program Files\Wireshark\tshark.exe -i " + number

IP_BEFOR = "0"
process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
myip = socket.gethostbyname(socket.gethostname())



def sendlog(ip):
    f= open(".\\"+ Starttime + "_calltrack-log.txt","a+")
    f.write("Folgende IP wurde getract:  " + ip + "\r")
    f.close() 




def getip(ip):
    location = requests.get(f'http://extreme-ip-lookup.com/json/{ip}')
    geo = location.json()
    clear()
    print(tabulate([
    ['IP', geo['query']],
    ['ipType', geo['ipType']],
    ['Country', geo['country']],
    ['Stadt', geo['country']],
    ['City', geo['city']],
    ['Region', geo['region']],
    ['Continent', geo['continent']],
    ['IPName', geo['ipName']],
    ['ISP', geo['isp']],
    ['Latitute', geo['lat']],
    ['Longitude', geo['lon']],
    ['Org', geo['org']],
    ['Status', geo['status']],
    ['Version 0.3.1', "by Kilian Schwarz : https://github.com/Kilian-Schwarz"]],
     tablefmt='fancy_grid'))
    
    sendlog(ip)

    return


getip("8.8.8.8")





for line in iter(process.stdout.readline, b""):
    columns = str(line).split(" ")

    if "SKYPE" in columns or "UDP" in columns:
        
        # for different tshark versions
        if "->" in columns:
            sip = columns[columns.index("->") - 1]
        elif "\\xe2\\x86\\x92" in columns:
            sip = columns[columns.index("\\xe2\\x86\\x92") - 1]
        else:
            continue
            
        if sip == myip:
            continue
        if sip == IP_BEFOR:
            continue

        result = sip.startswith(('192.168.', '10.', '172.16.'))
        if result:
            continue

        try:
            getip(sip)
            IP_BEFOR = sip
        except:
            try:
                realip = socket.gethostbyname(sip)
                getip(realip)
                IP_BEFOR = realip
            except:
                clear()
                print("Not found")
                print("by Kilian Schwarz : https://github.com/Kilian-Schwarz")

