#must be run as an administrator
import os
from time import sleep

#default var

def_delay=300
def_way=""
def_card=""
def_mac=""
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
""",

r"""
                 _
                 \`\
       /./././.   | |
     /        `/. | |
    /     __    `/'/'
 /\__/\ /'  `\    /
|  oo  |      `.,.|
 \vvvv/        ||||
   ||||        ||||      Mikmac.py
   `'`'        `'`'

"""
]

mode=int(input("""

[1] Default (change mac adress one times)

[2] chain (change mac adress every x seconds)

chosen mod (1,2): """)[0])

if mode not in [1,2]:
    print("put an existing mod")

print("\033[0;36m",cat[mode-1],"\033[0m")

if mode == 2:
    way=input(".txt file path (/home/...) : ")
    delay=input("delay between changing mac adress (s): ")

    if way=="":
        way=def_way
    if delay=="":
        delay=def_delay
    else:
        delay = int(delay)

    with open(way, 'r') as file:
        mac=[line[:17] for line in file if line[0]!="#"]

else:
    mac=[input("mac adress : ")]
    if mac[0] == "":
        mac[0] = def_mac

card=input("wifi card : ")
if card=="":
    card = def_card

i=0
while True:
    print("["+str(i+1)+"]-------------------------------------\n")
    os.system("ifconfig "+card+" down")
    os.system("macchanger -m "+mac[i]+" "+card)
    os.system("ifconfig "+card+" up")
    print("----------------------------------------\n")
    if mode == 2:
        i+=1
        if i==len(mac):
            i=0
        sleep(delay)
    else:exit()
