from libraries.tools.jsonFunctions import getJsonContents
from libraries.tools.jsonFunctions import writeJsonContents

import json

class userPreferences():
	def __init__(self, preferencesLocation):
		self.preferencesLocation = preferencesLocation
		self.userPreferences = self.getUserPreferences()

	def getUserPreferences(self):
		return getJsonContents(self.preferencesLocation)

	def getSetting(self, settings):
		if type(settings) is str:
			settings=[settings]
		finalSetting = self.userPreferences
		for setting in settings:
			if finalSetting and (setting in finalSetting):
				finalSetting = finalSetting[setting]
			else:
				finalSetting = None
		return finalSetting


	def setDirectly(self, settings, value):
		if type(settings) is str:
			settings = [settings]
		changingSetting = self.userPreferences
		for setting in settings[:-1]:
			changingSetting = changingSetting[setting]
		changingSetting[settings[-1]] = value

	def addOrRemoveValue(self, setting, item):
		if item in self.userPreferences[setting]:
			self.userPreferences[setting].remove(item)
		else:
			self.userPreferences[setting].append(item)

	def toggleBool(self, setting):
		self.setDirectly(setting, not bool(self.getSetting(setting)))

	def toggleJSON(self, setting, item=None):
		settingVal = self.getSetting(setting)
		if type(settingVal) is bool:
			self.toggleBool(setting)
		if type(settingVal) is list:
			self.addOrRemoveValue(setting, item)

	def saveSettings(self):
		writeJsonContents(self.preferencesLocation, self.userPreferences)

	def toggleSetting(self, setting, item=None):
		self.toggleJSON(setting, item)
		print (self.userPreferences)
		self.saveSettings()
