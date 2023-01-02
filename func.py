import os
import colorama
from colorama import init, Fore, Back, Style
colorama.init(autoreset = True)


def create_txt():
    if not os.path.isfile("combo.txt"):
        with open("combo.txt", "w") as f:
            f.close()


def hit():
    string = (Fore.GREEN + "[   HIT   ] ")
    return string

def fail():
    string = (Fore.RED + "[   FAIL  ] ")
    return string

def custom():
    string = (Fore.YELLOW + "[  CUSTOM ] ")
    return string

def error():
    string = (Fore.MAGENTA + "[  ERROR  ] ")
    return string


def logo():
    print(f"""
   -/~/ / ~\                     :;                \       _  > /(~\/
  || | | /\ ;\                   |l      _____     |;     ( \/    > >
  _\\)\)\)/ ;;;                  `8o __-~     ~\   d|      \      //
 ///(())(__/~;;\                  "88p;.  -. _\_;.oP        (_._/ /
(((__   __ \\   \                  `>,% (\  (\./)8"         ;:'  i
)))--`.'-- (( ;,8 \               ,;%%%:  ./V^^^V'          ;.   ;.
((\   |   /)) .,88  `: ..,,;;;;,-::::::'_::\   ||\         ;[8:   ;
 )|  ~-~  |(|(888; ..``'::::8888oooooo.  :\`^^^/,,~--._    |88::  |
 |\ -===- /|  \8;; ``:.      oo.8888888888:`((( o.ooo8888Oo;:;:'  |
 |_~-___-~_|   `-\.   `        `o`88888888b` )) 888b88888P""'     ;
 ; ~~~~;~~         "`--_`.       b`888888888;(.,"888b888"  ..::;-'
   ;      ;              ~"-....  b`8888888:::::.`8888. .:;;;''
      ;    ;                 `:::. `:::OOO:::::::.`OO' ;;;''
 :       ;                     `.      "``::::::''    .'
    ;                           `.   \_              /
  ;       ;                       +:   ~~--  `:'  -'; - Mega.nz Account Checker.
                                   `:         : .::/  - Full Capture.
      ;                            ;;+_  :::. :..;;;  - Coded by Arboff.
                                   ;;;;;;,;;;;;;;;,;  - Special Thanks to all the folks at the Circle.




""")