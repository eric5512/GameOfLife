import pygame
import random
import copy


class Cell:
    def __init__(self, x, y, w, h, act):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.act = act

    def draw(self, win):
        if self.act == 0:
            c = (255,255,255)
        else:
            c = (0,0,0)
        pygame.draw.rect(win, c, (self.x+1, self.y+1, self.w-1, self.h-1))

    def nextGen(self, suma):
        if suma == 3 and self.act == 0:
            self.act = 1
        elif (suma < 2 or suma > 3) and self.act == 1:
            self.act = 0


pygame.init()

sWidth = 500
sHeight = 500
res = 20
length = int(sWidth/res)

win = pygame.display.set_mode((sWidth,sHeight))
pygame.display.set_caption("Game of life")

indexs = [-1,0,1]
auxCells = []
cells = []
for i in range(length):
    cells.append([])
    for j in range(length):
        if random.randint(0,5) == 0:
            a = 1
        else:
            a = 0
        cells[i].append(Cell(j*res, i*res, res, res, a))


run = True
while run:
    pygame.time.delay(50)
    pygame.draw.rect(win,(255,255,255),(0,0,sWidth,sHeight))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    #Comprovar la siguiente generacion
    auxCells = copy.deepcopy(cells)
    for i in range(length):
        for j in range(length):
            suma = 0
            for g in indexs:
                for h in indexs:
                    indexI = (i + g + length) % length
                    indexJ = (j + h + length) % length
                    if not (g == 0 and h == 0):
                        suma += auxCells[indexI][indexJ].act
            cells[i][j].nextGen(suma)
            


    #Draw section
    for row in cells:
        for i in row:
            i.draw(win)

    pygame.display.update()


pygame.quit()