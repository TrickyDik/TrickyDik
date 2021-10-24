#Create new folders in my Documents folder
#2021-03-29

import os   #Use the OS Module

print('Enter folder name')  #Ask for folder name
Folder=str(input())

print('How many folders?')  #Ask for number of folders needed
NumberOfFolders=input()

ParentDir="C:/Users/Richard/Documents/"     #default path where folders will be created

for i in range(1,int(NumberOfFolders)+1):
    Path=os.path.join(ParentDir,Folder+str(" ")+str(i).zfill(2))
    os.makedirs(Path)
    print(Path)
      
print(' ')
print(str(NumberOfFolders)+' Folders have been created in '+ParentDir)
