import os
with open("RT Directoy.txt") as Reader:
    DirectoryLocation = Reader.readline()
    print(DirectoryLocation)
space = ""
print(space)
Directory = DirectoryLocation
FilesInDirectory = os.listdir(Directory)
print(FilesInDirectory)
print(space)
x = input("What # do you want to start from? ")
FileName = str(input("Name for the files? "))
for file in FilesInDirectory:
    FileExtension = os.path.splitext(file)
    FileExtension = FileExtension[1]
    print(FileExtension)
    x = str(x)
    print(Directory + file)
    os.rename(Directory + '\\' + file, Directory + "\\" + FileName + " " + x + FileExtension)
    x = int(x)
    x +=1
    print (file)

