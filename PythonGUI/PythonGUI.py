import turtle
from tkinter import *
from turtle import ScrolledCanvas, RawTurtle, TurtleScreen
import os
os.system(r"C:\Users\ufukb\Desktop\24v2\PythonGUI\FlexBison.exe")
def Oku():
    dosya = open("Outputs.txt", "r")
    liste = []
    for i in dosya:
        # com = dosya.readline()
        print(i)
        i = i.replace("\n", "")
        liste.append(i[0:])

    print(liste)
    COMMANDS = []
    for command in liste:
        if command[0] == 'F' or command[0] == 'R' or command[0] == 'C' or command[0] == 'P' or command[0]=='*' or command[0]=='B':
            COMMANDS.append(command)
        else:
            # Satırın L ile başladığı durumlar
            TEMP_COMMANDS = []
            loop_count = command[1:]  # Satırdan ilk harfi çıkartıp sayıyı bulmak için
            loop_count = int(loop_count)  # Stringi int değere çevirmek için
            for _ in range(loop_count):
                for elem in COMMANDS:
                    TEMP_COMMANDS.append(elem)
            COMMANDS = TEMP_COMMANDS

    return COMMANDS




def RunGUI():
    master = Tk()  # arayüz oluşturduk
    master.title("Automata Project")
    master.geometry("1920x1080")
    canvas = Canvas(master,height=700, width=700)  # arayüz boyutlandırması
    canvas.place(relx=0.04, rely=0.06, relwidth=0.91, relheight=0.6) # arayüzü çalıştırma
    screen= TurtleScreen(canvas)

    def MyTurtleFunc():
        dizi = Oku()

        t = turtle.RawTurtle(screen)

        t.speed(20)

        for i in dizi:

            if i[0] == "F":
                t.forward(int(i[1:]))
            if i[0] == "B":
                t.backward(int(i[1:]))
            if i[0] == "R":
                t.right(int(i[1:]))

            if i[0] == "C":

                if i[1] == "M":
                    t.color("blue")
                if i[1] == "K":
                    t.color("red")
                if i[1] == "Y":
                    t.color("green")

            if i[0] == "P":

                if i[1] == "1":
                    t.width(1)
                if i[1] == "2":
                    t.width(3)
                if i[1] == "3":
                    t.width(3)
            
    def DosyaYukle():
        return


    def RunTurt():
        MyTurtleFunc()

  #  frameÜst = Frame(master, bg='light green')
   # frameÜst.place(relx=0.04, rely=0.04, relwidth=0.91, relheight=0.6)  # frame i şekillendirdik ve çalıştırdık

    frameOrta = Frame(master, bg='light blue')
    frameOrta.place(relx=0.04, rely=0.66, relwidth=0.91, relheight=0.06)

    frameAlt = Frame(master, bg='orange')
    frameAlt.place(relx=0.04, rely=0.74, relwidth=0.91, relheight=0.25)

    #etiketÜst = Label(frameÜst, bg='light green', text="Çizen Robot", font="calibri 15 bold", foreground="black")
    #etiketÜst.pack(padx=5, pady=5)

    # etiketOrta = Label(frameOrta,bg = 'light blue',text = "Dosya aç:",font = "calibri 20 bold",foreground="black")
    # etiketOrta.pack(padx=5,pady=10,side=LEFT)

    # etiketOrta2=Label(frameOrta,bg = 'light blue',text = "Run:",font = "calibri 20 bold",foreground="black")
    # etiketOrta2.pack(padx=5,pady=10)

    etiketAlt = Label(frameAlt, bg='orange', text="Debug Area ", font="vendara 15 bold ", foreground="black")
    etiketAlt.pack(padx=0.1, pady=0.1)

    #AltFrameMetin = Text(frameAlt, height=10.5, width=180)
    #AltFrameMetin.tag_configure('style', foreground='white', font=('calibri', 10, 'bold'))
    l = Label(frameAlt, text= "", font= "times 30 ", bg="orange")
    l.pack()
    #AltFrameMetin.pack()

    def HatamesajıOku():

        hatadosya = open("Errors.txt", "r")
        str1 = ""

        for i in hatadosya:
            str1 = str1 + i
            return str1

    l = Label(frameAlt, text=HatamesajıOku(), font="times 30 ", bg="orange")
    l.pack()
    #KarsılamaMetni = HatamesajıOku()
    #AltFrameMetin.insert(END, KarsılamaMetni, 'style')

    dosyaAcButton = Button(frameOrta, text="DOSYA YÜKLE", bg="white", foreground="black", command=DosyaYukle)
    dosyaAcButton.pack(padx=0.2, pady=0.2, side=LEFT)

    ProgramCalıstır = Button(frameOrta, text="PROGRAMI ÇALIŞTIR", foreground="black", command=RunTurt)
    ProgramCalıstır.pack(padx=0.2, pady=0.2, side=LEFT)

    master.mainloop()


# MyTurtleFunc()

RunGUI()
a = input("..")
