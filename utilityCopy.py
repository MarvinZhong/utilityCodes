import os
import shutil
from tqdm import tqdm

parentFolder = "main/parent/folder"
newParentFolder = "main/parent/newFolder"


def allContentsToOneFolder():
    for folderName, subfolders, filenames in os.walk(parentFolder):
        print("The current folder is " + folderName)
        for subfolder in subfolders:
            print("SUB FOLDER OF " + folderName + ": " + subfolder)
        for filename in filenames:
            print("FILE INSIDE " + folderName + ": " + filename)
            shutil.copy(os.path.join(folderName, filename), newParentFolder)


def duplicateFolder():
    # remake folder structure from parentFolder to newParentFolder
    for folderName, subfolders, filenames in os.walk(parentFolder):
        print("\nThe current folder is " + folderName)
        for filename in tqdm(filenames):
            # slice folderName without parentFolder
            newFolderName = folderName[len(parentFolder):]
            # make new folder
            newFolder = newParentFolder + newFolderName
            if not os.path.exists(newFolder):
                os.makedirs(newFolder)
            # copy file to new folder
            shutil.copy(os.path.join(folderName, filename), newFolder)


def simpleCopy():
    shutil.copytree(parentFolder, newParentFolder)


def countFiles(countThisFolder):
    listExt = []
    for folderName, subfolders, filenames in os.walk(countThisFolder):
        for filename in filenames:
            # split filename to get extension
            ext = os.path.splitext(filename)[1]
            # if ext is not in listExt, add it
            if ext not in listExt:
                listExt.append(ext)
    print("There are " + str(len(listExt)) + " different extensions in " + countThisFolder)
    # print listExt
    countTotal = 0
    for ext in listExt:
        count = 0
        for folderName, subfolders, filenames in os.walk(countThisFolder):
            for filename in filenames:
                countTotal += 1
                if filename.endswith(ext):
                    count += 1
        print("\tThere are " + str(count) + " files with extension " + ext + " in " + countThisFolder)
    print("There are " + str(int(countTotal / len(listExt))) + " files in " + countThisFolder + "\n")


def main():
    # copy and replace the same folder structure and files to new folder
    # simpleCopy()

    # make the same folder structure and copy files to new folder without replacing
    duplicateFolder()

    # copy all contents to one folder
    # allContentsToOneFolder()

    # count files with different ext in both folders
    countFiles(parentFolder)
    countFiles(newParentFolder)


if __name__ == '__main__':
    main()
