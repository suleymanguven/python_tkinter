from tkinter import *
pencere=Tk()

def listeyeEkle():
    if secim1.get()==1:
        listBox.insert(END,"Seçenek-1")
        secim1.set(0)
def listeyeEkle1():
    if secim2.get() == 1:
        listBox.insert(END, "Seçenek-2")
        secim2.set(0)
def secileniSil():
    listBox.delete(ACTIVE)
def hepsiniSil():
    listBox.delete(0,END)
baslik=pencere.title("CheckBox&ListBox")
pencere.geometry("350x350")
secim1=IntVar()
secim1.set(0)
secim2=IntVar()
secim2.set(0)
onay1=Checkbutton(text="Seçenek-1",variable=secim1)
onay1.place(relx=0,rely=0.1)
onay2=Checkbutton(text="Seçenek-2",variable=secim2)
onay2.place(relx=0,rely=0.2)

buton1=Button(text="Ekle",command=listeyeEkle).place(relx=0.3,rely=0.1)
buton2=Button(text="Ekle",command=listeyeEkle1).place(relx=0.3,rely=0.2)

listBox=Listbox()
listBox.place(relx=0,rely=0.3)

buton3=Button(text="Seçileni Sil",command=secileniSil).place(relx=0.5,rely=0.3)
buton4=Button(text="Hepsini Sil",command=hepsiniSil).place(relx=0.5,rely=0.4)

mainloop()