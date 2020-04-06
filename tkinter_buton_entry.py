from tkinter import *
import tkinter.messagebox as msg
pencere=Tk()
def kaydetGoster():

    adEntryVeri=adEntry.get()
    if adEntryVeri!="":
        msg._show("Kayıt",adEntryVeri+" Yazıldı")
        adEntry.delete(0,END)
    else:
        msg._show("Kayıt Olmadı","Hiç bir veri girilmedi")
def iptalGoster():
    adEntryVeri = adEntry.get()
    if adEntryVeri!="":
        msg._show("İptal","İptal Butonuna Basıldı")
        adEntry.delete(0,END)
    else:
        msg._show("İptal", "İptal Butonuna Basıldı")
pencere.geometry("300x300")
baslik=pencere.title("Buton&Entry")
adLabel=Label(text="Adınız: ")
adLabel.place(relx=0.05,rely=0.05)
adEntry=Entry()
adEntry.place(relx=0.3,rely=0.05)
soyadEntry=Entry()
soyadEntry.place(relx=0.3,rely=0.12)
adEntry.focus()
soyadEntry.insert(0,"Deneme")
butonKayit=Button(text="Kayıt",width=8,command=kaydetGoster).place(relx=0.2,rely=0.25)
butonIptal=Button(text="İptal",width=8,command=iptalGoster).place(relx=0.5,rely=0.25)

mainloop()