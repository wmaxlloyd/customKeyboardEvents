import os
import json
from keyboardActions.commands import systemCommands
from libraries.tools.parseKeyCommands import keyCommandParser
from libraries.tools.jsonFunctions import getJsonContents

systemCommandList = systemCommands()
currentDirectory = __file__.replace('__init__.py','')

systemCommands = getJsonContents(currentDirectory + 'systemCommands.json')
userCommands = getJsonContents(currentDirectory + 'userCommands.json')

commandDict = {'u':userCommands, 's':systemCommands}

parseKeyCommands = keyCommandParser(commandDict)

def findKeyString(keys):
	keyArr = []
	for key in keys:
		keyArr.append(key)

	return "-".join(sorted(keyArr))

def findSystemCommand(action):
	function = systemCommandList
	for attr in action.split("."):
		function = getattr(function, attr)
	return function

def executeKeyboardCommand(keys):
	print (keys)
	currentKeyString = findKeyString(keys)
	if currentKeyString in parseKeyCommands:
		command = commandDict
		for key in parseKeyCommands[currentKeyString]:
			command = command[key]

		function = findSystemCommand(command["action"])

		print("Executing --> {0}".format(command["label"]))
		if "notification" in command and command["notification"]:
			systemCommandList.terminalFunctions.displayNotification(command["notification"])
		if command["arguement"]:
			return function(command["arguement"])
		else:
			return function()