#dlf-loader

import os
import sys
import subprocess
url=sys.argv[1]
fileout=""
try:
    fileout=sys.argv[2]
except:
    pass


r=subprocess.check_output(["curl", url])

tok=r.split()

for l in tok:
    if l.find(".mp3") >0:
        k = l.split("\"")
        print k[1]
        if fileout=="":
            fileout = k[1].split("/")[-1]
        r = subprocess.check_output(["curl",k[1],"--output",fileout])
        if r==0:
            break
        #print r
