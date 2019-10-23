import json

def getJsonContents(file):
    fileObj = open(file)
    print (fileObj.read())
    fileObj.close()
    fileObj = open(file)
    rawJSON = json.loads(fileObj.read())
    fileObj.close()
    return rawJSON

def writeJsonContents(file, jsonContents):
	with open(file, "w") as fileObj:
		fileObj.write(json.dumps(jsonContents))
