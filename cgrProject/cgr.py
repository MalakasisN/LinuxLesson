import math
import numpy as np
import matplotlib.pyplot as plt
import argparse

parser=argparse.ArgumentParser(description='Output:CGR plot for any string sequence')
parser.add_argument('--filename','-x',default='randseq.FA')
parser.add_argument('--distance','-k',default=1.5)
args=parser.parse_args()

def f(x):
    with open(x) as f:
        lines=f.readlines()
        for line in lines:
            if line[0]=='>': 
                seq=lines[lines.index(line)+1]
                break
            else:
                seq=lines[0]           
    return seq.replace('\n','').upper()
seq=f(args.filename)
uniq=[]
for i in seq:
    if i not in uniq:
        uniq.append(i)
uniq.sort()
states=len(uniq)
Ax=math.sqrt(2)/2
Ay=math.sqrt(2)/2
boundx=[Ax]
boundy=[Ay]
for i in range(1,states):
    Bx=-Ay*math.sin(2*np.pi/states)+Ax*math.cos(2*np.pi/states)
    By=Ay*math.cos(2*np.pi/states)+Ax*math.sin(2*np.pi/states)
    boundx.append(Bx)
    boundy.append(By)
    Ax=Bx
    Ay=By
startx=0
starty=0
k=float(args.distance)
coordx=[startx]
coordy=[starty]
for i in seq:
    for j in range(len(uniq)):
        if i==uniq[j]:
            startx=startx+(boundx[j]-startx)/k
            starty=starty+(boundy[j]-starty)/k
            coordx.append(startx)
            coordy.append(starty)
fig,ax=plt.subplots()
ax.scatter(coordx,coordy,c='r',s=0.1)
plt.xlim([-1,1])
plt.ylim([-1,1])
plt.savefig(args.filename+".png")
with open(args.filename+'x-coords.txt','w+') as f:
    for i in coordx:
        f.write(str(i)+' ')
with open(args.filename+'y-coords.txt','w+') as f:
    for i in coordy:
        f.write(str(i)+' ')