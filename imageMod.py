from PIL import Image
import os
import PIL.ImageOps   

# Function to convert multiple files
resource = 'D:/Folder/of/images/to/convert'

def main():
    for count, filename in enumerate(os.listdir(resource)):
        src = resource + '/' + filename
        img = Image.open(src)
        # invert image colour
        PIL.ImageOps.invert(img).save(src)
        
        # convert image to Grayscale
        #img.convert('LA').save(src)

# Driver Code
if __name__ == '__main__':
    main()
