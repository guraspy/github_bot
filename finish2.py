import pyautogui as MI
import time
import math

MI.PAUSE = 0.1

def finish(kills, losses, x_algorithm_use_rate):
    print("FINDING X\n")

    time.sleep(0.3)


    if(MI.locateCenterOnScreen('images/low_victoryX.png',confidence = 0.85,)):
        kills = kills + 1
        print("\tBattle Result: Win")
        
    elif(MI.locateCenterOnScreen('images/low_defeatX.png',confidence = 0.85,)):
        losses = losses + 1
        print("\tBattle Result: Loss")

    MI.PAUSE = 0.001

    button_images = ['images/xButton/xbutton1.png', 'images/xButton/xbutton2.png',
                     'images/xButton/xbutton3.png', 'images/xButton/xbutton4.png',
                     'images/xButton/xbutton5.png', 'images/xButton/xbutton6.png',
                     'images/xButton/xbutton7.png', 'images/xButton/xbutton8.png',
                     'images/xButton/xbutton9.png', 'images/xButton/xbutton10.png',
                     'images/xButton/xbutton11.png', 'images/xButton/xbutton12.png',
                     'images/xButton/xbutton13.png', 'images/xButton/xbutton14.png',
                     'images/xButton/xbutton15.png', 'images/xButton/xbutton16.png',
                     'images/xButton/xbutton17.png', 'images/xButton/xbutton18.png',
                     'images/xButton/xbutton19.png', 'images/xButton/xbutton20.png',
                     'images/xButton/xbutton21.png', 'images/xButton/xbutton22.png',
                     'images/xButton/xbutton23.png', 'images/xButton/xbutton24.png',
                     'images/xButton/xbutton25.png', 'images/xButton/xbutton26.png',
                     'images/xButton/xbutton27.png', 'images/xButton/xbutton28.png',
                     'images/xButton/xbutton29.png', 'images/xButton/xbutton30.png',
                     'images/xButton/xbutton31.png', 'images/xButton/xbutton32.png',
                     'images/xButton/xbutton33.png', 'images/xButton/xbutton34.png',
                     'images/xButton/xbutton35.png', 'images/xButton/xbutton36.png',
                     'images/xButton/xbutton37.png', 'images/xButton/xbutton38.png',
                     'images/xButton/xbutton39.png', 'images/xButton/xbutton40.png',
                     'images/xButton/xbutton41.png', 'images/xButton/xbutton42.png',
                     'images/xButton/xbutton43.png', 'images/xButton/xbutton44.png',
                     'images/xButton/xbutton45.png',]


    for e, button_image_path in enumerate(button_images, start=1):

        x = MI.locateCenterOnScreen(button_image_path, confidence=0.6, grayscale=True, region=(400, 165, 400, 270))
        if x:
            MI.click(x)
        
        if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
            pass
        else:
            print("\n\tCorrect X button: {},60".format(e))
            return kills, losses,  x_algorithm_use_rate

    print("movida?")

    print("\nFailed with 65 confidence. Confidence -5")

    images_folder = "images/low_xButton/fail/" + "fail" + str(time.time()) + ".png"
    MI.screenshot(images_folder, region = (400, 150, 398, 300))

#     # X ALGORITHM #
#     ##################################################################################################################################
    y = 190
    x_algorithm_use_rate += 1
    for _ in range(20):
        x = 398
        y += 10
        for _ in range(40): 
            x += 10
                
            X = (x, y)
            MI.click(X)
            if(MI.locateCenterOnScreen('images/low_playerbubble.png',confidence = 0.7, region = (452, 410, 60, 60))):
                MI.click(605, 211)
    
                return kills, losses, x_algorithm_use_rate
#     ###################################################################################################################################


    print("\nFailed to find X button. Restart the program.")
    input()

    # x = MI.locateCenterOnScreen('images/xButton/xbutton1.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 1")
        
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     MI.click(x)
    #     print("\n\tCorrect X button: 1,60")
    #     return kills, losses,  x_algorithm_use_rate  
    # ##########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton2.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 2")
        
    # time.sleep(0.005)
                    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 2,60")
    #     return kills, losses,  x_algorithm_use_rate  
    # ###########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton3.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 3")
        
    # time.sleep(0.005)
                
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 3,60")
    #     return kills, losses,  x_algorithm_use_rate  
    # ############################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton4.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 4")
        
    # time.sleep(0.005)
                            
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 4,60")
    #     return kills, losses,  x_algorithm_use_rate  
    # ###############################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton5.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 5")
        
    # time.sleep(0.005)
                    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 5,60")
    #     return kills, losses,  x_algorithm_use_rate  
    # ##################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton6.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 6")
        
    # time.sleep(0.005)
                
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 6,60")
    #     return kills, losses,  x_algorithm_use_rate  
    # #####################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton7.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 7")
        
    # time.sleep(0.005)
                    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 7,60")
    #     return kills, losses,  x_algorithm_use_rate  
    # ####################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton8.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 8")
        
    # time.sleep(0.005)
                
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 8,60")
    #     return kills, losses,  x_algorithm_use_rate  
    # ###################################3
    # x = MI.locateCenterOnScreen('images/xButton/xbutton9.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 9")
        
    # time.sleep(0.005)
                    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 9,60")
    #     return kills, losses,  x_algorithm_use_rate  
    # #####################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton10.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 10")
        
    # time.sleep(0.005)
                
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 10,60")
    #     return kills, losses,  x_algorithm_use_rate  
    # ###########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton11.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 11")
        
    # time.sleep(0.005)
                            
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 11,60")
    #     return kills, losses,  x_algorithm_use_rate  
    # #############################################3
    # x = MI.locateCenterOnScreen('images/xButton/xbutton12.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 12")
        
    # time.sleep(0.005)
                    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 12,60")
    #     return kills, losses,  x_algorithm_use_rate  
    # #####################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton13.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 13")
        
    # time.sleep(0.005)
                
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 13,60")
    #     return kills, losses,  x_algorithm_use_rate  
    # ################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton14.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 14")
        
    # time.sleep(0.005)
                    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 14,60")
    #     return kills, losses,  x_algorithm_use_rate  
    # #####################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton15.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 15")
        
    # time.sleep(0.005)
                
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 15,60")
    #     return kills, losses,  x_algorithm_use_rate  
    # #####################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton16.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 16")
        
    # time.sleep(0.005)
                    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 16,60")
    #     return kills, losses,  x_algorithm_use_rate  
    # #########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton17.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 17")
        
    # time.sleep(0.005)
                
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 17,60")
    #     return kills, losses,  x_algorithm_use_rate  
    # ###########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton18.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 18")
        
    # time.sleep(0.005)
                            
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 18,60")
    #     return kills, losses,  x_algorithm_use_rate  
    # ################################################  
    # x = MI.locateCenterOnScreen('images/xButton/xbutton19.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 19")
        
    # time.sleep(0.005)
                    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 19,60")
    #     return kills, losses,  x_algorithm_use_rate  
    # ###############################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton20.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 20")
        
    # time.sleep(0.005)
                
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 20,60")
    #     return kills, losses,  x_algorithm_use_rate  
    # ################################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton21.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 21")
        
    # time.sleep(0.005)
                    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 21,60")
    #     return kills, losses,  x_algorithm_use_rate  
    # ################################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton22.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 22")
        
    # time.sleep(0.005)
                
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 22,60")
    #     return kills, losses,  x_algorithm_use_rate  
    # #####################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton23.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 23")
        
    # time.sleep(0.005)
                    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 23,60")
    #     return kills, losses,  x_algorithm_use_rate  
    # #########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton24.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 24")
        
    # time.sleep(0.005)
                
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 24,60")
    #     return kills, losses,  x_algorithm_use_rate  
    # ##############################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton25.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 25")
        
    # time.sleep(0.005)
                            
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 25,60")
    #     return kills, losses,  x_algorithm_use_rate  
    # #########################################################   
    # x = MI.locateCenterOnScreen('images/xButton/xbutton26.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 26")
        
    # time.sleep(0.005)
                    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 26,60")
    #     return kills, losses,  x_algorithm_use_rate  
    # ################################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton27.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 27")
        
    # time.sleep(0.005)
                
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button 27,60:")
    #     return kills, losses,  x_algorithm_use_rate  
    # ##########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton28.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 28")
        
    # time.sleep(0.005)
                
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 28,60")
    #     return kills, losses,  x_algorithm_use_rate  
    # ########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton29.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 29")
        
    # time.sleep(0.005)
                
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 29,60")
    #     return kills, losses,  x_algorithm_use_rate  
    # ########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton30.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 30")
        
    # time.sleep(0.005)
    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 30,60")
    #     return kills, losses,  x_algorithm_use_rate  
    # ########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton31.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 31")
        
    # time.sleep(0.005)
    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 31,60")
    #     return kills, losses,  x_algorithm_use_rate  
    # ########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton32.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 32")
        
    # time.sleep(0.005)
    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 32,60")
    #     return kills, losses,  x_algorithm_use_rate  
    # ########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton33.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 33")
        
    # time.sleep(0.005)
    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 33,60")
    #     return kills, losses,  x_algorithm_use_rate  
    # ########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton34.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 34")
        
    # time.sleep(0.005)
    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 34,60")
    #     return kills, losses,  x_algorithm_use_rate  
    # ########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton35.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 35")
        
    # time.sleep(0.005)
    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 35,60")
    #     return kills, losses,  x_algorithm_use_rate  
    # ########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton36.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 36")
        
    # time.sleep(0.005)
    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 36,60")
    #     return kills, losses,  x_algorithm_use_rate  
    # ########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton37.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 37")
        
    # time.sleep(0.005)
    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 37,60")
    #     return kills, losses,  x_algorithm_use_rate  
    # ########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton38.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 38")
        
    # time.sleep(0.005)
    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 38,60")
    #     return kills, losses,  x_algorithm_use_rate  
    # ########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton39.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 39")
        
    # time.sleep(0.005)
    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 39,60")
    #     return kills, losses,  x_algorithm_use_rate  
    # ########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton40.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 40")
        
    # time.sleep(0.005)
    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #             pass
    # else:
    #     print("\n\tCorrect X button: 40,60")
    #     return kills, losses,  x_algorithm_use_rate  
    # ########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton41.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 41")
        
    # time.sleep(0.005)
    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 41,60")
    #     return kills, losses,  x_algorithm_use_rate  
    # ########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton42.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 42")
        
    # time.sleep(0.005)
    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 42,60")
    #     return kills, losses,  x_algorithm_use_rate  
    # ########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton43.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 43")
        
    # time.sleep(0.005)
    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 43,60")
    #     return kills, losses,  x_algorithm_use_rate  
    # ########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton44.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 44")
        
    # time.sleep(0.005)
    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 44,60")
    #     return kills, losses,  x_algorithm_use_rate
    #  ########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton45.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 44")
        
    # time.sleep(0.005)
    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 45,60")
    #     return kills, losses,  x_algorithm_use_rate  
    #  ########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton46.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 44")
        
    # time.sleep(0.005)
    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 46,60")
    #     return kills, losses,  x_algorithm_use_rate  
    #  ########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton47.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 44")
        
    # time.sleep(0.005)
    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 47,60")
    #     return kills, losses,  x_algorithm_use_rate  
    #  ########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton48.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 44")
        
    # time.sleep(0.005)
    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 48,60")
    #     return kills, losses,  x_algorithm_use_rate  
    #  ########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton49.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 44")
        
    # time.sleep(0.005)
    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 49,60")
    #     return kills, losses,  x_algorithm_use_rate 
    #  ########################################
    
    # #############################################################################################
    # #############################################################################################

    # #############################################################################################

    # #############################################################################################
    # #############################################################################################
    # #############################################################################################
    # #############################################################################################
    # #############################################################################################
    # #############################################################################################
    # #############################################################################################
    # #############################################################################################
    # #############################################################################################
    # #############################################################################################
    # #############################################################################################
    # #############################################################################################
    # #############################################################################################
    # #############################################################################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton50.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 44")
        
    # time.sleep(0.005)
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 50,60")
    #     return kills, losses,  x_algorithm_use_rate 
    #     ########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton51.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 44")
        
    # time.sleep(0.005)
    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 51,60")
    #     return kills, losses,  x_algorithm_use_rate
    #     ########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton52.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 44")
        
    # time.sleep(0.005)
    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 52,60")
    #     return kills, losses,  x_algorithm_use_rate
    #     ########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton53.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 44")
        
    # time.sleep(0.005)
    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 53,60")
    #     return kills, losses,  x_algorithm_use_rate
    # ########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton54.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 44")
        
    # time.sleep(0.005)
    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 54,60")
    #     return kills, losses,  x_algorithm_use_rate
    # ########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton55.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 44")
        
    # time.sleep(0.005)
    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 55,60")
    #     return kills, losses,  x_algorithm_use_rate
    # ########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton56.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 44")
        
    # time.sleep(0.005)
    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 56,60")
    #     return kills, losses,  x_algorithm_use_rate
    #     ########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton57.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 44")
        
    # time.sleep(0.005)
    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 57,60")
    #     return kills, losses,  x_algorithm_use_rate
    #     ########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton58.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 44")
        
    # time.sleep(0.005)
    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 58,60")
    #     return kills, losses,  x_algorithm_use_rate   
    #     ########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton59.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 44")
        
    # time.sleep(0.005)
    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 59,60")
    #     return kills, losses,  x_algorithm_use_rate
    #     ########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton60.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 44")
        
    # time.sleep(0.005)
    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 60,60")
    #     return kills, losses,  x_algorithm_use_rate
    #     ########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton61.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 44")
        
    # time.sleep(0.005)
    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 61,60")
    #     return kills, losses,  x_algorithm_use_rate
    #     ########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton62.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 44")
        
    # time.sleep(0.005)
    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 62,60")
    #     return kills, losses,  x_algorithm_use_rate
    #     ########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton63.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 44")
        
    # time.sleep(0.005)
    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 63,60")
    #     return kills, losses,  x_algorithm_use_rate
    #     ########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton64.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 44")
        
    # time.sleep(0.005)
    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 64,60")
    #     return kills, losses,  x_algorithm_use_rate
    #     ########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton65.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 44")
        
    # time.sleep(0.005)
    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 65,60")
    #     return kills, losses,  x_algorithm_use_rate
    #     ########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton66.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 44")
        
    # time.sleep(0.005)
    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 66,60")
    #     return kills, losses,  x_algorithm_use_rate
    #     ########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton67.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 44")
        
    # time.sleep(0.005)
    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 67,60")
    #     return kills, losses,  x_algorithm_use_rate
    #     ########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton68.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 44")
        
    # time.sleep(0.005)
    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 68,60")
    #     return kills, losses,  x_algorithm_use_rate

    #     ########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton69.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 44")
        
    # time.sleep(0.005)
    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 69,60")
    #     return kills, losses,  x_algorithm_use_rate
    #      ########################################
    # x = MI.locateCenterOnScreen('images/xButton/xbutton70.png', confidence = 0.6, grayscale=True, region = (400, 165, 400, 270))
    # if(x):
    #     MI.click(x)
    #     #print("\tX Button Found 44")
        
    # time.sleep(0.005)
    
    # if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
    #     pass
    # else:
    #     print("\n\tCorrect X button: 70,60")
    #     return kills, losses,  x_algorithm_use_rate
    

    


""" 
    #######################################################################
    #######################################################################
    #######################################################################
    #######################################################################
    #######################################################################
    #######################################################################

    x = MI.locateCenterOnScreen('images/xButton/xbutton1.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 1")
        
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        MI.click(x)
        print("\n\tCorrect X button: 1,55")
        return kills, losses,  x_algorithm_use_rate  
    ##########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton2.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 2")
        
    time.sleep(0.005)
                    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 2,55")
        return kills, losses,  x_algorithm_use_rate  
    ###########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton3.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 3")
        
    time.sleep(0.005)
                
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 3,55")
        return kills, losses,  x_algorithm_use_rate  
    ############################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton4.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 4")
        
    time.sleep(0.005)
                            
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 4,55")
        return kills, losses,  x_algorithm_use_rate  
    ###############################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton5.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 5")
        
    time.sleep(0.005)
                    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 5,55")
        return kills, losses,  x_algorithm_use_rate  
    ##################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton6.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 6")
        
    time.sleep(0.005)
                
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 6,55")
        return kills, losses,  x_algorithm_use_rate  
    #####################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton7.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 7")
        
    time.sleep(0.005)
                    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 7,55")
        return kills, losses,  x_algorithm_use_rate  
    ####################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton8.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 8")
        
    time.sleep(0.005)
                
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 8,55")
        return kills, losses,  x_algorithm_use_rate  
    ###################################3
    x = MI.locateCenterOnScreen('images/xButton/xbutton9.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 9")
        
    time.sleep(0.005)
                    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 9,55")
        return kills, losses,  x_algorithm_use_rate  
    #####################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton10.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 10")
        
    time.sleep(0.005)
                
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 10,55")
        return kills, losses,  x_algorithm_use_rate  
    ###########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton11.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 11")
        
    time.sleep(0.005)
                            
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 11,55")
        return kills, losses,  x_algorithm_use_rate  
    #############################################3
    x = MI.locateCenterOnScreen('images/xButton/xbutton12.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 12")
        
    time.sleep(0.005)
                    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 12,55")
        return kills, losses,  x_algorithm_use_rate  
    #####################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton13.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 13")
        
    time.sleep(0.005)
                
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 13,55")
        return kills, losses,  x_algorithm_use_rate  
    ################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton14.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 14")
        
    time.sleep(0.005)
                    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 14,55")
        return kills, losses,  x_algorithm_use_rate  
    #####################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton15.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 15")
        
    time.sleep(0.005)
                
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 15,55")
        return kills, losses,  x_algorithm_use_rate  
    #####################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton16.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 16")
        
    time.sleep(0.005)
                    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 16,55")
        return kills, losses,  x_algorithm_use_rate  
    #########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton17.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 17")
        
    time.sleep(0.005)
                
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 17,55")
        return kills, losses,  x_algorithm_use_rate  
    ###########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton18.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 18")
        
    time.sleep(0.005)
                            
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 18,55")
        return kills, losses,  x_algorithm_use_rate  
    ################################################  
    x = MI.locateCenterOnScreen('images/xButton/xbutton19.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 19")
        
    time.sleep(0.005)
                    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 19,55")
        return kills, losses,  x_algorithm_use_rate  
    ###############################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton20.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 20")
        
    time.sleep(0.005)
                
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 20,55")
        return kills, losses,  x_algorithm_use_rate  
    ################################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton21.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 21")
        
    time.sleep(0.005)
                    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 21,55")
        return kills, losses,  x_algorithm_use_rate  
    ################################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton22.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 22")
        
    time.sleep(0.005)
                
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 22,55")
        return kills, losses,  x_algorithm_use_rate  
    #####################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton23.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 23")
        
    time.sleep(0.005)
                    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 23,55")
        return kills, losses,  x_algorithm_use_rate  
    #########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton24.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 24")
        
    time.sleep(0.005)
                
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 24,55")
        return kills, losses,  x_algorithm_use_rate  
    ##############################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton25.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 25")
        
    time.sleep(0.005)
                            
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 25,55")
        return kills, losses,  x_algorithm_use_rate  
    #########################################################   
    x = MI.locateCenterOnScreen('images/xButton/xbutton26.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 26")
        
    time.sleep(0.005)
                    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 26,55")
        return kills, losses,  x_algorithm_use_rate  
    ################################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton27.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 27")
        
    time.sleep(0.005)
                
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button 27,55:")
        return kills, losses,  x_algorithm_use_rate  
    ##########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton28.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 28")
        
    time.sleep(0.005)
                
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 28,55")
        return kills, losses,  x_algorithm_use_rate  
    ########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton29.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 29")
        
    time.sleep(0.005)
                
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 29,55")
        return kills, losses,  x_algorithm_use_rate  
    ########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton30.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 30")
        
    time.sleep(0.005)
    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 30,55")
        return kills, losses,  x_algorithm_use_rate  
    ########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton31.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 31")
        
    time.sleep(0.005)
    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 31,55")
        return kills, losses,  x_algorithm_use_rate  
    ########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton32.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 32")
        
    time.sleep(0.005)
    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 32,55")
        return kills, losses,  x_algorithm_use_rate  
    ########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton33.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 33")
        
    time.sleep(0.005)
    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 33,55")
        return kills, losses,  x_algorithm_use_rate  
    ########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton34.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 34")
        
    time.sleep(0.005)
    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 34,55")
        return kills, losses,  x_algorithm_use_rate  
    ########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton35.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 35")
        
    time.sleep(0.005)
    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 35,55")
        return kills, losses,  x_algorithm_use_rate  
    ########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton36.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 36")
        
    time.sleep(0.005)
    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 36,55")
        return kills, losses,  x_algorithm_use_rate  
    ########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton37.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 37")
        
    time.sleep(0.005)
    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 37,55")
        return kills, losses,  x_algorithm_use_rate  
    ########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton38.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 38")
        
    time.sleep(0.005)
    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 38,55")
        return kills, losses,  x_algorithm_use_rate  
    ########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton39.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 39")
        
    time.sleep(0.005)
    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 39,55")
        return kills, losses,  x_algorithm_use_rate  
    ########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton40.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 40")
        
    time.sleep(0.005)
    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
                pass
    else:
        print("\n\tCorrect X button: 40,55")
        return kills, losses,  x_algorithm_use_rate  
    ########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton41.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 41")
        
    time.sleep(0.005)
    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 41,55")
        return kills, losses,  x_algorithm_use_rate  
    ########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton42.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 42")
        
    time.sleep(0.005)
    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 42,55")
        return kills, losses,  x_algorithm_use_rate  
    ########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton43.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 43")
        
    time.sleep(0.005)
    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 43,55")
        return kills, losses,  x_algorithm_use_rate  
    ########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton44.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 44")
        
    time.sleep(0.005)
    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 44,55")
        return kills, losses,  x_algorithm_use_rate  

    x = MI.locateCenterOnScreen('images/xButton/xbutton45.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 44")
        
    time.sleep(0.005)
    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 45,55")
        return kills, losses,  x_algorithm_use_rate  
     ########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton46.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 44")
        
    time.sleep(0.005)
    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 46,55")
        return kills, losses,  x_algorithm_use_rate  
     ########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton47.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 44")
        
    time.sleep(0.005)
    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 47,55")
        return kills, losses,  x_algorithm_use_rate  
     ########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton48.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 44")
        
    time.sleep(0.005)
    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 48,55")
        return kills, losses,  x_algorithm_use_rate  
     ########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton49.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 44")
        
    time.sleep(0.005)
    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 49,55")
        return kills, losses,  x_algorithm_use_rate 
     ########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton50.png', confidence = 0.55, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 44")
        
    time.sleep(0.1)
    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 50,55")
        return kills, losses,  x_algorithm_use_rate    
    


    print("\nFailed with 55 confidence. Confidence -5")

    

    #################################################
    #######################################################
    ############################################################
    ##################################################################
    #################################################
    #######################################################
    ############################################################
    ##################################################################
    #################################################
    #######################################################
    ############################################################
    ##################################################################
    #################################################
    #######################################################
    ############################################################
    ##################################################################

    x = MI.locateCenterOnScreen('images/xButton/xbutton1.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 1")
        
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        MI.click(x)
        print("\n\tCorrect X button: 1,50")
        return kills, losses,  x_algorithm_use_rate  
    ##########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton2.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 2")
        
    time.sleep(0.005)
                    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 2,50")
        return kills, losses,  x_algorithm_use_rate  
    ###########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton3.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 3")
        
    time.sleep(0.005)
                
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 3,50")
        return kills, losses,  x_algorithm_use_rate  
    ############################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton4.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 4")
        
    time.sleep(0.005)
                            
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 4,50")
        return kills, losses,  x_algorithm_use_rate  
    ###############################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton5.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 5")
        
    time.sleep(0.005)
                    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 5,50")
        return kills, losses,  x_algorithm_use_rate  
    ##################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton6.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 6")
        
    time.sleep(0.005)
                
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 6,50")
        return kills, losses,  x_algorithm_use_rate  
    #####################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton7.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 7")
        
    time.sleep(0.005)
                    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 7,50")
        return kills, losses,  x_algorithm_use_rate  
    ####################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton8.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 8")
        
    time.sleep(0.005)
                
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 8,50")
        return kills, losses,  x_algorithm_use_rate  
    ###################################3
    x = MI.locateCenterOnScreen('images/xButton/xbutton9.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 9")
        
    time.sleep(0.005)
                    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 9,50")
        return kills, losses,  x_algorithm_use_rate  
    #####################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton10.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 10")
        
    time.sleep(0.005)
                
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 10,50")
        return kills, losses,  x_algorithm_use_rate  
    ###########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton11.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 11")
        
    time.sleep(0.005)
                            
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 11,50")
        return kills, losses,  x_algorithm_use_rate  
    #############################################3
    x = MI.locateCenterOnScreen('images/xButton/xbutton12.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 12")
        
    time.sleep(0.005)
                    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 12,50")
        return kills, losses,  x_algorithm_use_rate  
    #####################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton13.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 13")
        
    time.sleep(0.005)
                
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 13,50")
        return kills, losses,  x_algorithm_use_rate  
    ################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton14.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 14")
        
    time.sleep(0.005)
                    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 14,50")
        return kills, losses,  x_algorithm_use_rate  
    #####################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton15.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 15")
        
    time.sleep(0.005)
                
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 15,50")
        return kills, losses,  x_algorithm_use_rate  
    #####################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton16.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 16")
        
    time.sleep(0.005)
                    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 16,50")
        return kills, losses,  x_algorithm_use_rate  
    #########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton17.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 17")
        
    time.sleep(0.005)
                
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 17,50")
        return kills, losses,  x_algorithm_use_rate  
    ###########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton18.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 18")
        
    time.sleep(0.005)
                            
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 18,50")
        return kills, losses,  x_algorithm_use_rate  
    ################################################  
    x = MI.locateCenterOnScreen('images/xButton/xbutton19.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 19")
        
    time.sleep(0.005)
                    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 19,50")
        return kills, losses,  x_algorithm_use_rate  
    ###############################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton20.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 20")
        
    time.sleep(0.005)
                
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 20,50")
        return kills, losses,  x_algorithm_use_rate  
    ################################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton21.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 21")
        
    time.sleep(0.005)
                    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 21,50")
        return kills, losses,  x_algorithm_use_rate  
    ################################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton22.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 22")
        
    time.sleep(0.005)
                
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 22,50")
        return kills, losses,  x_algorithm_use_rate  
    #####################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton23.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 23")
        
    time.sleep(0.005)
                    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 23,50")
        return kills, losses,  x_algorithm_use_rate  
    #########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton24.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 24")
        
    time.sleep(0.005)
                
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 24,50")
        return kills, losses,  x_algorithm_use_rate  
    ##############################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton25.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 25")
        
    time.sleep(0.005)
                            
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 25,50")
        return kills, losses,  x_algorithm_use_rate  
    #########################################################   
    x = MI.locateCenterOnScreen('images/xButton/xbutton26.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 26")
        
    time.sleep(0.005)
                    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 26,50")
        return kills, losses,  x_algorithm_use_rate  
    ################################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton27.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 27")
        
    time.sleep(0.005)
                
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button 27,50:")
        return kills, losses,  x_algorithm_use_rate  
    ##########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton28.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 28")
        
    time.sleep(0.005)
                
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 28,50")
        return kills, losses,  x_algorithm_use_rate  
    ########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton29.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 29")
        
    time.sleep(0.005)
                
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 29,50")
        return kills, losses,  x_algorithm_use_rate  
    ########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton30.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 30")
        
    time.sleep(0.005)
    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 30,50")
        return kills, losses,  x_algorithm_use_rate  
    ########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton31.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 31")
        
    time.sleep(0.005)
    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 31,50")
        return kills, losses,  x_algorithm_use_rate  
    ########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton32.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 32")
        
    time.sleep(0.005)
    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 32,50")
        return kills, losses,  x_algorithm_use_rate  
    ########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton33.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 33")
        
    time.sleep(0.005)
    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 33,50")
        return kills, losses,  x_algorithm_use_rate  
    ########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton34.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 34")
        
    time.sleep(0.005)
    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 34,50")
        return kills, losses,  x_algorithm_use_rate  
    ########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton35.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 35")
        
    time.sleep(0.005)
    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 35,50")
        return kills, losses,  x_algorithm_use_rate  
    ########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton36.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 36")
        
    time.sleep(0.005)
    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 36,50")
        return kills, losses,  x_algorithm_use_rate  
    ########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton37.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 37")
        
    time.sleep(0.005)
    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 37,50")
        return kills, losses,  x_algorithm_use_rate  
    ########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton38.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 38")
        
    time.sleep(0.005)
    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 38,50")
        return kills, losses,  x_algorithm_use_rate  
    ########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton39.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 39")
        
    time.sleep(0.005)
    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 39,50")
        return kills, losses,  x_algorithm_use_rate  
    ########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton40.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 40")
        
    time.sleep(0.005)
    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
                pass
    else:
        print("\n\tCorrect X button: 40,50")
        return kills, losses,  x_algorithm_use_rate  
    ########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton41.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 41")
        
    time.sleep(0.005)
    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 41,50")
        return kills, losses,  x_algorithm_use_rate  
    ########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton42.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 42")
        
    time.sleep(0.005)
    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 42,50")
        return kills, losses,  x_algorithm_use_rate  
    ########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton43.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 43")
        
    time.sleep(0.005)
    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 43,50")
        return kills, losses,  x_algorithm_use_rate  
    ########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton44.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 44")
        
    time.sleep(0.005)
    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 44,50")
        return kills, losses,  x_algorithm_use_rate  
    ########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton45.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 44")
        
    time.sleep(0.005)
    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 44,50")
        return kills, losses,  x_algorithm_use_rate  
    ########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton46.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 44")
        
    time.sleep(0.005)
    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 44,50")
        return kills, losses,  x_algorithm_use_rate  
    ########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton47.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 44")
        
    time.sleep(0.005)
    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 44,50")
        return kills, losses,  x_algorithm_use_rate  
    ########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton48.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 44")
        
    time.sleep(0.005)
    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 44,50")
        return kills, losses,  x_algorithm_use_rate  
    ########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton49.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 44")
        
    time.sleep(0.005)
    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 44,50")
        return kills, losses,  x_algorithm_use_rate  
    ########################################
    x = MI.locateCenterOnScreen('images/xButton/xbutton50.png', confidence = 0.5, region = (400, 165, 400, 270))
    if(x):
        MI.click(x)
        #print("\tX Button Found 44")
        
    time.sleep(0.1)
    
    if(MI.pixelMatchesColor(633, 241, (224, 211, 118))):
        pass
    else:
        print("\n\tCorrect X button: 44,50")
        return kills, losses,  x_algorithm_use_rate  

    print("\nFailed with 50 confidence")
"""     
