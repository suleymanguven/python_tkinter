from tkinter import *
anaPencere=Tk()
baslik=anaPencere.title("Python Tkinter")
anaPencere.geometry("500x300")
anaPencere.resizable(width=FALSE,height=FALSE)
etiket=Label(text="Python Programlama Dersi",font="Times 24 italic").pack()
buton=Button(text="Giriş",width=20,height=2).pack()
giris=Entry().pack()
listBox=Listbox(height=5).pack()
checkButon1=Checkbutton(text="Seçenek-1").pack()
checkButon2=Checkbutton(text="Seçenek-2").pack()
radioButon=Radiobutton(text="Onay-1").pack()

mainloop()