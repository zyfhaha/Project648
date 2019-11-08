from State import State


class Map:
    def __init__(self, file):
        self.states = []
        x = 0
        with open(file, 'r') as f:
            for line in f:
                stateline=list([])
                p = list(line.split(' '))
                for y in range(len(p)):
                    st = State(x,y,int(p[y]))
                    stateline.append(st)
                self.states.append(stateline)
                x+=1

    def mapprint(self):
        for i in range(len(self.states)):
            for j in range(len(self.states[i])):
                print(self.states[i][j].type,end=' ')
            print()