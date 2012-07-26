import rubik, config, random, time, sys, math

def solve_loop(c):
    ops = []
    while True:
        n = random.randrange(1, config.Solver.max_steps)
        for i in xrange(0, n):
            side = random.choice(rubik.Cube.SIDES)
            d    = random.choice([-1, 1])
            ops.append((side, d))
            c.rotate(side, d)
            c.update()
            time.sleep(config.Solver.unsolve_delay)
        time.sleep(config.Solver.unsolved_delay)
        while ops != []:
            (side, d) = ops.pop()
            c.rotate(side, -d)
            c.update()
            time.sleep(config.Solver.solve_delay)
        time.sleep(config.Solver.solved_delay)

def test(c):
    def f(s, x, y):
        (r, g, b) = config.Cube.colors[s]
        return ((r / 4.0)*(x+y),(g/4.0)*(x+y),(b/4.0)*(x+y))
    c.colorize(f)

def dist((x1,y1,z1),(x2,y2,z2),(xc,yc,zc)):
    m = math.sqrt(xc**2 + yc**2 + zc**2)
    return math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2) / m

def test2(c):
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

def fire(c):
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

def shell(c):
    import IPython
    test(c)
    IPython.embed()

if __name__=="__main__":
    f = solve_loop
    if len(sys.argv) > 1:
        try:
            f = globals()[sys.argv[1]]
        except:
            pass
    rubik.Cube(f)

