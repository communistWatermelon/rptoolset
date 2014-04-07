# client console side of game
# connect to admin
# choose or create character
# ready up
# send characters
# wait for turn (display stats)
# 	send move to admin
import socket
import globalTools

global client
gameInProgress = False
adminIP = "localhost"
adminPort = 8080

# connects the client to the admin, using the ipaddress and username provided. 
def connectToAdmin(ipaddress, username):
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect((ipaddress, adminPort))
	client.send(username)

# displays all characters in the character folder, and allows user to select one to play with.
# first display stats, then confirm character
# return characters name
def chooseCharacter():
	return


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
	client.send(message)
	return

# sends a move that isn't turn specific. Not sure if it's necessary yet?
def sendInturrupt():
	return

# send chosen character to the admin
def sendCharacter(character):
	return

# check player's current stats
def checkStats():
	return

# check player's equipment
def checkEquipment():
	return

def main():
	client = connectToAdmin("localhost", "player1")
	print "hit enter to ready up!"
	raw_input()
	character = chooseCharacter()
	alertAdmin("READY")
	sendCharacter(character)
	raw_input()
	beginGame()
	return

main()
