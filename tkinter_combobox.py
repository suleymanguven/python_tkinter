from tkinter import *
from tkinter.ttk import Combobox
""""
def ekranaYaz():
    global label
    label.destroy()
    x=combo.get()
    label=Label(text=x)
    label.pack()
pencere=Tk()
pencere.geometry("400x400")
secenek=["Pazartesi","Salı","Çarşamba","Perşembe","Cuma","Cumartesi","Pazar"]
combo=Combobox(pencere,values=secenek)
combo.pack()
buton=Button(text="Ekrana Yaz",command=ekranaYaz).pack()
label=Label(text="")
label.pack()
mainloop()
"""

yeniPencere=Tk()
yeniPencere.geometry("200x200")
def hesapla():
    global labelYeni
    labelYeni.destroy()
    yil=int(comboYeni.get())
    yas=2020-yil
    labelYeni=Label(text=yas)
    labelYeni.pack()
secenekYeni=list(range(1970,2001))
comboYeni=Combobox(yeniPencere,values=secenekYeni)
comboYeni.pack()
butonYeni=Button(text="Hesapla",command=hesapla).pack()
labelYeni=Label(text="")
labelYeni.pack()
mainloop()