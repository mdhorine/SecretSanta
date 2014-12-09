__author__ = 'mhorine'

from SantaPlayer import *
import random
import smtplib

def createPlayers():
    playerList = []
    playerList.append(SantaPlayer('Sara', 'sarascrib429@gmail.com', ['Scott', 'Matt', 'Amanda', 'Sam']))
    playerList.append(SantaPlayer('Scott', 'scott.timberg@gmail.com', ['Sara', 'Matt', 'Amanda', 'Sam']))
    playerList.append(SantaPlayer('Matt', 'mdlhorine@gmail.com', 'Amanda'))
    playerList.append(SantaPlayer('Amanda', 'atimberg@teachfirst.org.uk', 'Matt'))
    playerList.append(SantaPlayer('Craig', 'craigtimberg@gmail.com', 'Ruey'))
    playerList.append(SantaPlayer('Ruey', 'rtimberg@gmail.com', 'Craig'))
    playerList.append(SantaPlayer('Sam', 'samtimberg@gmail.com'))
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

with smtplib.SMTP_SSL("smtp.gmail.com") as smtp:
    smtp.login('mdlhorine@gmail.com', 'gxmwelgyuhzzeide')
    for player in playerList:
        player.printInfo()
        player.createEmailMessage()
        smtp.send_message(player.msg)
