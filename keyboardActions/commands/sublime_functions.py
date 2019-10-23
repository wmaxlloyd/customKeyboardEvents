from libraries.textEditors import userPreferences
preferencesLocation = r'../../Library/Application Support/Sublime Text 3/Packages/User/Preferences.sublime-settings'

def toggleNode():
	userPreferences(preferencesLocation).toggleSetting("folder_exclude_patterns","node_modules")