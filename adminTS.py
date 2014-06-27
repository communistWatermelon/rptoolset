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
connectedPlayers = 0
gameInProgress = True
gameState = "NULL"
sourcePort = 8080
playerThreads = {}
playersState = {}
playersReady = 0
playersSaved = 0

# wait for players to connect to the admin
# each player is then added to a list of players, as a new socket
# each socket is monitored for data
def waitForPlayers():
	global gameState
	global playersState

	gameState = "LOBBY"
	listenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	listenSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	listenSocket.bind(('', sourcePort))

	listenSocket.listen(1)

	while (gameState == "LOBBY"):
		player, address = listenSocket.accept()
		print 'Connected ', address
		
		playerThread = threading.Thread(target=listenPlayer, args=(player, address), )
		playerThread.daemon = True
		playerThreads[player] = playerThread
		playerThread.start()

		if raw_input() == "start":
			break

	return listenSocket


# check if players are ready to play
def listenPlayer(player, address):
	global playersState 
	global playersReady
	global connectedPlayers

	connectedPlayers += 1

	while (True):
		try: 
			data = player.recv(5)
			if data.find("READY") != -1:
				playersReady += 1
			elif data.find("CHARA") != -1:
				getCharacters(player, data)
			else:
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
def getCharacters(player, line):
	global playersState 
	global playersSaved
	global playersSaved

	while (True):
		try: 
			data = player.recv(10)
			if data.find("ARAHC") == -1:
				#handle player data
				print data
			elif data.find("ARAHC") != -1: 
				playersSaved += 1
		except socket.error as e:
			if e.args[0] == errno.EWOULDBLOCK:
				continue
			elif e.args[0] == errno.EBADF:
				break                
			else:
				print("Error occured on recv: {0}".format(e))
				break
	return

# alert all players with message
def alertPlayers(message):
	global playerThreads
	print 'sending: ', message
	for player in playerThreads.keys():
		player.send(message)
	return

def getNPCMove(playerMove):
	return "nothing"

# begin game loop, choose turn.
# if turn is players
#	 wait for player, react to player
# else F
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
	#print 'is player'
	return True

# pick the player with the highest speed and the lowest number of turns, return characters name. if the 
def chooseTurn():
	print '- choose turn'
	player = raw_input()
	return 'TURN ' + player

# wait for user input 
def waitForMove(playerMove):
	print '-- waiting for move from ', playerMove
	return

# react to user input, using input from the admin
def getReaction():
	print '--- getting reaction'
	return raw_input()

#add a player to the game  (human = true or false)
def addPlayer(character, human):
	return

# check if every player is currently ready
def allPlayersReady():
	global playersReady
	global connectedPlayers

	if playersReady != connectedPlayers:
		return False
	return True

def allPlayersSaved():
	global playersSaved
	global connectedPlayers

	if playersSaved != connectedPlayers:
		return False
	return True

# handle an inturrupting move
def handleInturrupt():
	return

def main():
	socket = waitForPlayers()

	while not allPlayersReady():
		print playersReady
		time.sleep(3)
		continue

	print "All ready!"

	while not allPlayersSaved():
		print playersSaved
		time.sleep(1)
		continue

	print 'got all characters!'
	
	print 'alert!'
	alertPlayers("GAME START")
	beginGame()
	raw_input()

main()
