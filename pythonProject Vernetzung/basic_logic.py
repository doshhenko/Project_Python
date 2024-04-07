import math


# die in jedem Algorithmus verwendete Programmlogik
# suchen die Radien jedes Punktes (dh die Entfernung vom Mittelpunkt des Kreises zu den Punkten)
def get_radius_list(current_points):
    # initialisieren eine leere Liste
    radius_list = []
    # eine Schleife, in der alle aktuellen Punkte durchlaufen werden
    for i in range(0, len(current_points[0])):
        # speichern ihre Koordinaten
        x = current_points[0][i]
        y = current_points[1][i]
        # verwenden den Satz des Pythagoras, um die Entfernung zu finden (Hypotenuse)
        # wobei 0,5 (was von der x- und y-Koordinate weggenommen wird) die Koordinaten des Kreises nach dem Offset sind
        # von der unteren linken Ecke zur Mitte des stddraw-Fensters : (0,5;0,5)
        distance_from_center = get_distance(x, y, 0.5, 0.5)
        # schreiben die gefundenen Radien (Entfernungen von Punkten zum Zentrum) in die Liste auf
        radius_list.append(distance_from_center)
    # zur Verwendung zurückgeben
    return radius_list


# wir haben einen Teil der "Logik" aus einer großen Funktion herausgenommen,
# um sie zum Beispiel in algorithm1 separat zu verwenden
def get_distance(x0, y0, x1, y1):
    # Eine Funktion, die mit Segmenten funktioniert, sodass wir die Kathete zwischen zwei Punkten finden
    # und schließen Sie ihre Differenz in ein Quadrat ein
    dist = math.sqrt(pow(x1 - x0, 2) + pow(y1 - y0, 2))
    return dist

# Interaktion mit dem Benutzer, wo er eine nicht negative Anzahl von Punkten eingeben muss
def get_points_amount():
    while True:
        points_amount = input("Geben Sie die Punktanzahl an: ")
        try:
            points_amount_num = int(points_amount)
        except ValueError:
            print("Keine richtige Angabe, Zahl soll gegeben sein")
        else:
            if points_amount_num < 0:
                print("Keine richtige Angabe, positive Zahl soll gegeben sein")
            else:
                print(f"Sie haben der Zahl {points_amount_num} gegeben")
                return points_amount_num
