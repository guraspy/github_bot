import pyautogui as MI
import groups as group
import time
import math
import low_finishBattle as CB
import random
import tkinter 


skype = False

warTime = True
killLimit = -1
maxBattles = -500

Human = False
NPCone = True
PMFlag = True
WCFlag = False

turns = 0

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
    time.sleep(0.3)
    MI.moveTo(600, 224)
    privateChat()

#Function for healing
def checkForHeal():
    notHeal = MI.locateCenterOnScreen('images/half_health.png', confidence = 0.90, region = (407, 170, 30, 15))
    if not notHeal:
        print("\t\tHealing\n")

        for _ in range(10):
            ##Medic
            MI.click(MI.locateCenterOnScreen('images/med_medicSkill.png', confidence = 0.80))
            time.sleep(0.2)


        mouseMove()
    privateChat()

##Function to check for PMS
def privateChat():

    global skype
    global PMFlag
    # PM messages
    statements_1 = ["hi", "hey", "good day", "hello", "yoo"]
    statements_2 = ["how are u", "how are you", "how are you doing?", "what's up?"]
    PM = MI.locateCenterOnScreen('images/skills/pm.png', confidence = 0.70, region = (730, 157, 50, 30))
    CHAT = MI.locateCenterOnScreen('images/skills/chat_x.png', confidence = 0.70, region=(612, 229, 20, 20))
    
    if((PM and PMFlag) or (CHAT and PMFlag)):

        print("We have received a PM")
        playerSS = "images/PMs/" + "PM_" + str(time.time()) + ".png"
        MI.screenshot(playerSS, region = (400,50,400,500))
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
def Boss():
    privateChat()

    if screen_width != 800 and screen_height != 600:
        print("Invalid resolution. Only 800x600 is supported.\t")


    PlayerFlag = False
    battleOver = False
    numPlayers = 0
    victory = False
        
    global Human
    global turns

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
        acatriel = MI.locateCenterOnScreen('images/acatriel.png', confidence= 0.7)

        if acatriel:
            
            found = True

        if(found):
            MI.click(acatriel)
            time.sleep(0.5)
            MI.click(451,238)

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
        
        elif(MI.locateCenterOnScreen('images/med_playerbubble.png', confidence = 0.70, region = (456,172,20,18))):
            privateChat()

            ##This statment continues to be run as long as we are alive or the battle is still going on 
            while(MI.locateCenterOnScreen('images/med_playerbubble.png', confidence = 0.70, region = (456,172,20,18))):
                battleOver = True
                MI.click(527,172)
                time.sleep(0.1)
                checkForHeal()

                if MI.locateCenterOnScreen('images/round.png', confidence = 0.9, region = (580, 249, 45, 20)):

                    # MI.click(MI.locateCenterOnScreen('images/maelstrom.png', confidence= 0.7))
                    # MI.click(MI.locateCenterOnScreen('images/cannon.png', confidence= 0.7))
                    # MI.click(MI.locateCenterOnScreen('images/fireball.png', confidence= 0.7))
                    MI.click(MI.locateCenterOnScreen('images/parasite.png', confidence= 0.7))
                    MI.click(MI.locateCenterOnScreen('images/infernal.png', confidence= 0.7))

                    no_mana = MI.locateCenterOnScreen('images/no_mana.png', confidence= 0.7, region = (724, 178, 65, 17))
                    if not no_mana:
                        MI.click(MI.locateCenterOnScreen('images/blood_shield.png', confidence= 0.7))

                    #bot
                    MI.click(701, 335)
                    
                    MI.click(MI.locateCenterOnScreen('images/frozen_rift.png', confidence= 0.7))

                    MI.click(MI.locateCenterOnScreen('images/gate.png', confidence= 0.7))

                    MI.click(MI.locateCenterOnScreen('images/focus_fury.png', confidence= 0.7))

                    #gun  
                    MI.click(497, 336)

                    #aux
                    MI.click(585, 337)  

                    # MI.click(MI.locateCenterOnScreen('images/fireball.png', confidence= 0.7))

 
                    MI.click(MI.locateCenterOnScreen('images/shield.png', confidence= 0.7))

                  

                    mouseMove()

        else:
            drop = MI.locateCenterOnScreen('images/med_continue.png', confidence = 0.90, region = (561,338,200,65))
            if(drop):
                    MI.click(drop)

            if(battleOver):
                if(MI.locateCenterOnScreen('images/med_didYouKnow.png',confidence = 0.7, region = (426, 383, 53, 49))):
                    
                    kills, losses, x_algorithm_use_rate = CB.finish(kills, losses, x_algorithm_use_rate)
                    # if kills < 0 and losses < 0:
                    #     print("X undetected")
                    #     return
                    # MI.click(605, 211)
                    # MI.click(605, 211)
                    # group.battleDone()
                    
                    if numBattles == 0:
                        kills = losses = 0 
                    Human = False
                    battleOver = False
                    newTime = time.time()
                    if numBattles > 0:
                        battleStats(numBattles, kills, losses, newTime, startingTime, overallTime, x_algorithm_use_rate)
                    turns = 0

                    #if we get pm program will close after battle
                    if not PMFlag:
                        exit()
            



#Show stats at the end of the battle
def battleStats(numBattles, kills, losses, newTime, startingTime, overallTime, x_algorithm_use_rate):
    global turns
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



Boss()
