import time

import color
import stddraw
import basic_logic
import circle_and_points


# Zeichne die inneren Ringe (Markierung)
def draw_many_internal_circles(amount):
    stddraw.setPenColor(color.BLACK)
    # Ein Zyklus, in dem wir Ringe in einer Menge von 1 bis amount + 1 zeichnen
    # (da die Anzahl der Ringe nicht den letzten enthält)
    for i in range(1, amount + 1):
        # Zeichnen einen Kreis mit x-, y-Koordinaten und einem Radius
        stddraw.circle(0.5, 0.5, calculate_internal_circle_radius(amount, i))
        stddraw.show(10)


# betrachten den Radius jedes Rings bei einer bestimmten Anzahl von Ringen
def calculate_internal_circle_radius(amount, number):
    # Der Radius des größten Kreises wird durch die Anzahl aller Ringe geteilt, +1
    # (da die Anzahl der Ringe nicht den letzten enthält) und mit der Nummer multipliziert werden
    return (0.5 / (amount + 1)) * number


# Nimmt Punkte, Radien und die Anzahl der inneren Kreise ein
def points_classification(points_to_classify, radii_of_points, amount_of_internal_circles):
    # Initialisieren eine leere Liste
    points_with_radii = []
    for i in range(0, len(points_to_classify[0])):
        # Danach fügen die Punkte zusammen mit ihren Radien der Liste nacheinander hinzu
        points_with_radii.append((points_to_classify[0][i], points_to_classify[1][i], radii_of_points[i]))
    classified_points_with_radii = []
    # In einer Schleife werden alle Ringe durchlaufen, innerhalb jeder Iteration der Schleife fügen wir der Liste
    # der klassifizierten Punkte mit dem Radius eine leere Liste hinzu,
    # um dann Punkte hinzuzufügen, die zum aktuellen Ring gehören
    for i in range(0, amount_of_internal_circles + 1):
        # fügen der Liste leere Listen hinzu (planen die Struktur für das weitere Ausfüllen)
        classified_points_with_radii.append([])
        # Aktuelle Einschränkung des äußeren Kreises; schreiben die Variable in den aktuellen Radius des Rings
        current_external_circle_radius = calculate_internal_circle_radius(amount_of_internal_circles, i + 1)
        # Aktuelle Einschränkung des inneren Kreises
        current_internal_circle_radius = calculate_internal_circle_radius(amount_of_internal_circles, i)
        # Radien von inneren Kreisen zählen
        # Ein Zyklus, in dem alle Punkte durchlaufen werden, um sie zu klassifizieren
        for j in range(0, len(points_with_radii)):
            # in jeder Phase des Zyklus berechnen wir den äußeren Radius
            # wenn der Punkt größer als der aktuelle innere Radius ist und kleiner oder gleich dem äußeren Radius ist,
            # dann fügen wir es der Liste der Punkte hinzu, die zu einem bestimmten Ring gehören
            if current_external_circle_radius >= points_with_radii[j][2] > current_internal_circle_radius:
                classified_points_with_radii[i].append(points_with_radii[j])
    return classified_points_with_radii


# Akzeptiert klassifizierte Punkte
def sort_points(classified_points_to_sort):
    # Initialisieren eine leere Liste
    sorted_points_list = []
    # Ein Zyklus, in dem alle durch Ringe klassifizierten Punkte durchlaufen werden
    for i in range(0, len(classified_points_to_sort)):
        # fügen der Liste leere Listen hinzu (planen die Struktur für das weitere Ausfüllen)
        sorted_points_list.append([])
        # Auswahl des Rings
        for _ in range(9):
            # Fügen der Liste 9 leere Listen hinzu, die zu jedem der 9 geplanten Bereiche gehören
            sorted_points_list[i].append([])
            # Durchlauf durch alle durch Ringe klassifizierten Punkte
        for j in range(0, len(classified_points_to_sort[i])):
            # Der Bereichswert ist der Wert der Funktion define_area, in der wir zuerst einen Punkt übergeben
            # (x- und y-Werte eines Punktes im kleinsten Ring), dann sind alle anderen Punkte in der Schleife
            area = define_area(classified_points_to_sort[i][j][0], classified_points_to_sort[i][j][1])
            # Fügen Sie einen Punkt zu einem bestimmten Bereich und einem bestimmten Ring hinzu,
            # der dort angekommen ist,
            # wobei i die Wahl des Rings von klein zu groß ist, area -1 ist der Index von 1 bis 9
            # (oder von 0 bis 8) (also subtrahiere eins)
            sorted_points_list[i][area - 1].append(classified_points_to_sort[i][j])

    # In jedem der geraden Bereiche nach Kotangens sortieren (insgesamt 4)
    for i in range(0, len(sorted_points_list)):
        for j in range(0, 4):
            # sortieren nach Kotangens mit einem negativen Punktwert mit den Koordinaten x, y
            sorted_points_list[i][j * 2 + 1].sort(key=lambda d: - calculate_ctg(d[0], d[1]))
    return sorted_points_list


def define_area(x, y):
    # Koordinatenwerte konvertieren: die Skalierung ändert sich um das Doppelte
    # der Schnittpunkt der Achsen des Koordinatensystems bewegt sich von der unteren linken Ecke (stddraw.window)
    # zum Mittelpunkt des Kreises
    x1 = (x - 0.5) * 2
    y1 = (y - 0.5) * 2
    # Bereich 1, Achse Abzisse +
    if y1 == 0 and x1 > 0:
        return 1
    # Bereich 2, Erstes Viertel
    if y1 > 0 and x1 > 0:
        return 2
    # Bereich 3, Achse Ordinate +
    if y1 > 0 and x1 == 0:
        return 3
    # Bereich 4, Zweites Viertel
    if y1 > 0 > x1:
        return 4
    # Bereich 5, Achse Abzisse -
    if y1 == 0 and x1 < 0:
        return 5
    # Bereich 6, Drittes Viertel
    if y1 < 0 and x1 < 0:
        return 6
    # Bereich 7, Ordinatachse -
    if y1 < 0 and x1 == 0:
        return 7
    # Bereich 8, Viertes Viertel
    if y1 < 0 < x1:
        return 8
    # Bereich 9, Punkt (0;0)
    if y1 == 0 and x1 == 0:
        return 9


# Die Formel zur Berechnung des Kotangens
def calculate_ctg(x, y):
    x1 = (x - 0.5) * 2
    y1 = (y - 0.5) * 2
    # berechnen Kotangens
    return x1 / y1


def connect_points(sorted_points):
    # Initialisieren eine leere Liste
    points_in_row = []
    stddraw.setPenColor(color.BLUE)
    # Bestimmen die Dicke der Verbindungslinie
    stddraw.setPenRadius(0.003)
    # Eine Schleife, in der wir auf den Ring nach Index i zugreifen
    for i in range(0, len(sorted_points)):
        # Dann wenden wir uns innerhalb jedes Rings nach dem Index j an die Bereiche
        for j in range(0, 9):
            # In jedem Bereich werden Punkte am Index p gespeichert
            # In diesem Zyklus durchlaufen wir alle Punkte eines bestimmten Rings (beginnend mit dem letzten)
            # und eines Bereichs
            for p in range(0, len(sorted_points[len(sorted_points) - i - 1][j])):
                # Fügen jeden Punkt zur Liste hinzu
                points_in_row.append(sorted_points[len(sorted_points) - i - 1][j][p])
    for i in range(0, len(points_in_row) - 1):
        # Koordinaten des 0. Punktes
        x0 = points_in_row[i][0]
        y0 = points_in_row[i][1]
        # Die Koordinaten des 1. Punktes
        x1 = points_in_row[i + 1][0]
        y1 = points_in_row[i + 1][1]
        # Zeichnen eine Linie zwischen den Koordinaten 0 und 1
        stddraw.line(x0, y0, x1, y1)
        stddraw.show(10)

# Interaktion mit dem Benutzer, wo er eine nicht negative Anzahl von Ringen eingeben muss
def get_internal_circles_amount():
    while True:
        internal_circles_amount = input("Geben Sie die Anzahl der inneren Ringe an: ")
        try:
            internal_circles_amount_num = int(internal_circles_amount)
        except ValueError:
            print("Keine richtige Angabe, Zahl soll gegeben sein")
        else:
            if internal_circles_amount_num < 0:
                print("Keine richtige Angabe, positive Zahl soll gegeben sein")
            else:
                print(f"Sie haben der Anzahl der inneren Ringe {internal_circles_amount_num} gegeben")
                return internal_circles_amount_num


if __name__ == '__main__':
    points_amount_num = basic_logic.get_points_amount()
    internal_circles_amount = get_internal_circles_amount()
    points = circle_and_points.draw_circle_and_points(points_amount_num)
    draw_many_internal_circles(internal_circles_amount)
    radii = basic_logic.get_radius_list(points)
    classified_points = points_classification(points, radii, internal_circles_amount)
    final_sorted_list = sort_points(classified_points)
    time.sleep(3)
    connect_points(final_sorted_list)
    time.sleep(1000)
