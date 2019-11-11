from State import State


class Map:
    def __init__(self, file):
        self.states = []
        self.visited=[]
        x = 0
        with open(file, 'r') as f:
            for line in f:
                stateline = list([])
                p = list(line.split(' '))
                for y in range(len(p)):
                    st = State(x, y, int(p[y]))
                    stateline.append(st)
                self.states.append(stateline)
                x += 1
        self.sizex = len(self.states)
        self.sizey = len(self.states[0])
        for i in range(len(self.states)):
            for j in range(len(self.states[i])):
                if i == 0 or self.states[i - 1][j].type == 1:
                    self.states[i][j].moveable[0] = 0
                if j == 0 or self.states[i][j - 1].type == 1:
                    self.states[i][j].moveable[2] = 0
                if i == self.sizex - 1 or self.states[i + 1][j].type == 1:
                    self.states[i][j].moveable[1] = 0
                if j == self.sizey - 1 or self.states[i][j + 1].type == 1:
                    self.states[i][j].moveable[3] = 0

        for i in range(len(self.states)):
            lines=list([])
            for j in range(len(self.states[i])):
                lines.append(0)
            self.visited.append(lines)

    def isterminal(self,st):
        flag=1
        x=st.locationx
        y=st.locationy
        if st.moveable[0]==1 and self.visited[x-1][y]==0:
            flag=0
        if st.moveable[1]==1 and self.visited[x+1][y]==0:
            flag=0
        if st.moveable[2]==1 and self.visited[x][y-1]==0:
            flag=0
        if st.moveable[3]==1 and self.visited[x][y+1]==0:
            flag=0
        return flag

    def mapprint(self):
        moveoption1 = [-1, +1, 0, 0]
        moveoption2 = [0, 0, -1, +1]
        for i in range(len(self.states)):
            for j in range(len(self.states[i])):
                kp=list(self.states[i][j].q)
                kl=[round(iii,1) for iii in kp]
                for pp in range(4):
                    if self.states[i][j].moveable[pp]==0 or self.states[i][j].type==1:
                        kl[pp]='*'
                print(kl,end=' ')
            print()

    def refreshvisit(self):
        self.visited = []
        for i in range(len(self.states)):
            lines=list([])
            for j in range(len(self.states[i])):
                lines.append(0)
            self.visited.append(lines)

    def mprint(self):
        for i in range(len(self.states)):
            for j in range(len(self.states[i])):
                if self.states[i][j].type==1:
                    print('# ',end='')
                else:
                    print('  ',end='')
            print()