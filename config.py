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




import random, time, math

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

    def loop(self, c):
        ops = []
        while True:
            n = random.randrange(1, self.max_steps)
            for i in xrange(0, n):
                side = random.choice([0,1,2,3,4,5])
                d    = random.choice([-1, 1])
                ops.append((side, d))
                c.rotate(side, d)
                c.update()
                time.sleep(self.unsolve_delay)
            time.sleep(self.unsolved_delay)
            while ops != []:
                (side, d) = ops.pop()
                c.rotate(side, -d)
                c.update()
                time.sleep(self.solve_delay)
            time.sleep(self.solved_delay)

class Test:
    def loop(self, c):
        def f(s, x, y):
            (r, g, b) = Cube.colors[s]
            return ((r / 4.0)*(x+y),(g/4.0)*(x+y),(b/4.0)*(x+y))
        c.colorize(f)

def dist((x1,y1,z1),(x2,y2,z2),(xc,yc,zc)):
    m = math.sqrt(xc**2 + yc**2 + zc**2)
    return math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2) / m

class Test2:
    def loop(self, c):
        w = (0, 0, 0)
        wd = (0.02, -0.03, 0.01)
        while True:
            w = (w[0] + wd[0], w[1] + wd[1], w[2] + wd[2])
            def p(v):
                return (1.0-v)**((math.sin(w[0] / 10)+1.2)*1.5)
            def f(s, x, y):
                return ( p(dist(c.pos(s, x, y), (0, math.sin(w[0])*1.5, math.cos(w[0])*1.5), (3.0, 3.0, 3.0))),
                         p(dist(c.pos(s, x, y), (math.sin(w[1])*1.5, 0, math.cos(w[1])*1.5), (3.0, 3.0, 3.0))),
                         p(dist(c.pos(s, x, y), (math.sin(w[2])*1.5, math.cos(w[2])*1.5, 0), (3.0, 3.0, 3.0))))    
            c.colorize(f)

class Fire:
    def loop(self, c):
        n = 3
        part = []
        while True:
            if len(part) < n:
                part.append( ( random.uniform(-1.5, 1.5), -3.0, random.uniform(-1.5, 1.5), random.uniform(0, 0.03)) )
            part = [ ( x, y + dy, z, dy) for (x, y, z, dy) in part if y <= 3.0 ]
            def f(s, x, y):
                r = 0
                g = 0
                b = 0
                for (xp, yp, zp, _) in part:
                    r = r + (1.0 - dist(c.pos(s, x, y), (xp, yp, zp), (6.0, 6.0, 6.0)))**3
                    g = g + (1.0 - dist(c.pos(s, x, y), (xp, yp, zp), (6.0, 6.0, 6.0)))**4
                    b = b + (1.0 - dist(c.pos(s, x, y), (xp, yp, zp), (6.0, 6.0, 6.0)))**5                
                return (min(r, 1.0), min(g, 1.0), min(b, 1.0))
            c.colorize(f)



class Shell:
    def loop(self, c):
        import IPython
        IPython.embed()

