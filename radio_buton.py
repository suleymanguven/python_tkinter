from tkinter import  *
pencere=Tk()
pencere.geometry("400x400")
def ekranaYaz():
    global labelSinif
    labelSinif.destroy()
    s=secenek.get()
    if s==1:
        labelSinif=Label(text="")
        labelSinif.place(relx=0.3, rely=0.7)
    elif s==2:
        labelSinif = Label(text="9. Sınıf")
        labelSinif.place(relx=0.3, rely=0.7)
    elif s==3:
        labelSinif = Label(text="10. Sınıf")
        labelSinif.place(relx=0.3, rely=0.7)
    elif s==4:
        labelSinif = Label(text="11. Sınıf")
        labelSinif.place(relx=0.3, rely=0.7)
    elif s==5:
        labelSinif = Label(text="12. Sınıf")
        labelSinif.place(relx=0.3, rely=0.7)

def ekranaYaz1():
    global labelSube
    labelSube.destroy()
    s = secenek1.get()
    if s == 1:
        labelSube = Label(text="")
        labelSube.place(relx=0.5, rely=0.7)
    elif s == 2:
        labelSube = Label(text="A Şubesi")
        labelSube.place(relx=0.5, rely=0.7)
    elif s == 3:
        labelSube = Label(text="B Şubesi")
        labelSube.place(relx=0.5, rely=0.7)
    elif s == 4:
        labelSube = Label(text="C Şubesi")
        labelSube.place(relx=0.5, rely=0.7)
    elif s == 5:
        labelSube = Label(text="D Şubesi")
        labelSube.place(relx=0.5, rely=0.7)

secenek=IntVar()
secenek1=IntVar()
radioButon=Radiobutton(text="Sınıf Yazma",value=1,variable=secenek,command=ekranaYaz).pack()
radioButon1=Radiobutton(text="9. Sınıf",value=2,variable=secenek,command=ekranaYaz).pack()
radioButon2=Radiobutton(text="10. Sınıf",value=3,variable=secenek,command=ekranaYaz).pack()
radioButon3=Radiobutton(text="11. Sınıf",value=4,variable=secenek,command=ekranaYaz).pack()
radioButon4=Radiobutton(text="12. Sınıf",value=5,variable=secenek,command=ekranaYaz).pack()
radioButon5=Radiobutton(text="Şube Yazma",value=1,variable=secenek1,command=ekranaYaz1).pack()
radioButon5=Radiobutton(text="A Şubesi",value=2,variable=secenek1,command=ekranaYaz1).pack()
radioButon6=Radiobutton(text="B Şubesi",value=3,variable=secenek1,command=ekranaYaz1).pack()
radioButon7=Radiobutton(text="C Şubesi",value=4,variable=secenek1,command=ekranaYaz1).pack()
radioButon8=Radiobutton(text="D Şubesi",value=5,variable=secenek1,command=ekranaYaz1).pack()
labelSinif=Label(text="")
labelSinif.place(relx=0.3,rely=0.7)
labelSube=Label(text="")
labelSube.place(relx=0.5,rely=0.7)

mainloop()