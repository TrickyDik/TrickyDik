import os
import pathlib

ParentDir="C:/Users/Richard/Documents/"

thislist = ["Monthly","Weekly Casuals","GSMD","Schools","Freemens","City Police"]

for x in thislist:
  Path=os.path.join(ParentDir,x)
  os.makedirs(Path)
  print(Path)
