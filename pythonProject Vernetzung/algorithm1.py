import color
import stddraw
import circle_and_points
import basic_logic
import time


def sort_points_by_distance_from_center(current_points, distance):
    sorted_points = []
    # Beschreibt eine Schleife über die gesamte Länge der Liste
    # (distance - Liste der Abstände zwischen den Punkten und dem Mittelpunkt des Kreises)
    for i in range(0, len(distance)):
        # Fügen der leeren Liste sorted_points eine Karte mit drei Elementen hinzu,
        # wobei jedes Element ein Punkt mit x-, y-Koordinaten und der Entfernung zum Mittelpunkt des Kreises ist
        sorted_points.append((current_points[0][i], current_points[1][i], distance[i]))
    # Sortieren die Punkte in aufsteigender Reihenfolge mit der sort-Methode
    # unter der Bedingung, dass der Abstand zum Mittelpunkt des Kreises ausgewählt wird,
    # d.h distance (3 Element mit Index 2)
    sorted_points.sort(key=lambda x: x[2])
    return sorted_points


def draw_lines(current_coordinates):
    stddraw.setPenColor(color.BLUE)
    # Verbinden den ersten und zweiten Punkt
    stddraw.line(current_coordinates[0][0], current_coordinates[0][1], current_coordinates[1][0],
                 current_coordinates[1][1])
    stddraw.show(0.0)
    # Eine Schleife, die den Abstand vom dritten Punkt zu einem der beiden bereits ausgewählten Punkte überprüft
    for i in range(2, len(current_coordinates)):
        #  Der nächste Punkt mit den x-, y-Koordinaten Null und der Abstand zum Punkt beträgt 10
        #  (eine zufällige, unrealistische Zahl für eine Schleife,
        #  die genau größer ist als der Mindestabstand zwischen den Punkten)
        closest_point = (0, 0, 10)
        # Auswählen des nächsten Punkts in Schleife j
        for j in range(0, i):
            # gehen durch alle bereits beteiligten Punkte, um festzustellen, welcher der aktuellen Punkte näher ist
            distance_to_next_point = basic_logic.get_distance(current_coordinates[i][0], current_coordinates[i][1],
                                                              current_coordinates[j][0],
                                                              current_coordinates[j][1])
            if distance_to_next_point < closest_point[2]:
                # Legen die Koordinaten des nächsten Punktes fest, mit dem wir verbinden
                closest_point = (current_coordinates[j][0], current_coordinates[j][1], distance_to_next_point)
        # Punkte verbinden
        stddraw.line(current_coordinates[i][0], current_coordinates[i][1], closest_point[0], closest_point[1])
        stddraw.show(100)


if __name__ == '__main__':
    points_amount_num = basic_logic.get_points_amount()
    points = circle_and_points.draw_circle_and_points(points_amount_num)
    coordinates = sort_points_by_distance_from_center(points, basic_logic.get_radius_list(points))
    draw_lines(coordinates)
    time.sleep(100)
