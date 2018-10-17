import random
import matplotlib.pyplot as plt 

npts = 20
grph_size = 400
hull = []
pts = []
ptsp = []

for i in range(npts):
    pts.append((random.randint(0,grph_size),random.randint(0,grph_size)))

def slp_srt(x):
    try:
        return -(x[0] - min_yp[0]) / (x[1] - min_yp[1])
    except:
        if((x[0] - min_yp[0]) < 0):
            return 10000
        else:
            return -10000 + x[0] - min_yp[0]
    
pts.sort(key=lambda x : x[1])
min_yp = pts.pop(0)
pts.sort(key=lambda x : slp_srt(x), reverse = True)
p1 = pts.pop()
p2 = pts.pop()
hull.extend([min_yp,p1,p2])

def orient(p1, p2, p3):
    val = (p2[1] - p1[1]) * (p3[0] - p2[0]) - (p2[0] - p1[0]) * (p3[1] - p2[1])  
    if (val == 0) :
        return 0 
    if (val > 0):
        return 1
    else:
        return 2

while(pts):
    cur_p = pts.pop()
    orip = orient(hull[-1],cur_p,hull[-2])
    
    if(orip > 1):
        hull.append(cur_p)        
    else:
        ptsp.append(hull.pop())
        while(True):
            try:
                orip = orient(hull[-1],cur_p,hull[-2])
                if(orip < 2):
                    ptsp.append(hull.pop())
                else:
                    break
            except:
                break
        hull.append(cur_p)

fig, ax = plt.subplots(figsize=(8,8))
ax.scatter([x[0] for x in ptsp], [x[1] for x in ptsp], c='blue')
ax.scatter([x[0] for x in hull], [x[1] for x in hull], c='red')

i = 0
while i < len(hull):
    x,y = zip(hull[i-1],hull[i])
    ax.plot(x,y,c='r')
    i+=1

plt.show()
