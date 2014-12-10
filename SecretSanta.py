__author__ = 'mhorine'

from SantaPlayer import *
import random
import smtplib
import config

def createPlayers():
    playerList = []

    with open('players.txt', 'r') as fileIn:
        for line in fileIn:
            data = line.strip().split(',', 2)
            data = [d.strip() for d in data]
            player = SantaPlayer(data[0], data[1])
            if data[2]:
                list = [d.strip(' []') for d in data[2].split(',')]
                player.addExclusion(list)
            playerList.append(player)
        for player in playerList:
            player.printInfo()

    return playerList

def drawMatch(player, list):
    complete = False
    hatList = []
    for slip in list:
        if slip.receivingStatus == 'Needs Match':
            hatList.append(slip.name)
    print('Hat List is: ' + str(hatList))

    while complete != True:
        random.shuffle(hatList)
        print('Shuffled Hat List is: ' + str(hatList))
        drawName = hatList[random.randint(0, len(hatList)-1)]
        print('I just drew: {0}'.format(drawName))
        draw = next((x for x in list if x.name == drawName), None)
        if draw.name == player.name or draw.name in player.exclusions:
            print('Oops. That\'s not gonna work.\n')
            hatList.remove(drawName)
        else:
            player.match = draw
            player.givingStatus = 'Matched'
            draw.receivingStatus = 'Matched'
            complete = True
            print('\n')

# Call test create function to create group of players

playerList = createPlayers()

for player in playerList:
    print('Current player is ' + player.name)
    drawMatch(player, playerList)

for player in playerList:
    player.printInfo()

with smtplib.SMTP_SSL(config.SMTP_Server) as smtp:
    smtp.login(config.SMTP_User_Name, config.SMTP_Password)
    for player in playerList:
        player.printInfo()
        player.createEmailMessage()
        smtp.send_message(player.msg)