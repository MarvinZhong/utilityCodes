import shutil
import os
import time


def makeArchive():
    shutil.make_archive(os.path.join(archiveFolder, 'archive'), 'zip', sourceFolder)


def unpackArchive():
    for root, dirs, files in os.walk(archiveFolder):
        for file in files:
            if file.endswith('.zip'):
                shutil.unpack_archive(os.path.join(root, file), finalFolder)
                os.remove(os.path.join(root, file))


if __name__ == '__main__':
    sourceFolder = 'S:\\source\\folder'
    archiveFolder = 'A:\\archive\\folder'
    finalFolder = 'F:\\final\\folder'
    sTime = time.time()
    makeArchive()
    unpackArchive()
    print(round((time.time() - sTime) / 60))
