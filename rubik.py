#from Cube import Cube
import copy
import config
import socket
import artnet

class Cube(object):

    F = 0
    L = 1
    R = 2
    T = 3
    D = 4
    B = 5

    NEIGHBOURS = {
        F : [ (L, 2, 2), (L, 2, 1), (L, 2, 0),
              (T, 0, 2), (T, 1, 2), (T, 2, 2),
              (R, 0, 0), (R, 0, 1), (R, 0, 2),
              (D, 2, 0), (D, 1, 0), (D, 0, 0) ],
        L : [ (B, 0, 0), (B, 0, 1), (B, 0, 2),
              (T, 0, 0), (T, 0, 1), (T, 0, 2),
              (F, 0, 0), (F, 0, 1), (F, 0, 2),
              (D, 0, 0), (D, 0, 1), (D, 0, 2) ],
        R : [ (F, 2, 2), (F, 2, 1), (F, 2, 0),
              (T, 2, 2), (T, 2, 1), (T, 2, 0),
              (B, 2, 2), (B, 2, 1), (B, 2, 0),
              (D, 2, 2), (D, 2, 1), (D, 2, 0) ],
        T : [ (B, 0, 2), (B, 1, 2), (B, 2, 2),
              (R, 2, 0), (R, 1, 0), (R, 0, 0),
              (F, 2, 0), (F, 1, 0), (F, 0, 0),
              (L, 2, 0), (L, 1, 0), (L, 0, 0) ],
        D : [ (F, 0, 2), (F, 1, 2), (F, 2, 2),
              (R, 0, 2), (R, 1, 2), (R, 2, 2),
              (B, 2, 0), (B, 1, 0), (B, 0, 0),
              (L, 0, 2), (L, 1, 2), (L, 2, 2) ],
        B : [ (D, 0, 2), (D, 1, 2), (D, 2, 2),
              (R, 2, 2), (R, 2, 1), (R, 2, 0),
              (T, 2, 0), (T, 1, 0), (T, 0, 0),
              (L, 0, 0), (L, 0, 1), (L, 0, 2) ]
        }
    
    SIDES = [ F, L, R, T, D, B]
    DIM = 3

    def update_backbuffer(self):
        self.bb_sides = [[[ self.sides[side][x][y]
                           for x in xrange(0, Cube.DIM)]
                          for y in xrange(0, Cube.DIM)]
                         for side in Cube.SIDES]

    def pos(self, s, x, y):
        if s == 0:
            return (y-1, (2-x)-1, 1.5)
        elif s == 5:
            return (y-1, x-1, -1.5)
        elif s == 1:
            return (-1.5, (2-x)-1, y-1)
        elif s == 2:
            return (1.5, (2-x)-1, (2-y)-1)
        elif s == 3:
            return (y-1, 1.5, x-1)
        else:
            return (y-1, -1.5, (2-x)-1)
    
    def __init__(self, fun):
        self.artnet_socket = None
        self.sides = [[[config.Cube.colors[side]
                        for _ in xrange(0, Cube.DIM)]
                       for _ in xrange(0, Cube.DIM)]
                      for side in Cube.SIDES]
        self.patch = [[[ None for _ in xrange(0, Cube.DIM) ]
                        for _ in xrange(0, Cube.DIM) ]
                       for _ in Cube.SIDES ]
        config.set_patch(self.patch)
        self.update_backbuffer()
        if config.Display.enabled:
            import glcube
            from thread import start_new_thread
            start_new_thread(fun, (self,))
            glcube.loop(self)
        else:
            fun(self)
            
            

    def update(self):
        self.update_backbuffer()
        if config.Artnet.enabled:
            self.artnet_send()

    def artnet_send(self):
        if self.artnet_socket == None:
            self.artnet_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        r = artnet.DmxPacket()
        p = 0
        for side in Cube.SIDES:
            for j in xrange(0, Cube.DIM):
                for i in xrange(0, Cube.DIM):
                    p = self.patch[side][i][j]
                    for c in xrange(0, 3):
                        r[p] = int(round(self.sides[side][i][j][c]*255))
                        p = p + 1
                    r[p] = 255
                    p = p + 1
                    r[p] = 0
        self.artnet_socket.sendto(r.encode(), (config.Artnet.ip, config.Artnet.port))                   

    def rotate_side(self, side):
        self.sides[side] = [[ self.sides[side][Cube.DIM-j-1][i]
                              for j in xrange(0, Cube.DIM) ]
                            for i in xrange(0, Cube.DIM) ]

    def rotate(self, side, dir=1):
        if dir == 1:
            self.rotate_side(side)
            new_sides = copy.deepcopy(self.sides)
            rlist = Cube.NEIGHBOURS[side]
            for i in xrange(0, 4*Cube.DIM):
                (sa, ax, ay) = rlist[i]
                (sb, bx, by) = rlist[(i + Cube.DIM) % (4*Cube.DIM)]
                new_sides[sb][by][bx] = self.sides[sa][ay][ax]
            self.sides = new_sides
        elif dir == -1:
            self.rotate(side, 1)
            self.rotate(side, 1)
            self.rotate(side, 1)

    def set(self, side, x, y, col):
        self.sides[side][x][y] = col

    def set_upd(self, side, x, y, col):
        self.set(side, x, y, col)
        self.update()

    def colorize(self, fun):
        for s in Cube.SIDES:
            for y in xrange(0, Cube.DIM):
                for x in xrange(0, Cube.DIM):
                    self.set(s, x, y, fun(s, x, y))
        self.update()


