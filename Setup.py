import os
import subprocess

filecheck = ['jobdescription.txt', 'education.txt', 'workexperience.txt']
configfile = 'config.py'
LettersDir = 'CoverLetters'

TxtList = []
Upperlist = []

def FindFiles(files):
    ThePath = os.path.join(Desti, files)
    if os.path.exists(ThePath):
        print('File '+ files + ' already exists')
    else:
        with open(ThePath, 'w'):
            pass
    return ThePath


currentSpot = os.getcwd()
FinalDir = r'CV-Builder'
Desti = os.path.join(currentSpot, FinalDir)
filesinhere = os.listdir(Desti)
print(filesinhere)

for files in filecheck:
    MyPath = FindFiles(files)
    TxtList.append(MyPath)

anotherList = []
configPath = os.path.join(Desti, configfile)
if os.path.exists(configPath):
    print('COnfig File exists')
else:
    with open(configPath, 'w') as base:
        base.write('API = " "\n')
    for files in TxtList:
        splitted = files.split('.')
        name = splitted[0]
        uppername = name.upper()
        Upperlist.append(uppername)
        mystring = uppername + ' = ' + files
        anotherList.append(mystring)
        with open(configPath, 'a') as base:
            for finals in anotherList:
                base.write(f"r'{finals}'\n")


Letters = os.path.join(Desti, LettersDir)
if os.path.exists(Letters) and os.path.isdir(Letters):
    print('Directory for CoverLtters Exists')
else:
    os.makedirs(Letters)
    blah = LettersDir.upper()
    Upperlist.append(blah)
    neededString = LettersDir.upper()+' = '+Letters
    with open(configPath, 'a') as continuation:
        continuation.write(f"r'{neededString}'\n")

print('Your initial Setup is now complete, if you have not already, be sure to enter the required information into the necessary file!!')


