import keyboard
import mouse

from time import sleep

on = False


def main():
    while True:
        if keyboard.is_pressed("c"):
            IsOn()
        elif keyboard.is_pressed("o"):
            quit()
        elif on == True:
            sleep(0.07)
            mouse.double_click()


def IsOn():
    global on 
    if on == False:
        on = True
    else:
        on = False



if __name__ == "__main__":
    main()