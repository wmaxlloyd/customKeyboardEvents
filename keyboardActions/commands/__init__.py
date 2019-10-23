import os
from importlib import import_module

restrictedFiles = ["__init__.py"]

class systemCommands:
    def __init__(self):
        currentDirectory = __file__.replace('__init__.py','')
        for fn in os.listdir(currentDirectory):
            fullPath = currentDirectory + fn
            if fn not in restrictedFiles and os.path.isfile(fullPath):
                fileName = fn.split('.')[0]
                module = __import__('keyboardActions.commands', fromlist=[fileName])

                setattr(self,fileName,getattr(module,fileName))


#Help documentations:
#   https://stackoverflow.com/questions/8790003/dynamically-import-a-method-in-a-file-from-a-string
#
#   Adds all available function names in all files as methods to the "systemCommands" class
