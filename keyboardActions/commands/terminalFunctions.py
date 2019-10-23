import os

def runCommand(command):
	os.system(command)

def openApp(appName):
	command = """open -a {0}""".format(appName)
	os.system(command)

def displayNotification(message):
	command = """osascript -e 'display notification "{}" with title "{}"'""".format(message, "Keyboard Shortcuts")
	os.system(command)