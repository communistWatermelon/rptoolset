"""
Tools for all users
	Used to create and modify character values

	create character sheet
	read character sheet
	modify character sheet
"""
import os

#create a simple character sheet using user input
def createCharacterSheet(character):
	default = readDefaultSheet()
	userCharacter = {}

	if not os.path.exists(character + ".char"):
		with open(character + ".char", 'w') as f:
			for field in default:
				userCharacter[field] = raw_input("enter " + field + " = ")
				f.write(field + "=" + userCharacter[field] + '\n')
	return

#this will read in all the user defined game parameters, like classes, status effects, etc
def readUserGameParams():
	return

#this will read in standard game parameters, for inexperienced users
def readDefaultGameParams():
	return

#reads the template character sheet
def readDefaultSheet():
	fields = []
	fieldName = ''
	fieldValue = ''

	with open("template.char") as f:
		for line in f:
			if not line.startswith("#"):
				line = stripWhitspace(line)
				temp = line.split("=")
				fieldName = temp[0]
				fields.append(fieldName)
	return fields 

#read in all the character values into the game
def readCharacterSheet(character):
    fields = {}
    fieldName = ''
    fieldValue = ''

    with open(character + ".char") as f:
        for line in f:
            if not line.startswith("#"):
                line = stripWhitspace(line)
                temp = line.split("=")
                fieldName = temp[0]
                fieldValue = temp[1]
                fields[fieldName] = fieldValue
    return fields 

#modify a field within a character sheet, setting it to value
def modifyValue(character, field, value):
	return

#get the value from field of a character sheet
def getValue(character, field):
	return

#apply a certain amount of damage to a character, then check if they are dead
def applyDamage(character, damage):
	checkDeath(character)
	return

#check if the character is dead
def checkDeath(character):
	return

#check all the equipment a character is wearing
def checkEquipment(character):
	return

#check only some equipment a character is wearing, based on type
def checkSomeEquipment(character, type):
	return

#compare some equipment to what a user is currently equipped to their character
def compareEquipment(character, equipment):
	return

#check all status effects a character has
def checkEffects(character):
	return

#add an effect to a character
def addEffect(character, effect):
	return

#remove an effect from a character
def removeEffect(character, effect):
	return

#add health to a character
def healDamage(character, heal):
	return

#add xp to a character
def addXP(character, xp):
	return

#check the currentl level of a character
def getLevel(character):
	return

#get the current xp of a character
def getXP(character):
	return

#checks the xp needed to get to the next level 
def getXPtoNextLevel(level):
	return 0

#check to see if a character has enough xp to level up
def checkLevelUp(character):
	currXP	  = getXP(character)
	currLevel = getLevel(character)
	while (currXP > getXPtoNextLevel(level)):
		currLevel = levelUp(character)

#level up the character
def levelUp(character):
	return

def checkGameMode():
	return

def stripWhitspace(text):
	temp = text.rstrip()
	temp = temp.lstrip()
	return temp