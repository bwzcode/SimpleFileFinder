#Brian Zhu
#June 4th, 2021
#Python 3 File Finder

import os
#Get FileName and Path
def inputter():
    print("FileFinder v1.0 - Brian Zhu")
    fName = input("Please specify a Filename + File Extension: ")
    fPath = input("Please specify a Directory: ")
    return fName,fPath
#Find the File, Get Boolean Values to see if it exists
def finder(inName,inPath):
    name = inName
    path = inPath
    for root, dirs, files in os.walk(path):
        if name in files:
            return True
        else:
            return False
#Print a message to whether or not the file exists in the path or not
def verifier(inBool,inName,inPath):
    boolVar = inBool
    name = inName
    path = inPath
    if(boolVar == True):
        print("The specified file: "+name+" exists in the directory: "+ path)
    else:
        print("File does not exist")
#Main Method
def main():
    name,path = inputter()
    boolVar = finder(name,path)
    verifier(boolVar,name,path)
if __name__ == "__main__":
    main()