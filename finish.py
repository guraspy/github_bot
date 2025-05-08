import cv2
import pyautogui as pa
import numpy as np
import time

def finish(kills, losses, x_algorithm_use_rate):
    print("FINDING X\n")
    time.sleep(0.3)

    button_images = ['images/xButton/xbutton1.png', 'images/xButton/xbutton2.png',
                     'images/xButton/xbutton3.png', 'images/xButton/xbutton4.png',
                     'images/xButton/xbutton5.png', 'images/xButton/xbutton6.png',
                     'images/xButton/xbutton7.png']

    for i, button_image_path in enumerate(button_images, start=1):
        button_image = cv2.imread(button_image_path, cv2.IMREAD_GRAYSCALE)
        template_size = button_image.shape[::-1]

        x = pa.locateCenterOnScreen(button_image_path, confidence=0.6, grayscale=True, region=(400, 165, 400, 270))
        if x:
            pa.click(x)
            # print("X Button Found", i)
        
        time.sleep(0.005)
        
        if not pa.pixelMatchesColor(633, 241, (224, 211, 118)):
            print("\n\tCorrect X button:", i, "60")
            return kills, losses, x_algorithm_use_rate

    return kills, losses, x_algorithm_use_rate