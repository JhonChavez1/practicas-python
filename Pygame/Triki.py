import pygame
import os

# Inicialización de Pygame y recursos
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Triki")

fondo = pygame.image.load('Static/fondo.png')
circulo = pygame.image.load('Static/circulo.png')
equis = pygame.image.load('Static/equis.png')

fondo = pygame.transform.scale(fondo, (450, 450))
circulo = pygame.transform.scale(circulo, (125, 125))
equis = pygame.transform.scale(equis, (125, 125))

coordenadas = [[(0,0), (0,0), (0,0)],
               [(0,0), (0,0), (0,0)],
               [(0,0), (0,0), (0,0)]]

tablero = [['', '', ''],
           ['', '', ''],
           ['', '', '']]

turno = 'X'
game_over = False
clock = pygame.time.Clock()

# dibujar el tablero
def dibujar_tablero():
    screen.blit(fondo, (0, 0))
    for fila in range(3):
        for columna in range(3):
            X = columna * 150 +12
            Y = fila * 150 +12
            if tablero[fila][columna] == 'X':
                screen.blit(equis, (X, Y))
            elif tablero[fila][columna] == 'O':
                screen.blit(circulo, (X, Y))

def verificar_ganador():
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != '':
            return tablero[i][0]
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != '':
            return tablero[0][i]
        
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != '':
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != '':
        return tablero[0][2]
    return None


while not game_over:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_x, mouse_y = event.pos
            fila = mouse_y // 150
            columna = mouse_x // 150

            if tablero[fila][columna] == '':
                tablero[fila][columna] = turno
                turno = 'O' if turno == 'X' else 'X'
    dibujar_tablero()

    ganador = verificar_ganador()
    if ganador:
        print(f"Ganador: {ganador}")
        game_over = True

    pygame.display.update()

pygame.quit()
               
