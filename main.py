from juego import Juego
import pyglet
from pyglet.gl import *
from pyglet import clock
from pyglet.window import key
from numeros import numeros

window = pyglet.window.Window()
clock.set_fps_limit(60)
j = Juego()
j.ant = j.tablero.copy()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.B:
        j.tablero = j.ant
    
    j.ant = j.tablero.copy()
    
    if symbol == key.LEFT:
        j.moveLeft()
    elif symbol == key.RIGHT:
        j.moveRigth()
    elif symbol == key.UP:
        j.moveUp()
    elif symbol == key.DOWN:
        j.moveDown()

@window.event
def on_draw():
    clock.tick()

    mapa = j.tablero

    mx = window.width // 2
    my = window.height // 2

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glBegin(GL_QUADS)
    glColor3f(0.3,0.3,0.3)
    glVertex2f(mx-90, my+90)
    glVertex2f(mx+95, my+90)
    glVertex2f(mx+95, my-95)
    glVertex2f(mx-90, my-95)
    glEnd()

    corrimiento_y = 85

    for linea in mapa:
        corrimiento_x = -85

        for pieza in linea:
            corner_x = mx + corrimiento_x
            corner_y = my + corrimiento_y

            glBegin(GL_QUADS)

            glColor3f(*numeros[str(pieza)])
            glVertex2f(corner_x, corner_y)
            glVertex2f(corner_x+40, corner_y)
            glVertex2f(corner_x+40, corner_y-40)
            glVertex2f(corner_x, corner_y-40)
            glEnd()

            if pieza != 0:
                label = pyglet.text.Label(
                    str(pieza),
                    font_name='Times New Roman',
                    font_size=10,
                    x=corner_x+20, y=corner_y-20,
                    anchor_x='center', anchor_y='center'
                )
                label.draw()
                label.delete()

            corrimiento_x += 45

        corrimiento_y -= 45

    #print score
    corner_x = mx + 115
    corner_y = my + 150

    glColor3f(0.5, 0.1, 0.1)
    glBegin(GL_QUADS)
    glVertex2f(corner_x, corner_y)
    glVertex2f(corner_x+100, corner_y)
    glVertex2f(corner_x+100, corner_y-20)
    glVertex2f(corner_x, corner_y-20)
    glEnd()

    label = pyglet.text.Label(
        'Score: ' + str(j.score),
        font_name='Times New Roman',
        font_size=10,
        x=corner_x+10, y=corner_y-10,
        anchor_x='left', anchor_y='center'
    )
    label.draw()
    label.delete()

pyglet.app.run()