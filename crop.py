from PIL import Image
import os

# Function to crop multiple files
resource = 'alldatasets/Class1'

def main():
    for count, filename in enumerate(os.listdir(resource)):
        src = resource + '/' + filename
        img = Image.open(src)
        area = (100, 100, 512, 512) #X start, Y start, X end, Y end 
        img.crop(area).save("cropped"+str(count+1)+".png")

# Driver Code
if __name__ == '__main__':
    main()