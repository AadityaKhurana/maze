# we use Up, Down, Right Left
import random
import pygame, sys
from pygame.locals import *
import sys

order = ["up", "down", "right", "left"]
row = col = int(sys.argv[1])
width = 700
height = 700
path = [[1, 1]]
grid = {}
grid_directions_explored = {}
direction = "up"
for x in range(1, col + 1):
    for y in range(1, row + 1):
        grid[x, y] = [1, 1, 1, 1]
        grid_directions_explored[x, y] = []

x = 1
y = 1

while len(path) != row*col:
    direction = random.choice(order)
    if len(grid_directions_explored[x, y]) == 4:
        cindex = path.index([x, y])
        x = path[cindex+1][0]
        y = path[cindex+1][1]
        if [x, y] not in path:
            path.insert(0, [x, y])

    elif direction in grid_directions_explored[x, y]:
        pass
    else:
        grid_directions_explored[x, y].append(direction)
        if direction == "up" and y != 1 and [x, y-1] not in path:
            grid[x, y][0] = 0
            grid[x, y-1][1] = 0
            y= y-1
            path.insert(0, [x, y])
        if direction == "down" and y != row and [x, y+1] not in path:
            grid[x, y][1] = 0
            grid[x, y+1][0] = 0
            y= y+1
            path.insert(0, [x, y])
        if direction == "right" and x != col and [x+1, y] not in path:
            grid[x, y][2] = 0
            grid[x+1, y][3] = 0
            x = x+1
            path.insert(0, [x, y])
        if direction == "left" and x != 1 and [x-1, y] not in path:
            grid[x, y][3] = 0
            grid[x-1, y][2] = 0
            x= x-1
            path.insert(0, [x, y])


grid[1, 1][3] = 0
grid[col, row][2] = 0

# ---------------------------------------------------------------------------------------------------- UI

margin = 20
pygame.init()

screen=pygame.display.set_mode((width,height))

background=(49,49,45)
linecolour=(240, 152, 56)

screen.fill(background)

def draw_Square(x, y, hw, up = 0, down= 0, right=0, left= 0):
    if up == 1:
        pygame.draw.line(screen, linecolour, ((x-1)*hw + margin, (y-1)*hw + margin), ((x)*hw + margin, (y-1)*hw + margin), 2)
    if down == 1:
        pygame.draw.line(screen, linecolour, ((x-1)*hw + margin, (y)*hw + margin), ((x)*hw + margin, (y)*hw + margin), 2)
    if right == 1:
        pygame.draw.line(screen, linecolour, ((x)*hw + margin, (y-1)*hw + margin), ((x)*hw + margin, (y)*hw + margin), 2)
    if left == 1:
        pygame.draw.line(screen, linecolour, ((x-1)*hw + margin, (y-1)*hw + margin), ((x-1)*hw + margin, (y)*hw + margin), 2)

for xy , udrl in grid.items():
    hw = (width - 40)/col
    draw_Square(xy[0], xy[1], hw, up = udrl[0], down = udrl[1], right=udrl[2], left=udrl[3])

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()