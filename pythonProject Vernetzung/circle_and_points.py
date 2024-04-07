import time
import random

import color
import stddraw

# konstanten festlegen (Fenstergröße)
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000


# zeigen ein Fenster mit den angegebenen Parametern für Breite und Höhe an
def show_canvas(width, height):
    stddraw.setCanvasSize(width, height)
    stddraw.show(150)


# zeichnen einen Kreis mit einem Mittelpunkt in Koordinaten (0,5; 0,5) und einem Radius von 0,5
def draw_circle():
    stddraw.circle(0.5, 0.5, 0.5)
    stddraw.show(150)


# erstellen eine Liste von Punkten mit x- und y-Koordinaten
def create_points(amount):
    x_points_list = []
    y_points_list = []
    # fügen Sie einen Zähler hinzu
    i = 1
    # solange i kleiner oder gleich der Anzahl der Punkte ist
    while i <= amount:
        # zufällige Koordinaten angeben
        x = random.random()
        y = random.random()
        # wenn (x-0,5)^2 + (y-0,5)^2 <= 0,5^2 (die Gleichung des Kreises) wird ausgeführt
        # und der Punkt befindet sich innerhalb unseres Kreises oder auf seiner Linie, dann passt er zu uns
        if pow(x - 0.5, 2) + pow(y - 0.5, 2) <= pow(0.5, 2):
            # wenn die x- oder y-Koordinate als korrekt gilt, wird sie in die Liste geschrieben
            x_points_list.append(x)
            y_points_list.append(y)
            # der Zähler wird mit jedem geeigneten Punkt bis dahin um 1 erhöht,
            # bis i mehr amount wird und die Schleife nicht mehr funktioniert
            # für den Fall, dass der Punkt nicht zu uns passt (liegt außerhalb des Kreises),
            # erhöht sich der Zähler nicht
            i += 1
    # geben die Werte der Listen zur späteren Verwendung zurück
    return x_points_list, y_points_list


# zeichnen die Punkte
def draw_points(points):
    stddraw.setPenColor(color.MAGENTA)
    for i in range(0, len(points[0])):
        # zeichnen Punkte auf der Leinwand, ihre Anzahl entspricht der Länge von 1 Element im Array points
        # (x-Koordinaten und y-Koordinaten Siehe unten)
        stddraw.point(points[0][i], points[1][i])
        stddraw.show(0.0)


def draw_circle_and_points(amount):
    # erstellen Punkte in der Datenstruktur und setzen sie in eine Variable
    points = create_points(amount)
    show_canvas(WINDOW_WIDTH, WINDOW_HEIGHT)
    draw_circle()
    draw_points(points)
    time.sleep(1)
    return points
