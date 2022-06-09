import os
import shutil
import time
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor


# move files from source to destination
def move_files(filenames, src, dest):
    # process all file names
    for filename in filenames:
        # create the path for the source
        src_path = os.path.join(src, filename)
        # create the path for the destination
        dest_path = os.path.join(dest, filename)
        # # move source file to destination file
        # shutil.move(src_path, dest_path)
        # # move source file to destination file only work with same drive
        # os.rename(src_path, dest_path)
        # # copy source file to destination file and delete source file 
        shutil.copy(src_path, dest_path)
        os.remove(src_path)


# move files from src to dest
def main(src, dest):
    # many files to action
    total = 10000
    files = []
    for count, filename in enumerate(os.listdir(src)):
        # comment bellow 2 lines to make changes to all files
        if count == total:
            break
        if filename.endswith('.jpg'):
            files.append(filename)
    # determine chunksize
    n_workers = 1000
    n_cores = 2
    chunkSize = round(len(files) / n_workers)
    print(chunkSize)
    # # create the process pool
    # with ProcessPoolExecutor(n_cores) as exe:
    # # create the Thread pool
    with ThreadPoolExecutor(n_workers) as exe:
        # split the move operations into chunks
        for i in range(0, len(files), chunkSize):
            # select a chunk of filenames
            filenames = files[i:(i + chunkSize)]
            # submit the batch move task
            _ = exe.submit(move_files, filenames, src, dest)
        exe.shutdown(wait=True)
    print('Done')


# entry point
if __name__ == '__main__':
    aFolder = 'A:\\User\\Folder'
    bFolder = 'B:\\User\\Folder'
    sTime = time.time()
    main(aFolder, bFolder)
    print(round((time.time() - sTime) / 60))
