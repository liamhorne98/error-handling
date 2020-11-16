from tkinter import *
from tkinter import messagebox

mywin =Tk()
mywin.title("mylogin app")
mywin.geometry("300x300")
user_label=Label(mywin, text="Username")
user_label.pack()

user_entry=Entry(mywin, textvariable="username")
user_entry.pack()
pass_label=Label(mywin, text="Password")
pass_label.pack()
pass_entry=Entry(mywin, textvariable="password", show="*")
pass_entry.pack()
def check():
	all_logs={"liam":"horne", "hi":"good", "soop": "er"}
	myuser=user_entry.get()
	password=pass_entry.get()
	if (myuser, password)in all_logs.items():
		messagebox.showinfo("INFO", "Correct Login")
		mywin.withdraw()
		import errorhandling
		errorhandling.verify()
	else:
		messagebox.showinfo("INFO", "Incorrect Login")
		user_entry.delete(0, END)
		pass_entry.delete(0, END)




mybutton= Button(mywin, text="Login ", bg="magenta", command=check).pack()
mywin.mainloop()