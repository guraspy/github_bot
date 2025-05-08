import pyautogui as MI
import groups as group
import time
import math
import low_finishBattle as CB
import finish2 
import random
import tkinter 


warTime = True
killLimit = -1
maxBattles = -500

Human = False
NPCone = True
PMFlag = True
need_war_core = False

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
    MI.moveTo(600, 224)
    privateChat()


#Function for healing
def checkForHeal():
    # notHeal = MI.locateCenterOnScreen('images/med_health.png', confidence = 0.90, region = (700, 170, 99, 15))
    # if not notHeal:
    #     print("\t\tHealing\n")

    #     ##HP Booster
    #     # MI.click(759, 336)

    #     ##Medic
    #     MI.click(MI.locateCenterOnScreen('images/med_medicSkill.png', confidence = 0.80))

    #     mouseMove()
    # privateChat()
    pass


##Function to check for PMS
def privateChat():

    global PMFlag
    # PM messages
    statements_1 = ["hi", "hey", "good day", "hello", "yoo"]
    statements_2 = ["how are u", "how are you", "how are you doing?", "what's up?"]
    PM = MI.locateCenterOnScreen('images/skills/pm.png', confidence = 0.70, region = (730, 157, 50, 30))
    CHAT = MI.locateCenterOnScreen('images/skills/chat_x.png', confidence = 0.70, region=(612, 229, 20, 20))
    
    if((PM and PMFlag) or (CHAT and PMFlag)):

        print("We have received a PM")
        playerSS = "images/PMs/" + "PM_" + str(time.time()) + ".png"
        MI.screenshot(playerSS, region = (400,50,400,100))
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


# def war_com():
#     global need_war_core
#     print("shmodis")
#     war_core = MI.locateCenterOnScreen('images/war_commander.png', confidence = 0.90, region = (717, 185, 80, 18))
#     if not war_core:
#         print("need_war_core = True")
#         need_war_core = True


# def insert():
#     global need_war_core
    
#     print("while")
#     time.sleep(2)
#     inventory = MI.locateCenterOnScreen('images/inventory.png', confidence = 0.9, region=(408,158,383,330))
#     while(not inventory):
#         print("while1")
#         MI.click(inventory)
#     time.sleep(2)
#     core_slot = MI.locateCenterOnScreen('images/core_slot.png', confidence = 0.7, region=(408,158,383,330))
#     while(not core_slot): 
#         print("while2")
#         MI.click(core_slot)
#     time.sleep(2)
#     search = MI.locateCenterOnScreen('images/inventory_search.png', confidence = 0.7, region=(707, 263, 83, 25))
#     while(not search):
#         print("while3")
#         MI.click(search)
#     time.sleep(2)
#     time.sleep(1)
#     MI.typewrite("war")
#     time.sleep(0.1)
#     MI.click(746,297)
#     time.sleep(0.1)
#     time.sleep(2)
#     insert1 = MI.locateCenterOnScreen('images/insert.png', confidence = 0.7, region=(408,158,383,330))
#     while(not insert1):
#         print("while4")
#         MI.click(insert1)
#     time.sleep(2)
#     insert2 = MI.locateCenterOnScreen('images/insert_2.png', confidence = 0.7, region=(408,158,383,330))
#     while(not insert2):
#         print("while5")
#         MI.click(insert2)
#     time.sleep(2)
#     x = MI.locateCenterOnScreen('images/x.png', confidence = 0.7, region=(408,158,383,330))
#     while(not x):
#         print("while6")
#         MI.click(x)
#     time.sleep(2)
#     jugg = MI.locateCenterOnScreen('images/med_jug.png', confidence = 0.7, region = (600, 400, 100, 100))
#     if(jugg):
#         need_war_core = False


#Main 
def Juggernaut():
    privateChat()

    if screen_width != 800 and screen_height != 600:
        print("Invalid resolution. Only 800x600 is supported.\t")

    # rain = MI.locateCenterOnScreen('images/skills/rain.png', confidence = 0.45, region=(1018,666,900,100))
    # bot = MI.locateCenterOnScreen('images/skills/botanic.png', confidence = 0.9)
    # gun = MI.locateCenterOnScreen('images/skills/gun.png', confidence = 0.9)
    # aux = MI.locateCenterOnScreen('images/skills/auxiliary.png', confidence = 0.9)

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
        

        ##Checks to see if we are out of battle and the jugg button is available
        jugg = MI.locateCenterOnScreen('images/med_jug.png', confidence = 0.7, region = (600, 400, 100, 100))
        if(jugg):
            
            ##Searches for a war objective before we enter a battle and drops bomb if there is one
            #WARR

            # '''WAR BIO'''
            # objective = MI.locateCenterOnScreen('images/WAR_BIO_2.png', confidence = 0.70)

            '''WAR BIO'''
            # objective = MI.locateCenterOnScreen('images/WAR_BIO.png', confidence = 0.70)

            # '''WAR WEST NAVAL YARD'''
            # objective = MI.locateCenterOnScreen('images/WEST_NAVAL_MIDDLE.png', confidence = 0.70)

            objective = MI.locateCenterOnScreen('images/turret.png', confidence=0.7)
            if(objective):
                MI.click(objective)
                time.sleep(1.5)
                MI.click(724, 322)
                MI.click(533, 267)

            # objective = MI.locateCenterOnScreen('images/obj_out_2.png', confidence=0.7)
            # if(objective):
            #     MI.click(objective)
            #     time.sleep(1.5)
            #     MI.click(533, 267)
            #     MI.click(724, 322)
            # objective = MI.locateCenterOnScreen('images/obj_out_3.png', confidence=0.7)
            # if(objective):
            #     MI.click(objective)
            #     time.sleep(1.5)
            #     MI.click(533, 267)
            #     MI.click(724, 322)
            

            ##Enters the jugg battle
            numBattles = numBattles + 1
            MI.click(jugg)

            time.sleep(1)

            ##In case of lag, keeps pressing the jugg battle as long as we see it (until we enter)

            jugg = MI.locateCenterOnScreen('images/med_jug.png', confidence = 0.7, region = (621, 407, 100, 100))
            jugg_stuck = MI.locateCenterOnScreen('images/med_jug_stuck.png', confidence = 0.6, region = (569, 412, 42, 12))
            while(jugg or jugg_stuck):
                MI.click(jugg)
                MI.click(630, 419)
                time.sleep(0.25)
                jugg = MI.locateCenterOnScreen('images/med_jug.png', confidence = 0.7, region = (621, 407, 100, 100))
                jugg_stuck = MI.locateCenterOnScreen('images/med_jug_stuck.png', confidence = 0.6, region = (569, 412, 42, 12))


            
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
        elif(MI.locateCenterOnScreen('images/med_playerbubble.png', confidence = 0.70, region = (760, 168, 35, 36))):
            privateChat()
            # war_com()


            ##This statment continues to be run as long as we are alive or the battle is still going on 
            while(MI.locateCenterOnScreen('images/med_playerbubble.png', confidence = 0.70, region = (760, 168, 35, 36))):
                battleOver = True
                time.sleep(0.1)

                if MI.locateCenterOnScreen('images/med_strike.png', confidence = 0.9):
                    checkForHeal()
                    privateChat()
                    time.sleep(0.1)


                    #bh multi
                    MI.click(MI.locateCenterOnScreen('images/multi-shot.png', confidence = 0.7, region=(408,158,383,330)))

                    #armor core
                    MI.click(755, 339)

                    # #bot
                    # MI.click(701, 335)

                    #static granade
                    MI.click(MI.locateCenterOnScreen('images/static_granade.png', confidence = 0.7, region=(408,158,383,330)))
                    time.sleep(0.05)

                    # primary core
                    MI.click(471, 335)

                    #gun  
                    MI.click(497, 336)  

                    #aux
                    MI.click(585, 337)  

                    mouseMove()

                    #attack
                    MI.click(570, 304)

                    #target location
                    MI.click(453,313)
                    MI.click(490,281)
                    # MI.click(467,341)
                    # MI.click(433,324)
                    # MI.click(461,311)
                    # MI.click(485,307)
                    # MI.click(511,301)

                    #bot
                    # MI.click(701, 335)
                    #cannon 
                    # MI.click(MI.locateCenterOnScreen('images/cannon_800_med.png', confidence= 0.7, region=(408,158,383,330)))
                    # mouseMove()

        else:
            privateChat()
            _continue = MI.locateCenterOnScreen('images/med_continue.png', confidence = 0.90, region = (561,338,200,65))
            if(_continue):
                    MI.click(_continue)
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
                    group.battleDone()
                    
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
            
            # if need_war_core:
                # insert()


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



Juggernaut()