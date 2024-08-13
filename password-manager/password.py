import tkinter as tk
from tkinter import messagebox
#password generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)
password_letter=[random.choice(letters)for _ in range(nr_letters)]
password_symbol=[random.choice(symbols) for _ in range(nr_symbols)]
password_number=[random.choice(numbers)for _ in range(nr_numbers)]
password_list=password_letter+password_number+password_symbol
random.shuffle(password_list)
def generate():
    password= ""
    password= password.join(password_list)
    pass_entry.insert(0,f"{password}")
    print(f"Your password is: {password}")

#functions
def save():
    web=web_entry.get()
    email=email_entry.get()
    password=pass_entry.get()
    is_ok=True
    if len(password)==0 or len(web)==0:
        is_ok=False
    is_dn=messagebox.askokcancel(title=web,message=f"these are the entered details:\nwebsite name:{web}\nemail:{email}\npassword name:{password}")
    if is_dn and is_ok:
            with open("data.txt","a")as data_file:
                data_file.write(f"\nwebsite name:{web}|email name:{email}|password name:{password}")
                web_entry.delete(0,tk.END)
                pass_entry.delete(0,tk.END)


#window
window=tk.Tk()
window.title("Password manager")
window.config(padx=50,pady=10,bg="light yellow")
#canvas
canvas=tk.Canvas(height=200,width=200)
canvas.config(bg="light yellow",highlightthickness=0)
img=tk.PhotoImage(file="pass.png")
canvas.create_image(130,100,image=img)
canvas.grid(row=0,column=1)
#labels
website_label=tk.Label(text="Website",bg="light yellow",fg="black")
website_label.grid(row=1,column=0)
email_label=tk.Label(text="email",bg="light yellow",fg="black")
email_label.grid(row=2,column=0)
password_label=tk.Label(text="password",bg="light yellow",fg="black")
password_label.grid(row=3,column=0)

#Entries
web_entry=tk.Entry(width=35)
web_entry.config(bg="light yellow",highlightthickness=0,fg="black",insertbackground="red")
web_entry.grid(row=1,column=1,columnspan=2)
web_entry.focus()
email_entry=tk.Entry(width=35)
email_entry.config(bg="light yellow",highlightthickness=0,fg="black",insertbackground="red")
email_entry.insert(0,"umesh1002@gmail.com")
email_entry.grid(row=2,column=1,columnspan=2)
pass_entry=tk.Entry(width=20)
pass_entry.config(bg="light yellow",highlightthickness=0,fg="black",insertbackground="red")
pass_entry.grid(row=3,column=1)
#buttons
generate=tk.Button(text="Generate password",width=11,command=generate)
generate.config(borderwidth=1,highlightthickness=0,pady=2)
generate.grid(row=3,column=2)
add=tk.Button(text="Add",width=36,command=save)
add.config(borderwidth=1,highlightthickness=0,pady=2)
add.grid(row=4,column=1,columnspan=2)



window.mainloop()
