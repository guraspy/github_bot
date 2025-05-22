import pyautogui as MI
import time
import math
# import low_finishBattle as CB
import finish2 
import random
import tkinter as tk


NPCone = True
PMFlag = True
need_war_core = False

root = tk.Tk()
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
        
        ##Checks to see if we are out of battle and the jugg button is available
        jugg = MI.locateCenterOnScreen('images/med_jug.png', confidence = 0.75)
        if(jugg):

            turret = MI.locateCenterOnScreen('images/turret.png', confidence=0.7)
            if(turret):
                MI.click(turret)
                time.sleep(1)
                
                #super bomb
                MI.click(690, 300)
                time.sleep(0.3)
                
                #small bomb
                MI.click(510, 290)
                time.sleep(0.3)
                

            ##Enters the jugg battle
            numBattles = numBattles + 1
            MI.click(jugg)

            time.sleep(1)

            ##In case of lag, keeps pressing the jugg battle as long as we see it (until we enter)

            jugg = MI.locateCenterOnScreen('images/med_jug.png', confidence = 0.7)
            while(jugg):
                MI.click(jugg)
                MI.click(630, 419)
                time.sleep(0.25)
                jugg = MI.locateCenterOnScreen('images/med_jug.png', confidence = 0.7)
                # jugg_stuck = MI.locateCenterOnScreen('images/med_jug_stuck.png', confidence = 0.6)

            if(numBattles == 1):
                startingTime = overallTime = time.time()
            else:
                startingTime = time.time()

            print("Battle -", numBattles,"\t")
            time.sleep(5)
            privateChat()
            time.sleep(5)
            privateChat()

        ##If we are in a juggernaut battle
        elif(MI.locateCenterOnScreen('images/med_playerbubble.png', confidence = 0.70, region = (690, 130, 105, 130))):
            privateChat()

            ##This statment continues to be run as long as we are alive or the battle is still going on 
            while(MI.locateCenterOnScreen('images/med_playerbubble.png', confidence = 0.70, region = (690, 130, 105, 130))):
                battleOver = True
                time.sleep(0.1)

                if MI.locateCenterOnScreen('images/med_strike.png', confidence = 0.9):
                    privateChat()
                    time.sleep(0.1)
                    
                    #AUX CORE
                    MI.click(644, 337)
                    
                    #multi
                    MI.click(MI.locateCenterOnScreen('images/multi-shot.png', confidence = 0.7))
                    MI.click(MI.locateCenterOnScreen('images/med_rain.png', confidence = 0.7))

                    #PISTOL CORE
                    MI.click(553, 337)

                    ##bot
                    MI.click(701, 335)
                    
                    #gun  
                    MI.click(497, 336) 

                    #aux
                    MI.click(585, 337)  

                    #attack
                    MI.click(570, 304)

                    mouseMove()

                    #target location
                    MI.click(453,313)
                    MI.click(490,281)


        elif battleOver == True:
            privateChat()
            time.sleep(2)
            MI.click(598, 350)
            if(battleOver):
                if(MI.locateCenterOnScreen('images/V.png', confidence=0.7) 
                    or (MI.locateCenterOnScreen('images/low_defeatX.png',confidence=0.7)) 
                    or (MI.locateCenterOnScreen('images/hand.png',confidence=0.7))):

            # if(MI.locateCenterOnScreen('images/finish.png',confidence = 0.7, region = (493, 239, 47, 138))):
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