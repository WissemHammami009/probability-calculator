#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division
import tkinter as tk
from tkinter import IntVar,DoubleVar
from tkinter import messagebox
from tkinter import *
import math
from fractions import Fraction as frac
def fact(n):
    if n == 1:
         return n
    elif n < 1:
        return 0
    else:
        return n*fact(n-1)
def poisson(k,la):
    x=(pow(la,k)*math.exp(-la))/fact(k)
    return x
def eseprence(la):
    return la
def variance(la):
    return la
def helloCallBack():
    k=int(entryk.get())
    la=float(entryn.get())
    entryprob.insert(0,poisson(k,la))
    entryesp.insert(0,eseprence(la))
    entryvar.insert(0,variance(la))
def developer():
    messagebox.showinfo("The Developer", "Wissem Hammami\nFor Contact:\nFacebook: Wissem Hammami\nInstagram: wissem_hammami21\nEmail: Hammamiwissem21@gmx.us")
window = tk.Tk()
window.geometry("300x300")
greeting = tk.Label(text="calculatrice loi De Poisson")
greeting.pack()
p1=IntVar()
n1=IntVar()
f=DoubleVar()
label = tk.Label(text="k=")
entryk = tk.Entry(textvariable=p1)
label.pack()
entryk.pack()
label = tk.Label(text="λ=")
entryn = tk.Entry(textvariable=f)
label.pack()
entryn.pack()
button = tk.Button(
    text="Caclculer",
    width=7,
    height=1,
    bg="white",
    fg="black",
    command=helloCallBack
)
button.pack()
label = tk.Label(text="Probabilité X=")
entryprob = tk.Entry()
label.pack()
entryprob.pack()
label = tk.Label(text="Espérence E(X)=")
entryesp = tk.Entry()
label.pack()
entryesp.pack()
label = tk.Label(text="Variance V(X)=")
entryvar = tk.Entry()
label.pack()
entryvar.pack()
menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="à propos", menu=filemenu)
filemenu.add_command(label="Développeur",command=developer)
filemenu.add_command(label="Quitter",command=window.destroy)
filemenu.add_separator()
window.config(menu=menubar)
window.title("Loi De Poisson")
window.resizable(False, False)
window.mainloop()
