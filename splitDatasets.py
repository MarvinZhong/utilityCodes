import os
import random

allClassFolders = 'D:\\Code\\datasets\\allClasses'
makeUpToFolders = 'D:\\Code\\newDatasets'

# ratio each Dir
train, valid, test = 0.6, 0.2, 0.2
basicFolders = ['train', 'valid', 'test']

# make basic folders if not exist in makeUpToFolders
for folder in basicFolders:
    if not os.path.exists(os.path.join(makeUpToFolders, folder)):
        os.mkdir(os.path.join(makeUpToFolders, folder))
        
    # make folders for each class
    for classFolder in os.listdir(allClassFolders):
        if not os.path.exists(os.path.join(makeUpToFolders, folder, classFolder)):
            os.mkdir(os.path.join(makeUpToFolders, folder, classFolder))


# get all class folders
classFolders = os.listdir(allClassFolders)
# loop through all class folders
for classFolder in classFolders:
    # move random images to train, valid, test folder by ratio
    classFolderPath = os.path.join(allClassFolders, classFolder)
    images = os.listdir(classFolderPath)
    random.shuffle(images)
    trainImages = images[:int(len(images) * train)]
    validImages = images[int(len(images) * train):int(len(images) * (train + valid))]
    testImages = images[int(len(images) * (train + valid)):]
    for image in trainImages:
        # move images to train folder
        os.rename(os.path.join(classFolderPath, image), os.path.join(makeUpToFolders, 'train', classFolder, image))
    for image in validImages:
        # move images to valid folder
        os.rename(os.path.join(classFolderPath, image), os.path.join(makeUpToFolders, 'valid', classFolder, image))
    for image in testImages:
        # move images to test folder
        os.rename(os.path.join(classFolderPath, image), os.path.join(makeUpToFolders, 'test', classFolder, image))
        
