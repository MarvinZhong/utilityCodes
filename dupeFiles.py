# modify files with the same name that have different extensions
import os

folderPath = 'C:/Users/Folders'


def main():
    for filename in os.listdir(folderPath):
        # get filename with json ext
        if filename.endswith('.json'):
            # get filename with png ext
            if filename.replace('.json', '.png') in os.listdir(folderPath):
                # remove both
                print(filename)
                os.remove(os.path.join(folderPath, filename))
                os.remove(os.path.join(folderPath, filename.replace('.json', '.png')))


# Driver Code
if __name__ == '__main__':
    main()
