import random
from Map import Map

map = Map('data.txt')
goalx = 5
goaly = 7
startx = 2
starty = 0
moveoption1 = [-1, +1, 0, 0]
moveoption2 = [0, 0, -1, +1]
k = 0
e = 0.1
alpha=1
gama=0.9
map.mapprint()
while k < 200:
    sx = startx
    sy = starty
    s = map.states[sx][sy]
    while map.isterminal(s) == 0:
        ra = random.random()
        mvablist = []
        for i in range(4):
            if s.moveable[i] == 1:
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
