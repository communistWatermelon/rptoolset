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
import threading
import errno

global client
playerAvatar = "NULL"
gameInProgress = True
adminIP = "localhost"
adminPort = 8080

# connects the client to the admin, using the ipaddress and username provided.
def connectToAdmin(ipaddress, username):
	global client
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect((ipaddress, adminPort))
	#client.send(username)
	return client

# displays all characters in the character folder, and allows user to select one to play with.
# first display stats, then confirm character
# return characters name
def chooseCharacter(characters):
	global playerAvatar
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

	playerAvatar = str(characters[int(choice) - 1])
	print playerAvatar + " chosen!"

	return int(choice) - 1


# begins gameplay. Waits for turn, then gets the users move
def beginGame():
	while gameInProgress:
		if not playersTurn():
			checkStats()
			continue
		move = getMove()
		alertAdmin(move)

	return

# if it is the players turn, return true
def playersTurn():
	print 'who\'s turn?'
	return True

# obtains input from the user to send to admin
def getMove():
	return raw_input()

# handle an alert from the admin
def handleAlert(client, line):
	print "alert handling"

	while (True):
		try: 
			data = client.recv(10)
			print data
		except socket.error as e:
			if e.args[0] == errno.EWOULDBLOCK:
				continue
			elif e.args[0] == errno.EBADF:
				break
			else:
				print("Error occured on recv: {0}".format(e))
				break

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
	print 'checking stats'
	return

# check player's equipment
def checkEquipment():
	return

def main():
	global client
	characters = []

	client = connectToAdmin("localhost", "player1")

	print "hit enter to ready up!"
	raw_input()

	alertThread = threading.Thread(target=handleAlert, args=(client, "hello"), )
	alertThread.daemon = True
	alertThread.start()

	choice = chooseCharacter(characters)
	alertAdmin("READY")
	sendCharacter(characters[choice])
	raw_input()

	while True:
		time.sleep(1)
	
	beginGame()
	
	return

main()
