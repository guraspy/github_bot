import pyautogui as MI
import time
import finish2 

jugg = MI.locateCenterOnScreen('images/med_jug.png', confidence = 0.7)
MI.moveTo(jugg.x, jugg.y)
# while True:
#     time.sleep(2)
#     MI.click(499, 290)
#     time.sleep(1)

#     MI.click(457, 204)
#     time.sleep(5)

#     MI.click(571, 302)
#     time.sleep(5)

#     images_folder = "images/low_xButton/" + "fail" + str(time.time()) + ".png"
#     time.sleep(2)
#     MI.screenshot(images_folder)
#     kills=0
#     losses=0
#     x_algorithm_use_rate=0
#     kills, losses, x_algorithm_use_rate = finish2.finish(kills, losses, x_algorithm_use_rate)