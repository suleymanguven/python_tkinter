from tkinter import *
import tkinter.messagebox as msg


GUNLER=["Pazartesi","Salı","Çarşamba","Perşembe","Cuma","Cumartesi","Pazar"]
def tamam():
    secilenGun=secenek.get()
    msg._show("Günler",secilenGun+" seçildi")
pencere=Tk()
pencere.geometry("250x250")
secenek=StringVar()
secenek.set(GUNLER[0])
opMenu=OptionMenu(pencere,secenek,*GUNLER)
opMenu.pack()
buton=Button(text="Tamam",command=tamam).pack()


mainloop()