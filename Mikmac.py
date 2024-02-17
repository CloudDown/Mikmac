#must be run as an administrator
import os,subprocess
from time import sleep

#default var

def_delay=300
def_way=""
def_card=""
def_mac=""

delay=0
cat=[
r"""
      |\      _,,,---,,_
ZZZzz /,`.-'`'    -.  ;-;;,_
     |,4-  ) )-,_. ,\ (  `'-'
    '---''(_/--'  `-'\_)         Mikmac.py
""",

r"""
 _._     _,-'""`-._
(,-.`._,'(       |\`-/|
    `-.-' \ )-`( , o o)
          `-    \`_`"'-     Mikmac.py
"""
]

def mode():
    return int(input("""
    [1] Default (change mac adress one times)

    [2] chain (change mac adress every x seconds)

    chosen mod (1,2): """)[0])

mode=mode()
if mode not in [1,2]:
    print("")
    print("\033[0;31m"," PUT AN EXISTING MOD !!","\033[0m")
    mode = mode()


print("\033[0;36m",cat[mode-1],"\033[0m")

if mode == 2:
    way=input(".txt file path (/home/...) : ")
    delay=input("delay between changing mac adress (s): ")

    if way=="":
        way=def_way
    if delay=="":
        delay=def_delay

    with open(way, 'r') as file:
        mac=[line[:17] for line in file if line[0]!="#"]

else:
    mac=[input("mac adress : ")]

card=input("wifi card : ")


if card=="":
    card = def_card
if mac[0] == "":
    mac[0] = def_mac

i=0
t=(1,0)
if mode==2:
    t=(0,1)
print("")
def changer(char,mode_f,card_f,mac_f,delay_f,i):
    mac_f[i]=mac_f[i].upper()

    print(char[0]*"---"+char[1]*("["+str(i+1)+"]")+"-------------------------------------\n")
    os.system("ifconfig "+card_f+" down")
    os.system("macchanger -m "+mac_f[i]+" "+card_f)
    os.system("ifconfig "+card_f+" up")
    print("----------------------------------------\n")
    verif_mac=subprocess.check_output("ifconfig "+card_f+" | grep -o -E '([[:xdigit:]]{1,2}:){5}[[:xdigit:]]{1,2}'",shell=True)
    verif_mac=str(verif_mac)[2:-3].upper()
    if verif_mac != mac_f[i]:
        err_input=input("\033[0;31m ERROR the MAC ADRESS did not change, would you retry : \033[0m").lower()
        if "y" in err_input:
            changer(char,mode_f,card_f,mac_f,delay_f,i)
    if mode == 1:
        return
    if i==len(mac_f):
        i=0
    sleep(delay_f)
    changer(char,mode_f,card_f,mac_f,delay_f,i+1)


changer(t,mode,card,mac,delay,i)
