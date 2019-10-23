import os

def openChromeTab(url):
	command = """/usr/bin/open -a "/Applications/Google Chrome.app" '{0}'""".format(url)
	os.system(command)

def openMultipleChromeTabs(urls):
	urlList = " ".join(urls)
	command = """
		osascript \
			-e 'on run(theUrls)' \
			-e '  tell app id "com.google.chrome" to tell make new window' \
			-e '    repeat with theUrl in theUrls' \
			-e '      set newTab to make new tab ¬' \
			-e '        with properties {{ url: theUrl }}' \
			-e '    end repeat' \
			-e '    tell tab 1 to close' \
			-e '  end tell' \
			-e 'end run' \
		{0}
	""".format(urlList)
	os.system(command)

def openMultipleChromeWindows(windows):
	for window in windows:
		openMultipleChromeTabs(window)