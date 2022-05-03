import os

# Function to rename multiple files
resource = 'start/folder/with/files/to/rename'
codename = "rename_"
findExt = ".png"
newExt = ".jpg"


def main():
    for count, filename in enumerate(os.listdir(resource)):
        oriName, fileExt = os.path.splitext(filename)
        dst = codename + str(count+1) + fileExt
        print("renaming " + filename + " to " + dst)
        src = resource + '/' + filename
        dst = resource + '/' + dst

        # rename() function will
        # rename all the files
        os.rename(src, dst)
        
        # change ext file without rename
#         if filename.endswith(findExt):
#             filename = os.path.splitext(filename)[0]
#             print("changing file ext of ", filename)
#             os.rename(os.path.join(resource, filename + findExt),
#                       os.path.join(resource, filename + newExt))


# Driver Code
if __name__ == '__main__':
    main()
