from PIL import Image
import os
import PIL.ImageOps   

# Function to convert multiple files
resource = 'alldatasets/Class1'

def main():
    for count, filename in enumerate(os.listdir(resource)):
        src = resource + '/' + filename
        img = Image.open(src)
        PIL.ImageOps.invert(img).save("invert"+str(count+1)+".png")

# Driver Code
if __name__ == '__main__':
    main()