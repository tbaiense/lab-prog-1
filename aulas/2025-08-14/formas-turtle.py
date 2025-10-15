import turtle
import random

t = turtle.Turtle()

tamanho = 10
t.speed(0)

def triangulo(tamanho):
    angulo = 120
    
    t.forward(tamanho)
    t.left(angulo)
    t.forward(tamanho)
    t.left(angulo)
    t.forward(tamanho)


def retangulo(tamanho):
    angulo = 90
    t.forward(tamanho)
    t.left(angulo)
    t.forward(tamanho)
    t.left(angulo)
    t.forward(tamanho)
    t.left(angulo)
    t.forward(tamanho)
    
    
def hexagono(tamanho):
    angulo = 60
    t.forward(tamanho)
    t.left(angulo)
    t.forward(tamanho)
    t.left(angulo)
    t.forward(tamanho)
    t.left(angulo)
    t.forward(tamanho)
    t.left(angulo)
    t.forward(tamanho)
    t.left(angulo)
    t.forward(tamanho)
    t.left(angulo)

turtle.colormode(255)
for i in range(10000):
    r = random.randrange(0,255)
    g = random.randrange(0,255)
    b = random.randrange(0,255)
    
    t.fillcolor((r, g, b))
    t.begin_fill()
    hexagono(tamanho)
    t.end_fill()
    t.teleport(r + b, g + b)

    

t.screen.mainloop()