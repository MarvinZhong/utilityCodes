from PIL import Image
import os

# Function to convert multiple files
resource = 'alldatasets/Class1'

def main():
    for count, filename in enumerate(os.listdir(resource)):
        src = resource + '/' + filename
        img = Image.open(src)
        img.convert('LA').save(src)

# Driver Code
if __name__ == '__main__':
    main()
