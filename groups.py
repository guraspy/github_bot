import pyautogui as MI
import time

MI.PAUSE = 0.001

group1Strike = True
group5Strike = True
groupBCore = True
groupCCore = True
groupDCore = True

# def groupA(name, coords, NPCone):
#     global static
#     global group1Strike

#     ##Aux
#     MI.click(1406, 626)

#     ##Bot
#     MI.click(1679, 627)

#     ##Rain
#     MI.click(MI.locateCenterOnScreen('images/skills/rain.png', confidence = 0.45, region=(1024,674,645,738)))

#     ##Gun
#     MI.click(1196, 625)

#     ##Strike
#     MI.click(1428, 548)

#     ##Attack
#     MI.click(coords)
    
def attack(coords):

    time.sleep(0.1)

    if MI.locateCenterOnScreen('images/skills/rain.png', confidence = 0.45, region=(1024,674,645,738)):

        ##Rain
        MI.click(MI.locateCenterOnScreen('images/skills/rain.png', confidence = 0.45, region=(1024,674,645,738)))  


    ##Bot
    MI.click(1679, 627) 
    

    ##Gun
    MI.click(1196, 625)  


    ##Aux
    MI.click(1406, 626)


    ##Strike
    MI.click(1428, 548)

    ##Attack
    MI.click(1126,773)

    ##Attack
    MI.click(1126,773)

    ##Attack
    MI.click(1126,773)


# def groupB(name, coords, NPCone):
#     global groupBCore

#     ##Aux
#     MI.click(1406, 626)

#     ##Bot
#     MI.click(1679, 627)

#     ##Rain
#     MI.click(MI.locateCenterOnScreen('images/skills/rain.png', confidence = 0.45, region=(1024,674,645,738)))

#     ##Gun
#     MI.click(1196, 625)

#     ##Strike
#     MI.click(1428, 548)

#     ##Attack
#     MI.click(coords)


# def groupC(name, coords, NPCone):
#     global groupCCore

#     ##Aux
#     MI.click(1406, 626)

#     ##Bot
#     MI.click(1679, 627)

#     ##Rain
#     MI.click(MI.locateCenterOnScreen('images/skills/rain.png', confidence = 0.45, region=(1024,674,645,738)))

#     ##Gun
#     MI.click(1196, 625)

#     ##Strike
#     MI.click(1428, 548)

#     ##Attack
#     MI.click(coords)



# def groupD(name, coords, NPCone):
#     global groupDCore

#     ##Aux
#     MI.click(1406, 626)

#     ##Bot
#     MI.click(1679, 627)

#     ##Rain
#     MI.click(MI.locateCenterOnScreen('images/skills/rain.png', confidence = 0.45, region=(1024,674,645,738)))

#     ##Gun
#     MI.click(1196, 625)

#     ##Strike
#     MI.click(1428, 548)

#     ##Attack
#     MI.click(coords)


# def groupE(name, coords, NPCone):
#     global group5Strike
    
#     ##Aux
#     MI.click(1406, 626)

#     ##Bot
#     MI.click(1679, 627)

#     ##Rain
#     MI.click(MI.locateCenterOnScreen('images/skills/rain.png', confidence = 0.45, region=(1024,674,645,738)))

#     ##Gun
#     MI.click(1196, 625)

#     ##Strike
#     MI.click(1428, 548)

#     ##Attack
#     MI.click(coords)


# def groupF(name, coords, NPCone):
#     global group5Strike
    
#     ##Aux
#     MI.click(1406, 626)

#     ##Bot
#     MI.click(1679, 627)

#     ##Rain
#     MI.click(MI.locateCenterOnScreen('images/skills/rain.png', confidence = 0.45, region=(1024,674,645,738)))

#     ##Gun
#     MI.click(1196, 625)

#     ##Strike
#     MI.click(1428, 548)

#     ##Attack
#     MI.click(coords)


# def groupG(name, coords, NPCone):

#     ##Aux
#     MI.click(1406, 626)

#     ##Bot
#     MI.click(1679, 627)

#     ##Rain
#     MI.click(MI.locateCenterOnScreen('images/skills/rain.png', confidence = 0.45, region=(1024,674,645,738)))

#     ##Gun
#     MI.click(1196, 625)

#     ##Strike
#     MI.click(1428, 548)

#     ##Attack
#     MI.click(coords)

# def attackHuman(coords, NPCone):
#     ##Aux
#     MI.click(1406, 626)

#     ##Bot
#     MI.click(1679, 627)

#     ##Rain
#     MI.click(MI.locateCenterOnScreen('images/skills/rain.png', confidence = 0.45, region=(1024,674,645,738)))

#     ##Gun
#     MI.click(1196, 625)

#     ##Strike
#     MI.click(1428, 548)

#     ##Attack
#     MI.click(coords)
    
    

def battleDone():
    global group1Strike
    global group5Strike
    global groupBCore
    global groupCCore
    global groupDCore

    group1Strike = True
    group5Strike = True
    groupBCore = True
    groupCCore = True
    groupDCore = True
