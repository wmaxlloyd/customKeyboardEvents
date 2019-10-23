from libraries.textEditors import userPreferences
preferencesLocation = r'../../Library/Application Support/Code/User/settings.json'

def toggleNode():
	userPreferences(preferencesLocation).toggleSetting(["files.exclude","**/node_modules"])