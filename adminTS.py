# admin side of game
# wait for clients to connect and ready up
# download characters
# add characters to current game
# tell clients to start game
# while playing
# 	fastest player gets turn
# 	wait for player's move
# 		react to players move (summon monsters as new players)
#		move to next player
import socket
import globalTools
import threading
import time
import errno

gameInProgress = False
gameState = "NULL"
sourcePort = 8080
numberOfPlayers = 1
playerThreads = {}
playersState = {}

# wait for players to connect to the admin
# each player is then added to a list of players, as a new socket
# each socket is monitored for data
def waitForPlayers():
	global gameState
	global numberOfPlayers
	global playersState

	gameState = "LOBBY"
	listenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	listenSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	listenSocket.bind(('', sourcePort))

	connectedPlayers = 0
	listenSocket.listen(1)

	while (gameState == "LOBBY"):
		player, address = listenSocket.accept()
		print 'Connected ', address
		connectedPlayers += 1
		
		playerThread = threading.Thread(target=listenPlayer, args=(player, address), )
		playerThread.daemon = True
		playerThreads[player] = playerThread
		playersState[player] = "WAITING"
		playerThread.start()

		if (numberOfPlayers == connectedPlayers):
			gameState = "SELECTION"

	return listenSocket


# check if players are ready to play
def listenPlayer(player, address):
	global playersState 

	while (True):
		try: 
			data = player.recv(5)
			if data.find("READY") != -1:
				playersState[player] = "READY"
			else:
				print data
				time.sleep(1)
		except socket.error as e:
			if e.args[0] == errno.EWOULDBLOCK:
				continue
			elif e.args[0] == errno.EBADF:
				break                
			else:
				print("Error occured on recv: {0}".format(e))
				break
	return

# download character sheets from each client
def getCharacters():
	return

# alert all players with message
def alertPlayers(messsage):
	return

# begin game loop, choose turn.
# if turn is players
#	 wait for player, react to player
# else 
#	make npc move
def beginGame():
	while gameInProgress:
		playerMove = chooseTurn()
		if isPlayer(playerMove):
			alertPlayers(playerMove)
			waitForMove(playerMove)
			adminMove = getReaction()
			alertPlayers(adminMove)
		else:
			creatureMove = getNPCMove(playerMove)
			alertPlayers(creatureMove)
			handleInturrupt()
	return

# checks to see if the character is player controlled or admin controlled
def isPlayer(character):
	return

# pick the player with the highest speed and the lowest number of turns, return characters name. if the 
def chooseTurn():
	return

# wait for user input 
def waitForMove():
	return

# react to user input, using input from the admin
def getReaction():
	return

#add a player to the game  (human = true or false)
def addPlayer(character, human):
	return

# check if every player is currently ready
def allPlayersReady():
	for player in playersState.keys():
		if playersState[player] != "READY":
			return False
	return True

# handle an inturrupting move
def handleInturrupt():
	return

def main():
	socket = waitForPlayers()
	while not allPlayersReady():
		time.sleep(1)
		continue
	print "All ready!"

	while True:
		time.sleep(1)
	getCharacters()
	alertPlayers("GAME START")
	beginGame()
	raw_input()

main()
