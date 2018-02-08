import os

root = os.path.dirname(os.path.realpath(__file__))
print(root)
files = 'Data'
Data_files= os.listdir(files)
print('Files at' + files + "." + Data_files.__str__())

for file in Data_files:
    filepath = os.path.join(root, files, file)
    print(filepath)

