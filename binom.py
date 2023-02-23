from __future__ import division
import tkinter as tk
from tkinter import IntVar,DoubleVar
from tkinter import messagebox
from tkinter import *
def combin(n, k):
    """Nombre de combinaisons de n objets pris k a k"""
    if k > n//2:
        k = n-k
    x = 1
    y = 1
    i = n-k+1
    while i <= n:
        x = (x*i)//y
        y += 1
        i += 1
    return x
def binom(k,n,p):
    """binom(k,n,p): probabilité d'avoir k réussite(s) dans n évènements indépendants, chaque évènement ayant une probabilité p% de réussite"""
    x=combin(n,k)*pow(p,k)*pow(1-p,n-k)
    return x
def eseprence(n,p):
    return n*p
def variance(n,p):
    return n*p*(1-p)
def helloCallBack():
    k=int(entryk.get())
    n=int(entryn.get())
    p=float(entryp.get())
    entryprob.insert(0,binom(k,n,p))
    entryesp.insert(0,eseprence(n,p))
    entryvar.insert(0,variance(n,p))
def developer():
    messagebox.showinfo("The Developer", "Wissem Hammami\nFor Contact:\nFacebook: Wissem Hammami\nInstagram: wissem_hammami21\nEmail: Hammamiwissem21@gmx.us")
window = tk.Tk()
greeting = tk.Label(text="Calculatrice loi binomiale")
greeting.pack()
window.geometry('300x300')
p1=IntVar()
n1=IntVar()
f=DoubleVar()
label = tk.Label(text="k=")
entryk = tk.Entry(textvariable=p1)
label.pack()
entryk.pack()
label = tk.Label(text="n=")
entryn = tk.Entry(textvariable=n1)
label.pack()
entryn.pack()
label = tk.Label(text="p=")
entryp = tk.Entry(textvariable=f)
label.pack()
entryp.pack()
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
window.title("Calcule Binomiale")
window.resizable(False, False)
window.mainloop()
