from juego import Juego
import graf

pyglet.app.run()

g = Graf()

while 1:
    g.graf()

p = Juego()
p.show()

while 1:
    input = raw_input('Ingrese direccion:')
    print('')

    if input == "l":
        p.moveLeft()
    elif input == "r":
        p.moveRigth()
    elif input == "u":
        p.moveUp()
    elif input == "d":
        p.moveDown()
    elif input == "q":
        break
    
    p.show()
    print('')