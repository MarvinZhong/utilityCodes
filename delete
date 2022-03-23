import os

# Function to remove multiple files
firstDir = 'folder/with/files/to/delete'
secondDir = 'folder/with/files/to/compareWith'


def main():
    # compare filename of firstDir and secondDir
    for filename in os.listdir(firstDir):
        if filename in os.listdir(secondDir):
            os.remove(os.path.join(firstDir, filename))


# Driver Code
if __name__ == '__main__':
    main()
