import random
from Map import Map


map=Map('data.txt')
goalx=5
goaly=7
startx=2
starty=0
moveoption1=[-1,+1,0,0]
moveoption2=[0,0,-1,+1]
k=0
e=0.1
map.mapprint()
while k<200:
    sx = startx
    sy = starty
    s = map.states[sx][sy]
    searchlist=[]
    actionlist=[]
    while map.isterminal(s)==0:
        searchlist.append(s)
        ra=random.random()
        mvablist=[]
        for i in range(4):
            if s.moveable[i]==1:
                mvablist.append(i)
        if ra>e:
