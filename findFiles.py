import os

def findFile(fileName, folderName):
    filesFound = []
    for path, subdirs, files in os.walk(folderName):
        for name in files:
            if(fileName == name):
                filePath = os.path.join(path,name)
                filesFound.append(filePath)
    return filesFound

print(findFile('file.name', 'startFolder'))
