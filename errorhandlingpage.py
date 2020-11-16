from tkinter import *
from tkinter import messagebox
mywin2=Tk()
mywin2.title("Error Checks")
labelling=Label()

amountlbl= Label(mywin2, text="enter amount:\n")
amountlbl.pack(side=TOP)
amounten= Entry(mywin2)
amounten.pack(side=TOP)

def malaysia():
    amount = int(amounten.get())
    try:
        if amount < 3000:
            raise ValueError(messagebox.showinfo('Message',"please deposite more money"))
    except ValueError as e:
        print(e)
        amounten.delete(0, END)

    else:
        messagebox.showinfo('Message',"You qualify")
        amounten.delete(0, END)
    finally:
        print("transaction complete")

def exit():
    mywin2.destroy()

extbtn = Button(mywin2, text="exit", command=exit)
extbtn.config(bg="linen")
extbtn.pack(side=TOP)

checkbutton = Button(mywin2, text="Check qualification", command=malaysia)
checkbutton.config(bg="Linen")
checkbutton.pack(side=TOP)
mywin2.mainloop()