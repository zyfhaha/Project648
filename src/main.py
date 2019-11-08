from Map import Map


map=Map('data.txt')
goalx=5
goaly=7
k=0
map.mapprint()
while k<200:
    sx = 2
    sy = 0
    s = map.states[2][0]