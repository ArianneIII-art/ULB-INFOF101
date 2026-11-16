# by ArianneIII-art on ghithub and codeberg

# version sans vérification, ni la fonction pseudo privé
import turtle

def init_window_and_position(x: int|float = 0, y: int|float = 0, speed: int = 6):
    """
    Permet de définir plusieur paramètre pour la fct flocon
    x et y: int|float   les coordonné de départ de la tortue
    speed : int         la vitesse de turtle (se référé a la doc de turtle.speed pour plus de détails)
    les valeur par défault sont le comportement que la documentation décris comme le défaut pour turtle
    """
    turtle.showturtle()
    turtle.speed(speed)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def flocon(d: float, seuil: float) -> None:
    """
    Trace une a proximation de une approximation de la courbe de von Koch avec le module turtle de python
    d:      int distance totale parcourue
    seuil:  int d a atteindre avant de tracer l'aproximation
    """
    if d/3 < seuil:
        turtle.forward(d/3)
        turtle.left(60)
        turtle.forward(d/3)
        turtle.right(120)
        turtle.forward(d/3)
        turtle.left(60)
        turtle.forward(d/3)
    else:
        flocon(d/3, seuil)
        turtle.left(60)
        flocon(d/3, seuil)
        turtle.right(120)
        flocon(d/3, seuil)
        turtle.left(60)
        flocon(d/3, seuil)

if __name__ == "__main__":
    distance_horizontal = 600
    seuil = 10
    offset = -(distance_horizontal/2)

    # met la vitesse au maximum et
    # positionne le cursuer pour que le centre de la feunetre soit le centre de la fractalle
    init_window_and_position(x=offset, speed=0)

    flocon(distance_horizontal, seuil)

    # keep the window open after the program ended
    turtle.mainloop()
