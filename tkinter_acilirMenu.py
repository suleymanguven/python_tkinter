from tkinter import *
def kapat():
    anaPencere.destroy()
def anaPencereGit():
    global yeniPencere
    yeniPencere.destroy()
    main()

def degistir():
    global yeniPencere
    anaPencere.destroy()
    yeniPencere=Tk()
    yeniPencere.geometry("200x200")
    yeniPencere.title("Yeni Pencere")
    buton=Button(text="Ana Pencere",command=anaPencereGit).pack()
    mainloop()

def main():
    global anaPencere
    anaPencere=Tk()
    anaPencere.title("Ana Pencere")
    anaPencere.geometry("300x300")
    menuKullanici=Menu(anaPencere)
    anaPencere.config(menu=menuKullanici)
    menuDosya=Menu(menuKullanici,tearoff=0)
    menuKullanici.add_cascade(label="Dosya",menu=menuDosya)
    menuDosya.add_command(label="Dosya Ekle")
    menuDosya.add_command(label="Dosya Sil")
    menuDosya.add_command(label="Pencere Değiştir",command=degistir)
    menuDosya.add_command(label="Çıkış",command=kapat)
    mainloop()

main()