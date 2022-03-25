import os

# Function to rename multiple files
resource = 'start/folder/with/files/to/rename'
codename = "rename_"


def main():
    for count, filename in enumerate(os.listdir(resource)):
        oriName, fileExt = os.path.splitext(filename)
        dst = codename + str(count+1) + fileExt
        src = resource + '/' + filename
        dst = resource + '/' + dst

        # rename() function will
        # rename all the files
        os.rename(src, dst)


# Driver Code
if __name__ == '__main__':
    main()
