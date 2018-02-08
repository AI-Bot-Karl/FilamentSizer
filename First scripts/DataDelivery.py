import os

files = 'Data'
root = os.path.dirname(os.path.realpath(__file__))

def getImage_Names():
    Data_files = os.listdir(files)
    print('Files at' + root + "/" + files + "/" + Data_files.__str__())
    return Data_files

def getImage_FilePath():
    filenames = getImage_Names()
    filepaths = []
    for file in filenames:
        filepaths.append(os.path.join(root, files, file))
    return filepaths