def keyCommandParser(allCommands):
	returnLib = {}
	for commandDictKey in allCommands:
		commandDict = allCommands[commandDictKey]
		for commandKey in commandDict:
			command = commandDict[commandKey]

			keyboardKey = "-".join(sorted(command["keyCombo"]))
			if keyboardKey in returnLib:
				raise Exception("{0} found twice!".format(keyboardKey))
			else:
				returnLib[keyboardKey] = [commandDictKey, commandKey]
	return returnLib
