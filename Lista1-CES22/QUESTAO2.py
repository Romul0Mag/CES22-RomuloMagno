#questao 2
import turtle


def draw_poly(t, n, sz):
    '''desenha um poligono de n lados regular de lado sz'''

    t.pensize(4)
    t.pencolor("hotpink")

    for i in range(n):
        t.forward(sz)
        t.left(360/n)


wn = turtle.Screen()

tess = turtle.Turtle()

wn.bgcolor("lightgreen")

wn.title("Questão 2")

draw_poly(tess, 8, 50)

wn.mainloop()