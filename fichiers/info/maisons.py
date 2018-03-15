from turtle import *

def va(x,y):
    up()
    goto(x,y)
    down()

def carre(x,y,l):
    va(x,y)
    for i in range(4):
        forward(l)
        left(90)

def triangle(x,y,l):
    va(x,y)
    for i in range(3):
        forward(l)
        left(120)
    
def maison(x,y,l,couleur):
    color(couleur)
    carre(x,y,l)
    triangle(x,y+l,l)
    carre(x+2/5*l,y,l/5)
    carre(x+1/5*l,y+3/5*l,l/5)
    carre(x+3/5*l,y+3/5*l,l/5)
    
def rue(x,y,l,n):
    for i in range(n):
        maison(x+i*l,y,l,i)


speed(0)
rue(-300,0,100,7)
rue(-300,-200,130,7)
done()