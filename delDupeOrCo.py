import shutil
import os

# Function to modify multiple files that have the same file names
toAction = 'A:/Folder/contain/files/to/modify'
toCompare = 'B:/Folder/contain/files/to/compare'
toSave = "C:/Empty/folder/to/save/the/files"

def main():
    # compare filename of toAction and toCompare
    count = 0
    for filename in os.listdir(toAction):
        if filename in os.listdir(toCompare):
            # copy file from toAction to toSave
            shutil.copyfile(os.path.join(toAction, filename), toSave + '/' + filename)

            # Delete duplicate files from toAction
            # os.remove(os.path.join(toAction, filename))

            # Print duplicate files and count
            # count += 1
            # print(filename, count)




# Driver Code
if __name__ == '__main__':
    main()
