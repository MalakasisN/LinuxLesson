import matplotlib.pyplot as plt
xcoords=[]
ycoords=[]
with open('x-coordstotal.txt') as f:
    for i in f.read().split():
        xcoords.append(float(i))
with open('y-coordstotal.txt') as f:
    for i in f.read().split():
        ycoords.append(float(i))
fig,ax=plt.subplots()
ax.scatter(xcoords,ycoords,c='r',s=0.1)
plt.xlim([-1,1])
plt.ylim([-1,1])

plt.savefig("total5000geneplot.png")