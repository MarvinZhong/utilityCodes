import pandas as pd
import os
import warnings

warnings.simplefilter("ignore")
parentFolder = 'D:\\Code\\automation\\20220511-20220517'


def main():
    for folderName, subfolders, filenames in os.walk(parentFolder):
        for filename in filenames:
            if filename.endswith('.xlsx'):

                print("FILE INSIDE " + folderName + ": " + filename)
                filePath = os.path.join(folderName, filename)
                
                # read excel without headers
                # df = pd.read_excel(filePath, index_col=None, header=None, engine="openpyxl")
                df = pd.read_excel(filePath, engine="openpyxl")
                
                # uncomment this code to custom Header
#                 newHead = ['MeasureTime', 'KeyValueList', '', '', 'Operator', 'RawData', '', '', '', 'Remark']
#                 df.columns = newHead

                # save to csv
                df.to_csv(filePath.replace('.xlsx', '.csv'), index=False)
      
                # delete the original xlsx file
                os.remove(filePath)
                print("FILE DELETED: " + filePath)
                print("FILE INSIDE " + folderName + ": " + filename + " DONE")


if __name__ == '__main__':
    main()
