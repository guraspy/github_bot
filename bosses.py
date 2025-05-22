import pyautogui as MI
import time
import math
import low_finishBattle as CB
import finish2 
import random
import tkinter 


NPCone = True
PMFlag = True
need_war_core = False

root = tkinter.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

MI.Pause = 0.001

print("STARTING IN") 
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("STARTING\n")


#Function to move mouse after we click everything
def mouseMove():
    MI.moveTo(600, 224)
    privateChat()

#Function for healing
def checkForHeal():
    notHeal = MI.locateCenterOnScreen('images/med_health.png', confidence = 0.90, region = (407, 170, 99, 15))
    if not notHeal:
        print("\t\tHealing\n")

        for _ in range(10):
            ##Medic
            MI.click(MI.locateCenterOnScreen('images/med_medicSkill.png', confidence = 0.60))
            time.sleep(0.2)


        mouseMove()
    privateChat()

##Function to check for PMS
def privateChat():

    global PMFlag
    # PM messages
    statements_1 = ["hi", "hey", "good day", "hello", "yoo"]
    statements_2 = ["how are u", "how are you", "how are you doing?", "what's up?"]
    PM = MI.locateCenterOnScreen('images/skills/pm.png', confidence = 0.70)
    CHAT = MI.locateCenterOnScreen('images/skills/chat_x.png', confidence = 0.70)
    
    if((PM and PMFlag) or (CHAT and PMFlag)):

        print("We have received a PM")
        playerSS = "images/PMs/" + "PM_" + str(time.time()) + ".png"
        MI.screenshot(playerSS)
        if PM:
            MI.click(PM)
        if((PM and PMFlag) or (CHAT and PMFlag)):
            time.sleep(1)
            MI.click(544, 300)
            time.sleep(3)
            MI.typewrite(random.choice(statements_1), interval=0.15)
            MI.hotkey("enter")
            time.sleep(5)
            MI.typewrite(random.choice(statements_2), interval=0.15)
            MI.hotkey("enter")
            MI.click(606, 244)
            PMFlag = False


#Main 
def main():
    privateChat()

    if screen_width != 800 and screen_height != 600:
        print("Invalid resolution. Only 800x600 is supported.\t")

    battleOver = False
    numBattles = 0
    kills = 0
    losses = 0
    x_algorithm_use_rate = 0

    ##For timing purposes
    startingTime = overallTime = time.time()

    ##Loop for doing jugg battles
    while(True):
        privateChat()
        found = False

        BIG_TUNA = MI.locateCenterOnScreen('images/big_tuna.png', confidence = 0.7)
        GEORGE_LOWE = MI.locateCenterOnScreen('images/george_lowe.png', confidence = 0.7)
        ELITE_YETI = MI.locateCenterOnScreen('images/elite_yeti.png', confidence = 0.7)
        BLACK_ABYSS = MI.locateCenterOnScreen('images/black_abyss.png', confidence = 0.7)
        CAPTAIN_SHOGGOTH = MI.locateCenterOnScreen('images/captain_shog.png', confidence = 0.7)
        ZEDMYR = MI.locateCenterOnScreen('images/zedmyr.png', confidence = 0.7)
        # THEON = MI.locateCenterOnScreen('images/theon.png', confidence = 0.7)
        NORAGH = MI.locateCenterOnScreen('images/noragh.png', confidence = 0.7)
        ALYDRIAH = MI.locateCenterOnScreen('images/alydriah.png', confidence = 0.7)
        REVONTHEUS = MI.locateCenterOnScreen('images/revontheus.png', confidence = 0.7)
        DAVARRIL = MI.locateCenterOnScreen('images/davarril.png', confidence = 0.7)
        ENDLESS = MI.locateCenterOnScreen('images/endless.png', confidence = 0.7)
        GOD_OF_WAR =  MI.locateCenterOnScreen('images/god_of_war.png', confidence = 0.7)
        DRAVAX_THE_HARBINGER = MI.locateCenterOnScreen('images/dravax_the.png', confidence = 0.7)
        CHAIRMAN_PLATINUM = MI.locateCenterOnScreen('images/chairman.png', confidence = 0.7)
        KARTHERAX = MI.locateCenterOnScreen('images/kartherax.png', confidence = 0.7)
        EDGAR_BOOTHE = MI.locateCenterOnScreen('images/edgar_bothe.png', confidence = 0.7)
        SAEVA_LIONHART = MI.locateCenterOnScreen('images/saeva_lionhart.png', confidence = 0.7)


        if BIG_TUNA:
            x1 = 705
            y1 = 288
            x2 = 442
            y2 = 223
            found = True
        elif GEORGE_LOWE:
            x1 = 598
            y1 = 280
            x2 = 454
            y2 = 202
            found = True
        elif ELITE_YETI:
            x1 = 709
            y1 = 307    
            x2 = 463
            y2 = 206
            found = True
        elif BLACK_ABYSS:
            x1 = 601
            y1 = 247
            x2 = 464
            y2 = 205
            found = True
        elif CAPTAIN_SHOGGOTH:
            x1 = 515
            y1 = 270
            x2 = 459
            y2 = 203
            found = True
        elif ZEDMYR:
            x1 = 715
            y1 = 358
            x2 = 460
            y2 = 225
            found = True
        # elif THEON:
        #     x1 = 535
        #     y1 = 298
        #     x2 = 465
        #     y2 = 220
        #     found = True
        elif NORAGH:
            x1 = 587
            y1 = 303
            x2 = 447
            y2 = 203
            found = True
        elif ALYDRIAH:
            x1 = 517
            y1 = 305
            x2 = 451
            y2 = 204
            found = True
        elif REVONTHEUS:
            x1 = 711
            y1 = 283
            x2 = 460
            y2 = 223
            found = True
        elif DAVARRIL:
            x1 = 463
            y1 = 279
            x2 = 461
            y2 = 206
            found = True
        elif ENDLESS:
            x1 = 569    
            y1 = 278
            x2 = 477
            y2 = 220
            found = True
        elif GOD_OF_WAR:
            x1 = 446
            y1 = 282
            x2 = 451
            y2 = 203
            found = True
        elif DRAVAX_THE_HARBINGER:
            x1 = 547
            y1 = 277
            x2 = 467
            y2 = 207
            found = True
        elif CHAIRMAN_PLATINUM:
            x1 = 547
            y1 = 297
            x2 = 466
            y2 = 206
            found = True
        elif KARTHERAX:
            x1 = 755
            y1 = 265
            x2 = 460
            y2 = 207
            found = True
        elif EDGAR_BOOTHE:
            x1 = 466
            y1 = 299
            x2 = 450
            y2 = 222
            found = True
        elif SAEVA_LIONHART:
            x1 = 611
            y1 = 261
            x2 = 457
            y2 = 205
            found = True
        

        if(found):
            MI.click(x1,y1)
            time.sleep(0.5)
            MI.click(x2,y2)

            ##Enters the battle
            numBattles = numBattles + 1

            if(numBattles == 1):
                startingTime = overallTime = time.time()
            else:
                startingTime = time.time()

            print("Battle -", numBattles,"\t")
            time.sleep(5)
            privateChat()
            ELITE_YETI = None
        
        elif(MI.locateCenterOnScreen('images/med_playerbubble.png', confidence = 0.70, region = (400, 150, 80, 70))):
            privateChat()

            ##This statment continues to be run as long as we are alive or the battle is still going on 
            while(MI.locateCenterOnScreen('images/med_playerbubble.png', confidence = 0.70, region = (400, 150, 80, 70))):
                battleOver = True
                checkForHeal()

                if MI.locateCenterOnScreen('images/med_strike.png', confidence = 0.9):

                    MI.click(MI.locateCenterOnScreen('images/cannon.png', confidence= 0.8))
                    MI.click(MI.locateCenterOnScreen('images/maelstrom.png', confidence= 0.8))
                    # MI.click(MI.locateCenterOnScreen('images/fireball.png', confidence= 0.8))
                    MI.click(MI.locateCenterOnScreen('images/parasite.png', confidence= 0.8))

                    #bot
                    MI.click(701, 335)
                    
                    MI.click(MI.locateCenterOnScreen('images/frozen_rift.png', confidence= 0.8))

                    MI.click(MI.locateCenterOnScreen('images/gate.png', confidence= 0.8))

                    MI.click(MI.locateCenterOnScreen('images/focus_fury.png', confidence= 0.8))

                    #gun  
                    MI.click(497, 336)  

                    #aux
                    MI.click(585, 337)  

                    #attack
                    MI.click(570, 304)
                    mouseMove()

        elif battleOver == True:
            print("aq movidaaaa?")
            privateChat()
            time.sleep(2)
            MI.click(598, 350)
            if(battleOver):
                if(MI.locateCenterOnScreen('images/V.png', confidence=0.7) 
                    or (MI.locateCenterOnScreen('images/low_defeatX.png',confidence=0.7)) 
                    or (MI.locateCenterOnScreen('images/hand.png',confidence=0.7))):
                    
                    kills, losses, x_algorithm_use_rate = finish2.finish(kills, losses, x_algorithm_use_rate)
                    if kills < 0 and losses < 0:
                        print("X undetected")
                        return
                    MI.click(605, 211)
                    MI.click(605, 211)
                    
                    if numBattles == 0:
                        kills = losses = 0 
                    battleOver = False
                    newTime = time.time()
                    if numBattles > 0:
                        battleStats(numBattles, kills, losses, newTime, startingTime, overallTime, x_algorithm_use_rate)

                    #if we get pm program will close after battle
                    if not PMFlag:
                        exit()


#Show stats at the end of the battle
def battleStats(numBattles, kills, losses, newTime, startingTime, overallTime, x_algorithm_use_rate):
    print("\n\tBattle Stats:\n") 
    print("\tWins:",kills,"Losses:",losses,"\n")          
    # print("\tLosses:",losses,"\n")
    if kills or losses > 1:
        print("\tWin Percent:", round((kills/(losses+kills))*100, 1),"\n")
    print("\tPer hour wins with this time:", round(3600/(newTime - startingTime), 2), "\n")
    print("\tBattle time:", round(newTime - startingTime, 2),"second(s)\n")
    if(numBattles>1):
        print("\tAverage battle time:", round((newTime - overallTime)/numBattles, 2), "second(s)\n")
        if kills > 1:
            print("\tWins per hour:", round(3600/((newTime - overallTime)/kills), 2), "\n")
        print("\tTime spent battling:", math.floor((newTime - overallTime)/3600), "H and",
                                     round(((newTime - overallTime)%3600)/60, 2), "M \n")
    else:
        print("\tTime spent battling:", round(newTime - overallTime, 2), "second(s)\n\n")
    print("\tFailed to find X:", x_algorithm_use_rate,"times\n")


main()