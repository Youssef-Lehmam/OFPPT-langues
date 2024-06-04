import pyautogui as p
import time
import math
import random
import ctypes
from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from colorama import Fore                               
from colorama import Style
import os

os.system('cls' if os.name == 'nt' else 'clear')
####### Colors   ###### 
fr  =   Fore.RED                                            
fc  =   Fore.CYAN                                           
fw  =   Fore.WHITE                                          
fg  =   Fore.GREEN                                          
sd  =   Style.DIM                                           
sn  =   Style.NORMAL                                        
sb  =   Style.BRIGHT
#######################

def banners():
    banner = """{}

                   ...          
                 ;::::;           ::
               ;::::; :;        :::::: 
              ;::::;  :;    
             ;:::::'   :;     
            ;:::::;     ;.
           ,:::::'       ;           OOO\
           ::::::;       ;          OOOOO\{}
           ;:::::;       ;         OOOOOOOO
          ,;::::::;     ;'         / OOOOOOO
        ;:::::::::`. ,,,;.        /  / DOOOOOO
      .';:::::::::::::::::;,     /  /     DOOOO
     ,::::::;::::::;;;;::::;,   /  /        DOOO
    ;`::::::`'::::::;;;::::: ,#/  /          DOOO
    :`:::::::`;::::::;;::: ;::#  /            DOOO  {}
    ::`:::::::`;:::::::: ;::::# /              DOO
    `:`:::::::`;:::::: ;::::::#/               DOO
     :::`:::::::`;; ;:::::::::##                OO
     ::::`:::::::`;::::::::;:::#                OO
     `:::::`::::::::::::;'`:;::#                O
      `:::::`::::::::;' /  / `:#
       ::::::`:::::;'  /  /   `#                                                                                            

        \n""".format(fg, fr, fg, sn)
        
    print(banner)
banners()

print(" ██████╗ ███████╗██████╗ ██████╗ ████████╗")
print("██╔═══██╗██╔════╝██╔══██╗██╔══██╗╚══██╔══╝")
print("██║   ██║█████╗  ██████╔╝██████╔╝   ██║   ")
print("██║   ██║██╔══╝  ██╔═══╝ ██╔═══╝    ██║   ")
print("╚██████╔╝██║     ██║     ██║        ██║   ")
print(" ╚═════╝ ╚═╝     ╚═╝     ╚═╝        ╚═╝   ")

print(f'''
        [x]========[x]=========================================[x]
         ║ Made By  ║     https://github.com/Youssef-Lehmam     ║
        [x]========[x]=========================================[x]
        ''')

def mute_system():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMute(1, None)


VIDEOS = [
    "https://app.ofppt-langues.ma/platform/learning-path/mission/PROMOUVOIR_L_EMPLOI_DES_JEUNES/lesson/FR_FR_C1_VOCABULARY_PROMOUVOIR_UNE_GARANTIE_JEUNESSE/activity/FR_FR_C1_VOCABULARY_PROMOUVOIR_UNE_GARANTIE_JEUNESSE_VIDEO?studyLg=fr_FR",
]

SCREEN_SIZE = p.size()


def getRandomVideo():
    return random.choice(VIDEOS)


def main():
    print("\033[91m\033[1mBADAL CLAVIER DYALK L QWERTY.\033[0m")
    input("Press \033[91m\033[1mEnter\033[0m to start executing.\n")


    print("\033[91m\033[1mMAT9ISS LA CLAVIER LA SOURIS.\033[0m")
    for i in range(3, 0, -1):
        time.sleep(1)
        print(f"Script starts in: {i}")
    print(" \n")
    mute_system()
    print("Opening Browser.")
    p.hotkey("win")
    time.sleep(2)
    p.typewrite(("firefox"))
    time.sleep(2)
    p.press("enter")

    time.sleep(5)

    print("Opening Video URL.")
    p.hotkey("ctrl", "t")
    p.typewrite(getRandomVideo())
    p.press("enter")

    time.sleep(5)

    p.press("f11")

    time.sleep(5)
    
    print("Playing the Video.")
    p.moveTo(math.floor(math.floor(SCREEN_SIZE[0] / 2)), math.floor(SCREEN_SIZE[1] / 3))
    p.click()

    iter = 0
    resetCounter = 30
    while True:

        timePassed = format((iter * 10) / 60, ".2f")
        resetCounter -= 1

        time.sleep(15)
        p.press("left")

        print(f"Iteration number: {iter}; Time: {timePassed}mins.")
        iter += 1

        if resetCounter <= 0:
            resetCounter = 30

            print("Switching to another video")

            p.hotkey("ctrl", "l")
            time.sleep(5)
            p.typewrite(getRandomVideo())
            time.sleep(5)
            p.press("enter")
            time.sleep(5)
            p.hotkey("ctrl", "r")

            time.sleep(5)

            print("Playing the Video.")
            p.moveTo(
                math.floor(math.floor(SCREEN_SIZE[0] / 2)),
                math.floor(SCREEN_SIZE[1] / 3),
            )
            time.sleep(3)
            p.click()


if __name__ == "__main__":
    main()
