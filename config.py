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




