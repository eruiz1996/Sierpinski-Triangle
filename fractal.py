# -*- coding: utf-8 -*-
import sys
import pygame
from math import sqrt

pygame.init()
# pantalla
ANCHO, ALTO = 800, 650
superficie=pygame.display.set_mode( (ANCHO, ALTO) )
pygame.display.set_caption('Fractal Sierpinski')
# colores
azul, negro = (0,0,255), (0,0,0)

class Punto():

	def __init__(self, x, y):
		self.x = int(x)
		self.y = int(y)

	def __str__(self):
		return f"Punto: ({self.x}, {self.y})"

	def punto_medio(self, p):
		medio = Punto((self.x + p.x)//2, (self.y + p.y)//2)
		return medio

	def recta(self, p):
		pygame.draw.line(superficie, azul, (self.x,self.y), (p.x,p.y), 2)

	def distancia(self,p):
		return int(sqrt((self.x - p.x)**2 + (self.y - p.y)**2))

def triangulo(p1, p2, p3):
	""" Dados tres puntos hace un triángulo """
	p1.recta(p2)
	p2.recta(p3)
	p3.recta(p1)

def clave(p1, p2, p3):
	""" Dados 3 puntos saca sus puntos medios y hace un triángulo con ellos """
	m1 = p1.punto_medio(p2)
	m2 = p2.punto_medio(p3)
	m3 = p3.punto_medio(p1)
	triangulo(m1,m2,m3)

def fractal(p1, p2, p3):
	""" función recursiva del fractal """
	if p1.distancia(p2) > 1:
		clave(p1,p2,p3)
		fractal(p1, p1.punto_medio(p2), p1.punto_medio(p3))
		fractal(p1.punto_medio(p2), p2, p2.punto_medio(p3))
		fractal(p1.punto_medio(p3), p2.punto_medio(p3), p3)
	else:
		return

A = Punto(325, 50)
B = Punto(50, 600)
C = Punto(600, 600)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	superficie.fill(negro) 

	# dibujamos el triángulo
	triangulo(A, B, C)
	# y mandamos llamar a la función fractal
	fractal(A, B, C)


	pygame.display.update()
