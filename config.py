# -*- coding: utf-8 -*-

class Artnet:
    # Soll gesendet werden?
    enabled = True
    # An welche IP?
    ip = "127.0.0.1"
    # An welchen Port?
    port = 10000

class Display:
    # Grafische Darstellung des Würfels zu Debugging-Zwecken?
    enabled = True
    width = 400
    height = 400
    bgcolor = (0.2, 0.2, 0.2)

class Cube:
    # Farben der Seiten des Würfels (Rot, Grün, Blau)
    colors = [ (0, 0, 1),   # Blau
               (0, 1, 0),   # Grün
               (1, 0, 0),   # Rot
               (1, 1, 0),   # Gelb
               (1, 0.5, 0), # Orange
               (1, 1, 1) ]  # Weiß

def set_patch(patch):
    patch[ 0 ][ 0 ][ 0 ] =  0
    patch[ 0 ][ 1 ][ 0 ] =  5
    patch[ 0 ][ 2 ][ 0 ] =  10
    patch[ 0 ][ 0 ][ 1 ] =  15
    patch[ 0 ][ 1 ][ 1 ] =  20
    patch[ 0 ][ 2 ][ 1 ] =  25
    patch[ 0 ][ 0 ][ 2 ] =  30
    patch[ 0 ][ 1 ][ 2 ] =  35
    patch[ 0 ][ 2 ][ 2 ] =  40
    patch[ 1 ][ 0 ][ 0 ] =  45
    patch[ 1 ][ 1 ][ 0 ] =  50
    patch[ 1 ][ 2 ][ 0 ] =  55
    patch[ 1 ][ 0 ][ 1 ] =  60
    patch[ 1 ][ 1 ][ 1 ] =  65
    patch[ 1 ][ 2 ][ 1 ] =  70
    patch[ 1 ][ 0 ][ 2 ] =  75
    patch[ 1 ][ 1 ][ 2 ] =  80
    patch[ 1 ][ 2 ][ 2 ] =  85
    patch[ 2 ][ 0 ][ 0 ] =  90
    patch[ 2 ][ 1 ][ 0 ] =  95
    patch[ 2 ][ 2 ][ 0 ] =  100
    patch[ 2 ][ 0 ][ 1 ] =  105
    patch[ 2 ][ 1 ][ 1 ] =  110
    patch[ 2 ][ 2 ][ 1 ] =  115
    patch[ 2 ][ 0 ][ 2 ] =  120
    patch[ 2 ][ 1 ][ 2 ] =  125
    patch[ 2 ][ 2 ][ 2 ] =  130
    patch[ 3 ][ 0 ][ 0 ] =  135
    patch[ 3 ][ 1 ][ 0 ] =  140
    patch[ 3 ][ 2 ][ 0 ] =  145
    patch[ 3 ][ 0 ][ 1 ] =  150
    patch[ 3 ][ 1 ][ 1 ] =  155
    patch[ 3 ][ 2 ][ 1 ] =  160
    patch[ 3 ][ 0 ][ 2 ] =  165
    patch[ 3 ][ 1 ][ 2 ] =  170
    patch[ 3 ][ 2 ][ 2 ] =  175
    patch[ 4 ][ 0 ][ 0 ] =  180
    patch[ 4 ][ 1 ][ 0 ] =  185
    patch[ 4 ][ 2 ][ 0 ] =  190
    patch[ 4 ][ 0 ][ 1 ] =  195
    patch[ 4 ][ 1 ][ 1 ] =  200
    patch[ 4 ][ 2 ][ 1 ] =  205
    patch[ 4 ][ 0 ][ 2 ] =  210
    patch[ 4 ][ 1 ][ 2 ] =  215
    patch[ 4 ][ 2 ][ 2 ] =  220
    patch[ 5 ][ 0 ][ 0 ] =  225
    patch[ 5 ][ 1 ][ 0 ] =  230
    patch[ 5 ][ 2 ][ 0 ] =  235
    patch[ 5 ][ 0 ][ 1 ] =  240
    patch[ 5 ][ 1 ][ 1 ] =  245
    patch[ 5 ][ 2 ][ 1 ] =  250
    patch[ 5 ][ 0 ][ 2 ] =  255
    patch[ 5 ][ 1 ][ 2 ] =  260
    patch[ 5 ][ 2 ][ 2 ] =  265

class Solver:
    # Wieviele Schritte wird der Würfel maximal randomisiert?
    max_steps = 20
    # Pause zwischen Schritten beim lösen
    solve_delay = 0.5
    # Pause zwischen Schritten beim randomisieren
    unsolve_delay = 0.5
    # Länge Pause nach Lösung
    solved_delay = 1.0
    # Länge Pause nach Randomisierung
    unsolved_delay = 1.0




