# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 18:00:23 2021

@author: IVAN
"""

import turtle

miTortuga = turtle.Turtle()
miVentana = turtle.Screen()

miTortuga.goto(10,10)
miTortuga.forward(200)
miTortuga.right(90)
miTortuga.penup()
miTortuga.forward(200)

miTortuga.shape("turtle")


miVentana.exitonclick()

# def dibujarEspiral(miTortuga, longitudLinea):
#     if longitudLinea > 0:
#         miTortuga.forward(longitudLinea)
#         miTortuga.right(90)
#         dibujarEspiral(miTortuga,longitudLinea-5)

# dibujarEspiral(miTortuga,100)
# miVentana.exitonclick()
