import os
import shutil

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
        print("The current folder is " + folderName)
        for subfolder in subfolders:
            print("SUB FOLDER OF " + folderName + ": " + subfolder)
        for filename in filenames:
            print("FILE INSIDE " + folderName + ": " + filename)
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


def main():
    # copy the same folder structure and copy files to it
    # simpleCopy()

    # longer version of simpleCopy()
    # can't copy empty folder
    duplicateFolder()

    # copy all contents to one folder
    # allContentsToOneFolder()


if __name__ == '__main__':
    main()
