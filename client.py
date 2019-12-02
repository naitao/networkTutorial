import pygame
from network import Network
from player import Player

width = 500
heigh = 500
win = pygame.display.set_mode((width, heigh))
pygame.display.set_caption('Client')

#clientNumber = 0

'''
class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 3

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
        if keys[pygame.K_UP]:
            self.y += self.vel
        if keys[pygame.K_DOWN]:
            self.y -= self.vel
        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)

def read_pos(pos_str):
    print("old str:", pos_str)
    pos_str = pos_str.split(",")
    print("new str:", pos_str)
    return int(pos_str[0]), int(pos_str[1])

def make_pos(tup):
    print("tup: {}".format(tup))
    return str(tup[0]) + "," + str(tup[1])
'''
def redrawWindow(win, player, player2):
    win.fill((255,255,255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()

def main():
    run = True
    n = Network()
    p = n.getP()
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        p2 = n.send(p)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        redrawWindow(win, p, p2)

if __name__ == '__main__':
    main()