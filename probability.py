from __future__ import division
import tkinter as tk
from tkinter import IntVar,DoubleVar
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageFont, ImageDraw, ImageTk
import math
import webbrowser
from tkinter.ttk import *
image = PhotoImage(file = "back.jpg")
img = ImageTk.PhotoImage(image) 
def callback(url):
    webbrowser.open_new(url)
def expo(x,la):
    if(x>=0):
        x=la*math.exp(-la*x)
        return x
    else:
        return 0
def eseprenceex(la):
    return 1/la
def varianceex(la):
    return 1/(la*la)
def fact(n):
    if n == 1:
         return n
    elif n==0:
        return 1
    elif n < 1:
        return 0
    else:
        return n*fact(n-1)
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
def poisson(k,la):
    x=(pow(la,k)*math.exp(-la))/fact(k)
    return x
def eseprencep(la):
    return la
def variancep(la):
    return la
def binom(k,n,p):
    """binom(k,n,p): probabilité d'avoir k réussite(s) dans n évènements indépendants, chaque évènement ayant une probabilité p% de réussite"""
    x=combin(n,k)*pow(p,k)*pow(1-p,n-k)
    return x
def eseprenceb(n,p):
    return n*p
def varianceb(n,p):
    return n*p*(1-p)
def helloCallBackex():
    entryk,entryn=create_expo()
    k=int(entryk.get())
    n=float(entryn.get())
    label = tk.Label(text="Probabilité X=")
    entryprob = tk.Entry()
    label.place(x=320,y=240)
    entryprob.place(x=310,y=260)
    label = tk.Label(text="Espérence E(X)=")
    entryesp = tk.Entry()
    label.place(x=320,y=280)
    entryesp.place(x=310,y=300)
    label = tk.Label(text="Variance V(X)=")
    entryvar = tk.Entry()
    label.place(x=320,y=320)
    entryvar.place(x=310,y=340)
    entryprob.insert(0,expo(k,n))
    entryesp.insert(0,eseprenceex(n))
    entryvar.insert(0,varianceex(n))
def helloCallBackp():
    entryk,entryn=create_poiss()
    k=int(entryk.get())
    n=float(entryn.get())
    label = tk.Label(text="Probabilité X=")
    entryprob = tk.Entry()
    label.place(x=320,y=240)
    entryprob.place(x=310,y=260)
    label = tk.Label(text="Espérence E(X)=")
    entryesp = tk.Entry()
    label.place(x=320,y=280)
    entryesp.place(x=310,y=300)
    label = tk.Label(text="Variance V(X)=")
    entryvar = tk.Entry()
    label.place(x=320,y=320)
    entryvar.place(x=310,y=340)
    entryprob.insert(0,poisson(k,n))
    entryesp.insert(0,eseprencep(n))
    entryvar.insert(0,variancep(n))
def helloCallBackb():
    entryk,entryn,entryp=create_binom()
    k=int(entryk.get())
    n=int(entryn.get())
    p=float(entryp.get())
    label = tk.Label(text="Probabilité X=")
    entryprob = tk.Entry()
    label.place(x=320,y=240)
    entryprob.place(x=310,y=260)
    label = tk.Label(text="Espérence E(X)=")
    entryesp = tk.Entry()
    label.place(x=320,y=280)
    entryesp.place(x=310,y=300)
    label = tk.Label(text="Variance V(X)=")
    entryvar = tk.Entry()
    label.place(x=320,y=320)
    entryvar.place(x=310,y=340)
    entryprob.insert(0,binom(k,n,p))
    entryesp.insert(0,eseprenceb(n,p))
    entryvar.insert(0,varianceb(n,p))
def settozero():
    entryk.delete(0,END)
    entryn.delete(0,END)
    entryp.delete(0,END)
    entryprob.delete(0,END)
    entryesp.delete(0,END)
    entryvar.delete(0,END)
def developer():
    messagebox.showinfo("Information", "Wissem Hammami\nFor Contact:\nFacebook: Wissem Hammami\nInstagram: wissem_hammami21\nEmail: Hammamiwissem21@gmx.us")
def create_binom():
    label = tk.Label(text="   Loi Binomiale       " ,bg="black" ,fg="white")
    label.place(x=330,y=60)
    label = tk.Label(text="k=")
    entryk = tk.Entry(textvariable=p1)
    label.place(x=290,y=100)
    entryk.place(x=310,y=100)
    label = tk.Label(text="n=")
    label.place(x=290,y=120)
    entryn = tk.Entry(textvariable=n1)
    entryn.place(x=310,y=120)
    label = tk.Label(text="p=")
    label.place(x=290,y=140)
    entryp = tk.Entry(textvariable=f)
    entryp.place(x=310,y=140)
    button = tk.Button(
        text="Calculer",
        width=7,
        height=1,
        bg="white",
        fg="black",
        command=helloCallBackb
    )
    button.place(x=350,y=180)
    # label = tk.Label(text="Probabilité X=")
    # entryprob = tk.Entry()
    # label.place(x=320,y=220)
    # entryprob.place(x=310,y=240)
    # label = tk.Label(text="Espérence E(X)=")
    # entryesp = tk.Entry()
    # label.place(x=320,y=260)
    # entryesp.place(x=310,y=280)
    # label = tk.Label(text="Variance V(X)=")
    # entryvar = tk.Entry()
    # label.place(x=320,y=300)
    # entryvar.place(x=310,y=320)
    return entryk,entryn,entryp
def create_poiss():
    label = tk.Label(text="   Loi de Poisson     " ,bg="black" ,fg="white")
    label.place(x=330,y=60)
    label = tk.Label(text="k=")
    entryk = tk.Entry(textvariable=p1)
    label.place(x=290,y=100)
    entryk.place(x=310,y=100)
    label = tk.Label(text="λ=")
    label.place(x=290,y=120)
    entryn = tk.Entry(textvariable=n1)
    entryn.place(x=310,y=120)
    label = tk.Label(text="                                               ")
    label.place(x=290,y=140)
    labe = tk.Label(text="                                                 ")
    labe.place(x=310,y=140)
    button = tk.Button(
        text="Calculer",
        width=7,
        height=1,
        bg="white",
        fg="black",
        command=helloCallBackp
    )
    button.place(x=350,y=180)
    # label = tk.Label(text="Probabilité X=")
    # entryprob = tk.Entry()
    # label.place(x=320,y=220)
    # entryprob.place(x=310,y=240)
    # label = tk.Label(text="Espérence E(X)=")
    # entryesp = tk.Entry()
    # label.place(x=320,y=260)
    # entryesp.place(x=310,y=280)
    # label = tk.Label(text="Variance V(X)=")
    # entryvar = tk.Entry()
    # label.place(x=320,y=300)
    # entryvar.place(x=310,y=320)
    return entryk,entryn
def create_expo():
    label = tk.Label(text="   Loi Exponentielle" ,bg="black" ,fg="white")
    label.place(x=330,y=60)
    label = tk.Label(text="k=")
    entryk = tk.Entry(textvariable=p1)
    label.place(x=290,y=100)
    entryk.place(x=310,y=100)
    label = tk.Label(text="λ=")
    label.place(x=290,y=120)
    entryn = tk.Entry(textvariable=n1)
    entryn.place(x=310,y=120)
    label = tk.Label(text="                                               ")
    label.place(x=290,y=140)
    labe = tk.Label(text="                                                 ")
    labe.place(x=310,y=140)
    button = tk.Button(
        text="Calculer",
        width=7,
        height=1,
        bg="white",
        fg="black",
        command=helloCallBackex
    )
    button.place(x=350,y=180)
    # label = tk.Label(text="Probabilité X=")
    # entryprob = tk.Entry()
    # label.place(x=320,y=220)
    # entryprob.place(x=310,y=240)
    # label = tk.Label(text="Espérence E(X)=")
    # entryesp = tk.Entry()
    # label.place(x=320,y=260)
    # entryesp.place(x=310,y=280)
    # label = tk.Label(text="Variance V(X)=")
    # entryvar = tk.Entry()
    # label.place(x=320,y=300)
    # entryvar.place(x=310,y=320)
    return entryk,entryn
window = tk.Tk()
greeting = tk.Label(text="Calculatrice de Probabilité")
greeting.place(x=300,y=0)
label = tk.Label(text="Choisir Une Loi: ")
label.place(x=50,y=30)
button = tk.Button(
    text="Loi Binomiale",
    width=20,
    height=1,
    bg="white",
    fg="black",
    command=create_binom
)
button.place(x=150,y=30)
button = tk.Button(
    text="Loi Exponentielle",
    width=20,
    height=1,
    bg="white",
    fg="black",
    command=create_expo
)
button.place(x=320,y=30)
button = tk.Button(
    text="Loi de Poisson",
    width=20,
    height=1,
    bg="white",
    fg="black",
    command=create_poiss
)
button.place(x=490,y=30)
window.geometry('800x600')
p1=IntVar()
n1=IntVar()
f=DoubleVar()
menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="à propos", menu=filemenu)
filemenu.add_command(label="Développeur",command=developer)
filemenu.add_command(label="Quitter",command=window.destroy)
filemenu.add_separator()
window.config(menu=menubar)
window.title("Calcule De Probabilité")
window.resizable(False, False)
label=tk.Label(text="Developped By ")
label.place(x=575,y=570)
wissem=tk.Label(text="Wissem Hammami",fg="blue",cursor="hand2")
wissem.place(x=660,y=570)
wissem.bind("<Button-1>",lambda e: callback("https://www.facebook.com/Mr.pan009"))
window.mainloop()
