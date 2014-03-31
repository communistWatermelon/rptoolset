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
gameInProgress = False
gameState = "LOBBY"

# wait for players to connect to the admin
def waitForPlayers():
	return

# check if players are ready to play
def playersReady():
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

# handle an inturrupting move
def handleInturrupt():
	return

def main():
	waitForPlayers()
	while not playersReady():
		continue

	getCharacters()
	alertPlayers("GAME START")
	beginGame()