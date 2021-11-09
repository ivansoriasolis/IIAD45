# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 18:01:35 2021

@author: IVAN
"""

import turtle

def arbol(longitudRama,t):
    if longitudRama > 5:
        t.forward(longitudRama)
        t.right(20)
        arbol(longitudRama-15,t)
        t.left(40)
        arbol(longitudRama-15,t)
        t.right(20)
        t.backward(longitudRama)

def main():
    t = turtle.Turtle()
    miVentana = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    arbol(75,t)
    miVentana.exitonclick()

main()