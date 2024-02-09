#must be run as an administrator
import os
from time import sleep

#default var

def_delay=300
def_way=""
def_card=""
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

[3] chain with in python file settings

chosen mode (1,2,3): """)[0])

print("\033[0;36m",cat[mode-1],"\033[0m")
card=""
if mode != 1:
    if mode == 3:
        way=def_way
        delay=def_delay
        card=def_card
    else:
        way=input(".txt file path (/home/...) : ")
        delay=int(input("delay between changing mac adress (s): "))
    with open(way, 'r') as file:
        mac=[line[:-1] for line in file]

else:
    mac=[input("mac adress : ")]

if card=="":
    card=input("wifi card : ")
i=0
while True:
    print("["+str(i+1)+"]-------------------------------------\n")
    os.system("ifconfig "+card+" down")
    os.system("macchanger -m "+mac[i]+" "+card)
    os.system("ifconfig "+card+" up")
    print("----------------------------------------\n")
    if mode != 1:
        i+=1
        if i==len(mac):
            i=0
        sleep(delay)
    else:exit()
