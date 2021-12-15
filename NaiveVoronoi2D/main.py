import sys
import random
import math
import pygame
from pygame.locals import QUIT

pygame.init()
size = (400, 400)
window = pygame.display.set_mode((size[0], size[1]))
window.fill((100, 100, 100))
points = [[[300, 150], (255, 0, 0)], [[200, 100], (0,255,0)], [[150, 350], (0, 0, 255)], [[200, 200], (255, 255, 0)], [[100, 270], (0, 255, 255)]]
pygame.display.set_caption('Voronoi Diagram')

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # posx, posy = pygame.mouse.get_pos()
            # point = [positions, color] COMMENT
            # points.append([[posx, posy], (random.randint(1, 254), random.randint(1, 254), random.randint(1, 254))])
            for point in points:
                pygame.draw.circle(window, (255, 0, 0), (point[0][0], point[0][1]), 5)

            for x in range(size[0]):
                for y in range(size[1]):
                    if window.get_at((x, y))[:-1] != (255, 0, 0):
                        distancias = []
                        for i in points:
                            distancia = math.sqrt((x - i[0][0]) ** 2 + (y - i[0][1]) ** 2), (155,155,155)
                            distancias.append(distancia)

                        distanciaMinima = min(distancias)
                        # Asignamos el color de la minima distancia
                        window.set_at((x, y), distanciaMinima[1])

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()