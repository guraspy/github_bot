import time
import pyautogui as MI
import keyboard

#press "L" to get postion

while True:
    if keyboard.is_pressed('l'):
        X, Y = MI.position()
        print(MI.position())
        pix = MI.pixel(X ,Y)
        print(pix)
        time.sleep(0.5)
    elif keyboard.is_pressed('p'):
        MI.click(690, 300)
        time.sleep(0.3)
        MI.click(510, 290)
    

    


