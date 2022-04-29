import os
import shutil

mainFolder = "main/folder/toSort"


# image name example : MRV01-003-000-002.jpg

def main():
    # sort files by last code name in file name
    for filenames in os.listdir(mainFolder):
        if filenames.endswith(".jpg"):
            # file name without extension
            fileName = filenames.split(".")[0]
            # slice file name by - to get last code name
            codeName = int(fileName.split("-")[-1])
            print(codeName)
            # create new folder with codename
            newFolder = mainFolder + "/" + str(codeName)
            # create new folder if it doesn't exist
            if not os.path.exists(newFolder):
                os.makedirs(newFolder)
            # move file to new folder
            shutil.move(mainFolder + "/" + filenames, newFolder + "/" + filenames)


if __name__ == '__main__':
    main()
