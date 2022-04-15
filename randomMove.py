# move n random files from one directory to another
import os
import random
import shutil

oldPath = 'C:/Users/oldPath/'
newPath = 'C:/Users/newPath/'


def randomFile():
    # get a random file with json ext from the folder
    fileList = os.listdir(oldPath)
    fileName = fileList[random.randint(0, len(fileList) - 1)]
    if fileName.endswith('.json'):
        return fileName
    else:
        return randomFile()


def main():
    # loop for 100 times / files
    n = 100
    for i in range(n):
        # get a random file from the folder
        fileName = randomFile()
        print(fileName)
        # find same fileName with png ext
        for file in os.listdir(oldPath):
            if fileName.replace('.json', '.png') == file:
                print(file)
                # move the file to new folder
                shutil.move(oldPath + fileName, newPath + fileName)
                shutil.move(oldPath + file, newPath + file)
                break

# Driver Code
if __name__ == '__main__':
    main()
