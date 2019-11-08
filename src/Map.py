from State import State


class Map:
    def __init__(self, file):
        self.states = []
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

    def mapprint(self):
        for i in range(len(self.states)):
            for j in range(len(self.states[i])):
                print(self.states[i][j].type, end=' ')
            print()
