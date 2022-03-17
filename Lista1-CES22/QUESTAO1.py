#questao 1
import turtle


def draw_square(t, sz):
    '''desenha um quadrado de lado sz'''

    t.pensize(4)
    t.pencolor("hotpink")
    for i in range(4) :
        t.forward(sz)
        t.left(90)


def draw_multiple_squares(t, sz, n):
    '''desenha quadrados de lado sz, 2sz, 3sz, ..., n*sz, com o mesmo centro'''

    for i in range(n) :
        draw_square(t, sz*(i+1))
        v = t.position()
        t.up()
        t.goto(v - (sz/2, sz/2))
        t.down()


wn = turtle.Screen()

tess = turtle.Turtle()

wn.bgcolor("lightgreen")

wn.title("Questão 1")

draw_multiple_squares(tess, 20, 5)

wn.mainloop()