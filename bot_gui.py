import pyautogui as MI
import time
import math
import low_finishBattle as CB
import finish2 
import random
import tkinter as tk
import threading

NPCone = True
PMFlag = True
need_war_core = False

root = tk.Tk()


MI.Pause = 0.001

print("STARTING\n")


    
def log(message):
    terminal.insert(tk.END, message + "\n")
    terminal.see(tk.END)
    
running = False  # Global variable to control the bot

def start_bot():
    global running
    if not running:
        running = True
        log("Bot started.")
        threading.Thread(target=main, daemon=True).start()
        
def stop_bot():
    global running
    running = False
    log("Bot stopped.")
    
def enter_value():
    value = int_input.get()
    terminal.insert(tk.END, f"Program will stop after {value} battles:\n")

root.title("JUGGERNAUT BOT")
root.geometry("400x300")

frame = tk.Frame(root)
frame.pack(expand=True, fill="both", padx=10, pady=10)

# First line: label + input + enter button
row1 = tk.Frame(frame)
row1.pack(pady=5)

tk.Label(row1, text="How many juggernauts to play:").pack(side="left", padx=5)

int_input = tk.Entry(row1, width=10)
int_input.pack(side="left", padx=5)

btn_enter = tk.Button(row1, text="Enter", command=enter_value)
btn_enter.pack(side="left", padx=5)

# Second line: start + stop buttons
row2 = tk.Frame(frame)
row2.pack(pady=5)

btn_start = tk.Button(row2, text="Start", command=start_bot)
btn_start.pack(side="left", padx=10)

btn_stop = tk.Button(row2, text="Stop", command=stop_bot)
btn_stop.pack(side="left", padx=10)

# Terminal output
terminal = tk.Text(frame, height=12)
terminal.pack(expand=True, fill="both", pady=10)

root.mainloop()

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

#Function to move mouse after we click everything
def mouseMove():
    MI.moveTo(600, 224)
    privateChat()
    
#Main 
def main():
    global running
    privateChat()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    if screen_width != 800 and screen_height != 600:
        log("Invalid resolution. Only 800x600 is supported.\t")

    battleOver = False
    numBattles = 0
    kills = 0
    losses = 0
    x_algorithm_use_rate = 0

    ##For timing purposes
    startingTime = overallTime = time.time()

    ##Loop for doing jugg battles
    while(running):
        privateChat()
        
        ##Checks to see if we are out of battle and the jugg button is available
        jugg = MI.locateCenterOnScreen('images/med_jug.png', confidence = 0.75)
        if(jugg):

            objective = MI.locateCenterOnScreen('images/turret.png', confidence=0.7)
            if(objective):
                MI.click(objective)
                time.sleep(1.5)
                MI.click(724, 322)
                MI.click(533, 267)

            ##Enters the jugg battle
            numBattles = numBattles + 1
            MI.click(jugg)

            time.sleep(1)

            ##In case of lag, keeps pressing the jugg battle as long as we see it (until we enter)

            jugg = MI.locateCenterOnScreen('images/med_jug.png', confidence = 0.7)
            while(jugg):
                print("jug dainaxa")
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

                    #multi
                    MI.click(MI.locateCenterOnScreen('images/multi-shot.png', confidence = 0.7))
                    MI.click(MI.locateCenterOnScreen('images/med_rain.png', confidence = 0.7))

                    # #bot
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


# main()

