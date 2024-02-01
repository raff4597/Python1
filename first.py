#Imports
import pygame
import sys
import os
import time
import random

# CURRENT BUGS
# When i click anywhere while the game is loading, once it switches to the start menu, the game crashes,

#Initializing
pygame.init()
pygame.font.init()
myFont = pygame.font.SysFont('Comic Sans MS', 30)

#Setting up screen
screen_width = 1000
screen_height = 650
screen = pygame.display.set_mode((screen_width, screen_height))

#Variables
game_state = "loadingScreen"
selectedCountry = 0
counter = 0
teams = ["England", "Belgium", "Hungary", "Portugal", "Slovakia", "France", "Croatia", "Germany", "Romania", "Turkey", "Albania", "Czechia", "Italy", "Scotland", "Spain", "Austria", "Denmark", "Netherlands", "Serbia", "Switzerland"]
team1 = 0
team2 = 0
team3 = 0
team4 = 0
team5 = 0
team6 = 0
team7 = 0
team8 = 0
team9 = 0
team10 = 0
team11 = 0
team12 = 0
team13 = 0
team14 = 0 
team15 = 0
team16 = 0
team17 = 0
team18 = 0
team19 = 0
team20 = 0

count = 0

#Buttons

englandButton = 0
belgiumButton = 0
hungaryButton = 0
portugalButton = 0
slovakiaButton = 0
franceButton = 0
croatiaButton = 0
germanyButton = 0
romaniaButton = 0
turkeyButton = 0
albaniaButton = 0
czechiaButton = 0
italyButton = 0
scotlandButton = 0
spainButton = 0
austriaButton = 0
denmarkButton = 0
netherlandsButton = 0
serbiaButton = 0
switzerlandButton = 0

buttons = [englandButton, belgiumButton, hungaryButton, portugalButton, slovakiaButton, franceButton, croatiaButton, germanyButton, romaniaButton, turkeyButton, albaniaButton, czechiaButton, italyButton, scotlandButton, spainButton, austriaButton, denmarkButton, netherlandsButton, serbiaButton, switzerlandButton]

#Backgrounds
loadingScreen = pygame.image.load('FootballBackground.png')
teamSelect = pygame.image.load("countries.png")
tornementPlan = pygame.image.load("TornementPlan.png")
pointsTable = pygame.image.load("PointsTable.png")


#Classes
class Country:
    def __init__(self, image):
        self.Img = pygame.image.load(image)
        self.Icon = pygame.transform.scale(self.Img, (40,40))

class Table:
    
    def __init__(self, MP, Wins, Draws, Losses, GD, Points):
        self.MP: int = MP
        self.Wins: int = Wins
        self.Draws: int = Draws
        self.Losses: int = Losses
        self.GD: int = GD
        self.Points: int = Points


#Drawing loading screen
def drawLoadingScreen():
    screen.blit(loadingScreen, (0,0))
    pygame.display.update()

#Drawing the team select page
def drawStartMenu(buttons):
   
   screen.blit(teamSelect, (0,0))

   pygame.display.update() 

   #Buttons
    
   buttons[0] = pygame.Rect(60, 126, 129.3, 80)
   buttons[1] = pygame.Rect(248, 126, 129.3, 80)
   buttons[2] = pygame.Rect(436, 126, 129.3, 80)
   buttons[3] = pygame.Rect(624, 126, 129.3, 80)
   buttons[4] = pygame.Rect(812, 126, 129.3, 80)
   buttons[5] = pygame.Rect(60, 255, 129.3, 80)
   buttons[6] = pygame.Rect(248, 255, 129.3, 80)
   buttons[7] = pygame.Rect(436, 255, 129.3, 80)
   buttons[8] = pygame.Rect(624, 255, 129.3, 80)
   buttons[9] = pygame.Rect(812, 255, 129.3, 80)
   buttons[10] = pygame.Rect(60, 384, 129.3, 80)
   buttons[11] = pygame.Rect(248, 384, 129.3, 80)
   buttons[12] = pygame.Rect(436, 384, 129.3, 80)
   buttons[13] = pygame.Rect(624, 384, 129.3, 80)
   buttons[14] = pygame.Rect(812, 384, 129.3, 80)
   buttons[15] = pygame.Rect(60, 513, 129.3, 80)
   buttons[16] = pygame.Rect(248, 513, 129.3, 80)
   buttons[17] = pygame.Rect(436, 513, 129.3, 80)
   buttons[18] = pygame.Rect(624, 513, 129.3, 80)
   buttons[19] = pygame.Rect(812, 513, 129.3, 80)

#Drawing tornement plan

def tornementPlanDisplay():

    screen.blit(tornementPlan, (0,0))

    global count
    count = count + 1

    team = [team1, team2, team3, team4, team5, team6, team7, team8, team9, team10, team11, team12, team13, team14, team15, team16, team17, team18, team19, team20]

    if count == 1:
        random.shuffle(teams)
    

    for i in range(len(teams)):
        team[i] = teams[i]

    groupA = [team[0], team[1], team[2], team[3], team[4]]
    groupB = [team[5], team[6], team[7], team[8], team[9]]
    groupC = [team[10], team[11], team[12], team[13], team[14]]
    groupD = [team[15], team[16], team[17], team[18], team[19]]
    
    for i in range (5):

        if groupA[i] == selectedCountry:
            teamText = myFont.render(groupA[i], False, (255,0,0))
        else:
            teamText = myFont.render(groupA[i], False, (0,0,0))
        teamRect = teamText.get_rect()
        teamRect.center = (137, 390 + (40 * i))
        screen.blit(teamText, teamRect.topleft)

    for i in range (5):

        if groupB[i] == selectedCountry:
            teamText = myFont.render(groupB[i], False, (255,0,0))
        else:
            teamText = myFont.render(groupB[i], False, (0,0,0))
        teamRect = teamText.get_rect()
        teamRect.center = (379, 390 + (40 * i))
        screen.blit(teamText, teamRect.topleft)

    for i in range (5):
        if groupC[i] == selectedCountry:
            teamText = myFont.render(groupC[i], False, (255,0,0))
        else:
            teamText = myFont.render(groupC[i], False, (0,0,0))
        teamRect = teamText.get_rect()
        teamRect.center = (621, 390 + (40 * i))
        screen.blit(teamText, teamRect.topleft)

    for i in range (5):

        if groupD[i] == selectedCountry:
            teamText = myFont.render(groupD[i], False, (255,0,0))
        else:
            teamText = myFont.render(groupD[i], False, (0,0,0))
        teamRect = teamText.get_rect()
        teamRect.center = (863, 390 + (40 * i))
        screen.blit(teamText, teamRect.topleft)
    
    pygame.display.update()

    return groupA, groupB, groupC, groupD

#Points table display
def pointsTableDisplay(groupA, groupB, groupC, groupD, counter):
    screen.blit(pointsTable, (0,0))


    #Displaying icons
    for i in range(5):
        text = groupA[i] + "Flag.png"
        countryIcon = Country(text)
        screen.blit(countryIcon.Icon, (72.5, 42.5*i + 83))

        print(counter)

        tempCountry = groupA[i]
        if counter == 0:
            tempCountry = Table(0, 0, 0, 0, 0, 0)

        string = str(tempCountry.MP)

        countriesMatchesPlayed = myFont.render(string, False, (0,0,0))
        teamRect = countriesMatchesPlayed.get_rect()
        teamRect.center = (138, 101 + (43 * i))
        screen.blit(countriesMatchesPlayed, teamRect.topleft)

        countriesWins = myFont.render(str(tempCountry.Wins), False, (0,0,0))
        teamRect = countriesWins.get_rect()
        teamRect.center = (180, 101 + (43 * i))
        screen.blit(countriesWins, teamRect.topleft)

        countriesDraws = myFont.render(str(tempCountry.Draws), False, (0,0,0))
        teamRect = countriesDraws.get_rect()
        teamRect.center = (224, 101 + (43 * i))
        screen.blit(countriesDraws, teamRect.topleft)

        countriesLosses = myFont.render(str(tempCountry.Losses), False, (0,0,0))
        teamRect = countriesLosses.get_rect()
        teamRect.center = (265, 101 + (43 * i))
        screen.blit(countriesLosses, teamRect.topleft)

        countriesGD = myFont.render(str(tempCountry.GD), False, (0,0,0))
        teamRect = countriesGD.get_rect()
        teamRect.center = (308, 101 + (43 * i))
        screen.blit(countriesGD, teamRect.topleft)

        countriesPoints = myFont.render(str(tempCountry.Points), False, (0,0,0))
        teamRect = countriesPoints.get_rect()
        teamRect.center = (350, 101 + (43 * i))
        screen.blit(countriesPoints, teamRect.topleft)
    for i in range(5):
        text = groupB[i] + "Flag.png"
        countryIcon = Country(text)
        screen.blit(countryIcon.Icon, (635.5, 42.5*i + 83))

        tempCountry = groupB[i]
        if counter == 0:
            tempCountry = Table(0, 0, 0, 0, 0, 0)

        countriesMatchesPlayed = myFont.render(str(tempCountry.MP), False, (0,0,0))
        teamRect = countriesMatchesPlayed.get_rect()
        teamRect.center = (701, 101 + (43 * i))
        screen.blit(countriesMatchesPlayed, teamRect.topleft)

        countriesWins = myFont.render(str(tempCountry.Wins), False, (0,0,0))
        teamRect = countriesWins.get_rect()
        teamRect.center = (743, 101 + (43 * i))
        screen.blit(countriesWins, teamRect.topleft)

        countriesDraws = myFont.render(str(tempCountry.Draws), False, (0,0,0))
        teamRect = countriesDraws.get_rect()
        teamRect.center = (786, 101 + (43 * i))
        screen.blit(countriesDraws, teamRect.topleft)

        countriesLosses = myFont.render(str(tempCountry.Losses), False, (0,0,0))
        teamRect = countriesLosses.get_rect()
        teamRect.center = (827, 101 + (43 * i))
        screen.blit(countriesLosses, teamRect.topleft)

        countriesGD = myFont.render(str(tempCountry.GD), False, (0,0,0))
        teamRect = countriesGD.get_rect()
        teamRect.center = (871, 101 + (43 * i))
        screen.blit(countriesGD, teamRect.topleft)

        countriesPoints = myFont.render(str(tempCountry.Points), False, (0,0,0))
        teamRect = countriesPoints.get_rect()
        teamRect.center = (913, 101 + (43 * i))
        screen.blit(countriesPoints, teamRect.topleft)
    for i in range(5):
        text = groupC[i] + "Flag.png"
        countryIcon = Country(text)
        screen.blit(countryIcon.Icon, (72.5, 42.5*i + 403))

        tempCountry = groupC[i]
        if counter == 0:
            tempCountry = Table(0, 0, 0, 0, 0, 0)

        countriesMatchesPlayed = myFont.render(str(tempCountry.MP), False, (0,0,0))
        teamRect = countriesMatchesPlayed.get_rect()
        teamRect.center = (138, 420 + (43 * i))
        screen.blit(countriesMatchesPlayed, teamRect.topleft)

        countriesWins = myFont.render(str(tempCountry.Wins), False, (0,0,0))
        teamRect = countriesWins.get_rect()
        teamRect.center = (180, 420 + (43 * i))
        screen.blit(countriesWins, teamRect.topleft)

        countriesDraws = myFont.render(str(tempCountry.Draws), False, (0,0,0))
        teamRect = countriesDraws.get_rect()
        teamRect.center = (224, 420 + (43 * i))
        screen.blit(countriesDraws, teamRect.topleft)

        countriesLosses = myFont.render(str(tempCountry.Losses), False, (0,0,0))
        teamRect = countriesLosses.get_rect()
        teamRect.center = (265, 420 + (43 * i))
        screen.blit(countriesLosses, teamRect.topleft)

        countriesGD = myFont.render(str(tempCountry.GD), False, (0,0,0))
        teamRect = countriesGD.get_rect()
        teamRect.center = (308, 420 + (43 * i))
        screen.blit(countriesGD, teamRect.topleft)

        countriesPoints = myFont.render(str(tempCountry.Points), False, (0,0,0))
        teamRect = countriesPoints.get_rect()
        teamRect.center = (350, 420 + (43 * i))
        screen.blit(countriesPoints, teamRect.topleft)
    for i in range(5):
        text = groupD[i] + "Flag.png"
        countryIcon = Country(text)
        screen.blit(countryIcon.Icon, (635.5, 42.5*i + 403))

        tempCountry = groupD[i]
        if counter == 0:
            tempCountry = Table(0, 0, 0, 0, 0, 0)

        countriesMatchesPlayed = myFont.render(str(tempCountry.MP), False, (0,0,0))
        teamRect = countriesMatchesPlayed.get_rect()
        teamRect.center = (701, 420 + (43 * i))
        screen.blit(countriesMatchesPlayed, teamRect.topleft)

        countriesWins = myFont.render(str(tempCountry.Wins), False, (0,0,0))
        teamRect = countriesWins.get_rect()
        teamRect.center = (743, 420 + (43 * i))
        screen.blit(countriesWins, teamRect.topleft)

        countriesDraws = myFont.render(str(tempCountry.Draws), False, (0,0,0))
        teamRect = countriesDraws.get_rect()
        teamRect.center = (786, 420 + (43 * i))
        screen.blit(countriesDraws, teamRect.topleft)

        countriesLosses = myFont.render(str(tempCountry.Losses), False, (0,0,0))
        teamRect = countriesLosses.get_rect()
        teamRect.center = (827, 420 + (43 * i))
        screen.blit(countriesLosses, teamRect.topleft)

        countriesGD = myFont.render(str(tempCountry.GD), False, (0,0,0))
        teamRect = countriesGD.get_rect()
        teamRect.center = (871, 420 + (43 * i))
        screen.blit(countriesGD, teamRect.topleft)

        countriesPoints = myFont.render(str(tempCountry.Points), False, (0,0,0))
        teamRect = countriesPoints.get_rect()
        teamRect.center = (913, 420 + (43 * i))
        screen.blit(countriesPoints, teamRect.topleft)
    
    pygame.display.update()
    
    return counter

def gameSimulator(groupA, groupB, groupC, groupD, counter):
    
    for i in range(4):
        def randomFirstTeam():
            randomFirstTeam = groupA[random.randint(0,4)]
            return randomFirstTeam

        def randomSecondTeam():
            randomSecondTeam = groupA[random.randint(0,4)]
            return randomSecondTeam
        
        randomTeam1 = randomFirstTeam()
        randomTeam2 = randomSecondTeam()

        def teamChecks():
            if randomTeam1 == randomTeam2:
                randomTeam1 = randomFirstTeam()
                randomTeam2 = randomSecondTeam()
                teamChecks()
            elif randomTeam1.MP == 4:
                randomTeam1 = randomFirstTeam()
                teamChecks()
            elif randomTeam2.MP == 4:
                randomTeam2 = randomSecondTeam()
                teamChecks()
            return randomTeam1, randomTeam2

        randomTeam1, randomTeam2 = teamChecks()

        winner = 1

        if winner == random.randint(1,2):
            randomTeam1.MP += 1
            randomTeam1.Points += 3
            randomTeam1.Wins += 1
            randomTeam2.MP += 1
            randomTeam2.Losses -= 1

        print(randomFirstTeam.MP)
        game_state = "PointsTable"
        return counter



#Game loop
while True: 

    if game_state == "loadingScreen":

        drawLoadingScreen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("Clicked")

        time.sleep(4)

        game_state = "startMenu"

    elif game_state == "startMenu":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #Checking which team they selected
                for i in range(len(buttons)):
                    if buttons[i].collidepoint(event.pos):
                        selectedCountry = teams[i]
                        game_state = "tornementPlan"
                        break
                    else:
                        print("No")
        drawStartMenu(buttons)
    elif game_state == "tornementPlan":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                game_state = "PointsTable"
        groupA, groupB, groupC, groupD = tornementPlanDisplay()
    elif game_state == "PointsTable":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                game_state = "Game"
        counter = pointsTableDisplay(groupA, groupB, groupC, groupD, counter)
        counter = counter + 1
    elif game_state == "Game":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
        gameSimulator(groupA, groupB, groupC, groupD, counter)
    
    
