import random
from Map import Map



map = Map('data.txt')
goalx = 0
goaly = 3
startx = 1
starty = 0
moveoption1 = [-1, +1, 0, 0]
moveoption2 = [0, 0, -1, +1]
k = 0
e = 0.1
alpha=0.5
gama=0.9
while k < 2:
    sx = startx
    sy = starty
    s = map.states[sx][sy]
    map.refreshvisit()
    while map.isterminal(s) == 0:
        print(s.locationx,' ',s.locationy)
        map.visited[s.locationx][s.locationy]=1
        ra = random.random()
        mvablist = []
        for i in range(4):
            if s.moveable[i] == 1 and map.visited[s.locationx+moveoption1[i]][s.locationy+moveoption2[i]]==0:
                mvablist.append(i)
        if ra > e:
            maxi = 0
            for ii in range(len(mvablist)):
                if s.q[mvablist[ii]] > s.q[mvablist[maxi]]:
                    maxi = ii
            maxm = mvablist[maxi]
            s1 = map.states[s.locationx + moveoption1[maxm]][s.locationy + moveoption2[maxm]]
        else:
            maxm = mvablist[random.randint(0, len(mvablist) - 1)]
            s1 = map.states[s.locationx + moveoption1[maxm]][s.locationy + moveoption2[maxm]]

        mvablist1 = []
        for i in range(4):
            if s1.moveable[i] == 1 and map.visited[s1.locationx+moveoption1[i]][s1.locationy+moveoption2[i]]==0:
                mvablist1.append(i)
        if map.isterminal(s1)==1:
            qs1=50
        else:
            qs1=0
            for ii in range(len(mvablist1)):
                if s1.q[mvablist1[ii]] > qs1:
                    qs1=s1.q[mvablist1[ii]]
        qs=s.q[maxm]
        if map.isterminal(s1)==1:
            if s1.locationx==goalx and s1.locationy==goaly:
                r=50
            else:
                r=-30
        else:
            r=-1
        s.q[maxm]=(1-alpha)*qs+alpha*(r+gama*qs1)
        s=s1
        if map.isterminal(s)==1:
            print(s.locationx, ' ', s.locationy)
    k+=1
    map.mapprint()
    print()