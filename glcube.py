import pygame, config
# -*- coding: utf-8 -*-
from sys import exit
from OpenGL.GL import *
from OpenGL.GLU import *
from math import sin, cos

screen = (config.Display.width, config.Display.height)
pygame.init()
surface = pygame.display.set_mode(screen, pygame.OPENGL|pygame.DOUBLEBUF, 24)
pygame.display.set_caption("Rubiks Cube")

def get_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

def reshape((width, height)):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1.0*width/height, 0.1, 1000.0)
    glMatrixMode(GL_MODELVIEW)

def init():
    glEnable(GL_DEPTH_TEST)
    (r, g, b) = config.Display.bgcolor
    glClearColor(r, g, b, 1.0)
    reshape(screen)

def draw(w, c):
    sides = [[[ c.bb_sides[s][x][y] for x in xrange(0, 3)]
              for y in xrange(0, 3)]
             for s in xrange(0, 6)]
    
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(0, 0, 6, 0, 0, -10, 0, 1, 0)
    (mx, my) = pygame.mouse.get_pos()
    glRotatef((mx / (config.Display.width*1.0)) * 360, 0, 1, 0)
    glRotatef(45, 0, 0, 1)
    glRotatef(45, 0, 1, 0)
    b = 0.001
    glBegin(GL_QUADS)
    glColor(0,0,0)

    glVertex3f(-1.5+b, -1.5+b, -1.5+b)
    glVertex3f(+1.5-b, -1.5+b, -1.5+b)
    glVertex3f(+1.5-b, +1.5-b, -1.5+b)
    glVertex3f(-1.5+b, +1.5-b, -1.5+b)
    
    glVertex3f(-1.5+b, -1.5+b, +1.5-b)
    glVertex3f(+1.5-b, -1.5+b, +1.5-b)
    glVertex3f(+1.5-b, +1.5-b, +1.5-b)
    glVertex3f(-1.5+b, +1.5-b, +1.5-b)

    glVertex3f(-1.5+b, -1.5+b, -1.5+b)
    glVertex3f(+1.5-b, -1.5+b, -1.5+b)
    glVertex3f(+1.5-b, -1.5+b,  +1.5-b)
    glVertex3f(-1.5+b, -1.5+b,  +1.5-b)

    glVertex3f(-1.5+b, +1.5-b, -1.5+b)
    glVertex3f(+1.5-b, +1.5-b, -1.5+b)
    glVertex3f(+1.5-b, +1.5-b,  +1.5-b)
    glVertex3f(-1.5+b, +1.5-b,  +1.5-b)
    
    glVertex3f( -1.5+b, -1.5+b, -1.5+b)
    glVertex3f( -1.5+b, +1.5-b, -1.5+b)
    glVertex3f( -1.5+b, +1.5-b, +1.5-b)
    glVertex3f( -1.5+b, -1.5+b, +1.5-b)

    glVertex3f( +1.5-b, -1.5+b, -1.5+b)
    glVertex3f( +1.5-b, +1.5-b, -1.5+b)
    glVertex3f( +1.5-b, +1.5-b, +1.5-b)
    glVertex3f( +1.5-b, -1.5+b, +1.5-b)


    b = 0.05

    for y in xrange(0, 3):
        for x in xrange(0, 3):
            glColor(*sides[0][2-y][x])
            glVertex3f(x-1.5+b, y-1.5+b, 1.5)
            glVertex3f(x-1.5+1-b, y-1.5+b, 1.5)
            glVertex3f(x-1.5+1-b, y-1.5+1-b, 1.5)
            glVertex3f(x-1.5+b, y-1.5+1-b, 1.5)            
            glColor(*sides[5][y][x])
            glVertex3f(x-1.5+b, y-1.5+b, -1.5)
            glVertex3f(x-1.5+1-b, y-1.5+b, -1.5)
            glVertex3f(x-1.5+1-b, y-1.5+1-b, -1.5)
            glVertex3f(x-1.5+b, y-1.5+1-b, -1.5)
            glColor(*sides[1][2-x][y])
            glVertex3f(-1.5, x-1.5+b, y-1.5+b)
            glVertex3f(-1.5, x-1.5+1-b, y-1.5+b)
            glVertex3f(-1.5, x-1.5+1-b, y-1.5+1-b)
            glVertex3f(-1.5, x-1.5+b, y-1.5+1-b)
            glColor(*sides[2][2-x][2-y])
            glVertex3f(1.5, x-1.5+b, y-1.5+b)
            glVertex3f(1.5, x-1.5+1-b, y-1.5+b)
            glVertex3f(1.5, x-1.5+1-b, y-1.5+1-b)
            glVertex3f(1.5, x-1.5+b, y-1.5+1-b)
            glColor(*sides[3][y][x])
            glVertex3f(x-1.5+b, 1.5, y-1.5+b)
            glVertex3f(x-1.5+1-b, 1.5, y-1.5+b)
            glVertex3f(x-1.5+1-b, 1.5, y-1.5+1-b)
            glVertex3f( x-1.5+b, 1.5, y-1.5+1-b)
            glColor(*sides[4][2-y][x])
            glVertex3f(x-1.5+b, -1.5, y-1.5+b)
            glVertex3f(x-1.5+1-b, -1.5, y-1.5+b)
            glVertex3f(x-1.5+1-b, -1.5, y-1.5+1-b)
            glVertex3f(x-1.5+b, -1.5, y-1.5+1-b)            

            

   
    glEnd()
    pygame.display.flip()

def loop(c):
    init()
    maxfps = 100
    clock = pygame.time.Clock()
    w = 0
    while True:
        w = w + 0.3
        clock.tick(maxfps)
        draw(w, c)
        get_event()        
