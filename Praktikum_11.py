### KEGIATAN 1
##
##from Tkinter import *
##
##my_app = Tk(className='Aplikasi dengan beberapa widget')
##L0 = Label(my_app, text = "Data diri", font=('Arial', 24))
##L0.grid(row=0, column=0)
##L1 = Label(my_app, text="Nama")
##L1.grid(row=1, column=0, sticky=W)
##E1 = Label(my_app, text="Anita Lusi Romadhon")
##E1.grid(row=1, column=1, sticky=W)
##L2 = Label(my_app, text="NIM")
##L2.grid(row=2, column=0, sticky=W)
##E2 = Label(my_app, text="L200180153")
##E2.grid(row=2, column=1, sticky=W)
##L3 = Label(my_app, text="Buku favorit")
##L3.grid(row=3, column=0, sticky=W)
##E3 = Label(my_app, text="Merayakan kehilangan-Brian Khrisna")
##E3.grid(row=3, column=1, sticky=W)
##L4 = Label(my_app, text="Idola di kalangan sahabat")
##L4.grid(row=4, column=0, sticky=W)
##E4 = Label(my_app, text="Umar bin Khattab")
##E4.grid(row=4, column=1, sticky=W)
##L5 = Label(my_app, text="Motto")
##L5.grid(row=5, column=0, sticky=W)
##E5 = Label(my_app, text ="Jangan sepelekan hal kecil")
##E5.grid(row=5, column=1, sticky=W)
##
##def tutup():
##    my_app.quit()
##
##B = Button(my_app,text="Tutup" ,command=tutup)
##B.grid(row=6, column=1)
##my_app.mainloop()
           

#KEGIATAN 2

##from Tkinter import *
##calc = Tk(className='Kalkulator sederhana')
##
##L1 = Label(calc, text='Angka 1', font="Times 14")
##L1.place(x=20, y=20)
##E1 = Entry(calc, justify=RIGHT, font="Times 14")
##E1.place(x=90, y=10, height=35, width=180)
##
##L2 = Label(calc, text='Angka 2', font="Times 14")
##L2.place(x=20, y=60)
##E2 = Entry(calc, justify=RIGHT, font="Times 14")
##E2.place(x=90, y=60, height=35, width=180)
##
##def tambah() :
##    "menjumlahkan dua bilangan"
##    bil1 = int(E1.get())
##    bil2 = int(E2.get())
##    hasil = bil1 + bil2
##    L4.config(text=hasil)
##def kurang() :
##    "mengurangi dua bilangan"
##    bil1 = int(E1.get())
##    bil2 = int(E2.get())
##    hasil= bil1 - bil2
##    L4.config(text=hasil)
##def kali() :
##    "perkalian dua bilangan"
##    bil1 = int(E1.get())
##    bil2 = int(E2.get())
##    hasil = bil1 * bil2
##    L4.config(text=hasil)
##def bagi() :
##    "pembagian dua bilangan"
##    bil1 = int(E1.get())
##    bil2 = int(E2.get())
##    hasil = bil1 / bil2
##    L4.config(text=hasil)
##
##B1 = Button(calc, text="+", command=tambah, font="Times 14")
##B1.place(x=60, y=110, height=30, width=30)
##
##B2 = Button(calc, text="-", command=kurang, font="Times 14")
##B2.place(x=120, y=110, height=30, width=30)
##
##B3 = Button(calc, text="x", command=kali, font="Times 14")
##B3.place(x=180, y=110, height=30, width=30)
##
##B4 = Button(calc, text=":", command=bagi, font="Times 14")
##B4.place(x=240, y=110, height=30, width=30)
##    
##L3 = Label(calc, text='Hasil', font="Times 14")
##L3.place(x=20, y=170)
##
##L4 = Label(calc, font="Times 14", justify=RIGHT, relief=RIDGE)
##L4.place(x=90, y=165, height=35, width=180)
##
##calc.mainloop()


# KEGIATAN 3

from Tkinter import *
bageo = Tk(className="Luas Bangun Geometri")

title = Label(bageo, text="Bangun Geometri", font="Times, 24")
title.grid(row=0)

desk = Label(bageo, font="Times, 12", justify=LEFT, text="""Geometri adalah ilmu yang membahas tentang hubungan antar titik,
garis, sudut, bidang, dan bangun-bangun ruang. Ada  2 macam bangun geometri, yaitu bangun geometri datar dan bangun geometri ruang.
Contoh bangun geometri ruang yaitu bola.Bola memiliki beberapa sifat yaitu : tidak memiliki rusuk dan titik sudut dan
Setiap titik pada bidang lengkung memiliki jarak yang sama dengan titik pusat.""")
desk.grid(row=1)

L1 = Label(bageo, font="Times, 12", text="Jari-jari")
L1.place(x=85, y=170)

E = Entry(bageo, font="Times, 12")
E.place(x=175, y=170, height=30)

def hitung():
    r = int(E.get())
    hasil= 4*3.14*r**2
    luas.config(text=hasil)

B = Button(bageo, text="Hitung Luas", command=hitung, font="Times, 14")
B.place(x=85, y=210)

L2 = Label(bageo, text="Luas", font="Times, 14 bold")
L2.place(x=200, y=215)

luas = Label(bageo, font="Times 14 bold")
luas.place(x=265, y=215)

bageo.mainloop()
