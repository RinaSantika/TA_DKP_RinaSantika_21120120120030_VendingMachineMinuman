from tkinter import *

#Pembuatan Jendela GUI
root = Tk()
root.title("Program Vending Machine Minuman")
root.resizable(0,0)

#Layout Global
MainF = Frame(root, relief=RAISED, bg="Red", bd=20)
MainF.grid(row=0, column=0, rowspan=2, columnspan=2)

IncomeF = Frame(MainF, relief=RAISED, bg="white", bd=10)
IncomeF.grid(row=1, column=1, rowspan=2, columnspan=2)

ReturnF = Frame(MainF, relief=SUNKEN, bg="red", bd=5)
ReturnF.grid(row=2, column=1, rowspan=2, columnspan=2)

SelectF = Frame(MainF, relief=RAISED, bg="red", bd=10)
SelectF.grid(row=2, column=0, rowspan=2)
                 
TitleLbl=Label(MainF, text="\tVENDING MACHINE", bg="red", font=("arial bold", 20))
TitleLbl.grid(row=0, column=0, columnspan=2)

#Function
def ShowPaid():
    quote = "Di Bayar : Rp " + str(BayarEntry.get()) + "\n"
    change = int(BayarEntry.get()) - Harga.get()
    if int(BayarEntry.get()) > Harga.get():
        quote = quote + "Uang Kembalian : Rp " + str(change) + "\n"
    else:
        quote = "Jumlah Tidak Valid!"
    moneys = [50000, 20000, 10000, 5000, 2000, 1000, 500]
    x = 0
    while change > 0:
        while change >= moneys[x]:
            change = change - moneys[x]
            quote = quote + "Rp "+ str(moneys[x]) + " dibagikan\n" 
        x = x + 1
    T.insert(END, quote+"\n")

def quit():
    root.destroy()

#Frame Main
Harga = IntVar()
Harga.set(1)
drinks = [["Aqua Rp 5.000",5000],
          ["Teh Pucuk Rp 9.000", 9000],
          ["Pocari Sweat Rp 15.000",15000],
          ["Coca Cola Rp 8.000",8000],
          ["Fanta Rp 6.500",6500],
          ["Sprite Rp 6.000",6000],
          ["Fruit Tea Rp 11.000",11000],
          ["Floridina Rp 12.000",12000],
          ["Larutan Penyegar Rp 5.500",5500],
          ["Golda Coffe Rp 10.000",10000],
          ["Teh Javana Rp 9.500",9500],
          ["Ichi Ocha Rp 7.000",7000],
          ["Ultra Milk Rp 4.500",4500],
              ["EXIT",0]]

Memilih = Label(MainF, text="Pilih Minuman Favorit Anda", bg="red", font=("arial bold", 10)) 
Memilih.grid(row=1, column=0)

#Frame Select
for i in range (0,len(drinks)-1):
  Pilihan = Radiobutton(SelectF,
                       text=drinks[i][0],
                       bg="sky blue",
                       font=("pixel", 10),
                       indicatoron = 0,
                       width = 20,
                       padx = 20,
                       variable=Harga,
                       value=drinks[i][1])
  Pilihan.pack(side=TOP)

Pilihan = Radiobutton(SelectF,
                       text=drinks[i+1][0],
                       indicatoron = 0,
                       bg="lime",
                       width = 5,
                       padx = 20,
                       variable=Harga,
                       command=quit,
                       value=drinks[i+1][1])
Pilihan.pack(side=TOP)

#Frame Income
PembayaranLbl= Label(IncomeF, text="Masukkan Uang",bg="white")
PembayaranLbl.grid(row=0, column=0, columnspan=2)
BayarEntry = Entry(IncomeF, bd=7)
BayarEntry.grid(row=1, column=0)
PayBtn = Button(IncomeF, text='Pay', bd=5, command=ShowPaid)
PayBtn.grid(row=1, column=1)

#Frame Return
S = Scrollbar(ReturnF)
S.pack(side=RIGHT, fill=Y)
T = Text(ReturnF, height=7, width=28, bg="black", fg="red", bd=10)
T.pack(side=LEFT, fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
T.insert(END, "Perubahan\n")

root.mainloop()


