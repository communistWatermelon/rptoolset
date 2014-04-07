# client console side of game
# connect to admin
# choose or create character
# ready up
# send characters
# wait for turn (display stats)
# 	send move to admin
import socket
import globalTools
import time
import os

global client
gameInProgress = False
adminIP = "localhost"
adminPort = 8080

# connects the client to the admin, using the ipaddress and username provided. 
def connectToAdmin(ipaddress, username):
	global client 
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect((ipaddress, adminPort))
	#client.send(username)

# displays all characters in the character folder, and allows user to select one to play with.
# first display stats, then confirm character
# return characters name
def chooseCharacter(characters):
	i = 1
	for character in os.listdir("./characters"):
		characters.append(character)
	
	for character in characters:
		print str(i) +  " " + character
		i+=1
 
	while(True):
		choice = raw_input()
		if (int(choice) + 1 <= len(characters) + 1 and int(choice) + 1 >= 0):
			break
	
	print str(characters[int(choice) - 1]) + " chosen!"

	return int(choice) - 1


# begins gameplay. Waits for turn, then gets the users move
def beginGame():
	while gameInProgress:
		if not playersTurn():
			checkStats()
			continue
		move = getMove()
		sendMove(move)

	return

# if it is the players turn, return true
def playersTurn():
	return False

# obtains input from the user to send to admin
def getMove():
	return

# check if it's your turn, then sends move to the admin
def sendMove():
	return

# handle an alert from the admin
def handleAlert():
	return

# alert the admin of information
def alertAdmin(message):
	global client
	client.send(message)
	return

# sends a move that isn't turn specific. Not sure if it's necessary yet?
def sendInturrupt():
	return

# send chosen character to the admin
def sendCharacter(character):
	line = ''
	total = ''

	alertAdmin("CHARA")
	with open("./characters/" + character) as f:
		line = f.read(1024)
		total += line
	client.send(total)
	client.send("ARAHC")
	return

# check player's current stats
def checkStats():
	return

# check player's equipment
def checkEquipment():
	return

def main():
	characters = []

	client = connectToAdmin("localhost", "player1")
	print "hit enter to ready up!"
	raw_input()
	choice = chooseCharacter(characters)
	alertAdmin("READY")
	sendCharacter(characters[choice])
	raw_input()
	while True:
		time.sleep(1)
	beginGame()
	return

main()
