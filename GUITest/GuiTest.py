import time


objectList = []

WIDTH = 20
HEIGHT = 10
BODY = '#'


def addStr(n, x, y):
    for i,c in enumerate(n):
        addObject(c, x, y+i)

def addRect(n, w, h, x, y):
    for a in range(h):
        addObject(n, x+a, y)
        addObject(n, x+a, y+w-1)
    for b in range(w):
        addObject(n, x, y+b)
        addObject(n, x+h-1, y+b)


def render():
    line = ''
    gui = [[ ' ' for x in range(WIDTH)] for y in range(HEIGHT)]
    for o in objectList:
        gui[o[1]][o[2]] = o[0]
    line += ' '+'--'* WIDTH + '\n'
    for g in gui:
        line += '|'
        for u in g:
            line += u + ' '
        line += '|\n'
    line += ' '+'--'* WIDTH
    print line

def cls():
    print '\n'* 100
    
def addObject(n, x, y):
    objectList.append([n, x, y])
    return len(objectList)-1


class Object:
        
    def __init__(self, n, x, y):
        self.index = addObject(n,x,y)
        self.type = n

    def move(self, dx, dy):
        objectList[self.index][1] += dx
        objectList[self.index][2] += dy

    def delete(self):
        objectList[self.index] = [' ', 0,0]

class StrObject:
    
    def __init__(self, n, x, y):
        self.index = []
        for i,c in enumerate(n):
            self.index.append(addObject(c, x, y+i))

    def move(self, dx, dy):
        for i in self.index:
            objectList[i][1] += dx
            objectList[i][2] += dy

    def delete(self):
        for i in self.index:
            objectList[i] = [' ', 0,0]

obj = Object('x', 5, 0)

for a in range(15):
    obj.move(0,1)
    time.sleep(0.5)
    cls()
    render()
    

    
