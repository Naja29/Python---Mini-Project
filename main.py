from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database

db = Database("Employee.db")
root = Tk()
root.title("Cab Service")
root.geometry("1920x1080+0+0")
root.config(bg="#2c3e50")
root.state("zoomed")

name=StringVar()
contact=StringVar()
vehicle=StringVar()
number=StringVar()
vehicleName=StringVar()
email=StringVar()

# Entries Frame
entries_frame = Frame(root, bg="#535c68")
entries_frame.pack(side=TOP, fill=X)
title = Label(entries_frame, text="Cab Service System", font=("Calibri", 18, "bold"), bg="#535c68", fg="white")
title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")

lblName = Label(entries_frame, text="Name", font=("Calibri", 16), bg="#535c68", fg="white")
lblName.grid(row=1, column=0, padx=10, pady=10, sticky="w")
txtName = Entry(entries_frame, textvariable=name, font=("Calibri", 16), width=20)
txtName.grid(row=1, column=1, padx=10, pady=10)

lblContact = Label(entries_frame, text="Contact Number", font=("Calibri", 16), bg="#535c68", fg="white")
lblContact.grid(row=1, column=2, padx=10, pady=10, sticky="w")
txtContact = Entry(entries_frame, textvariable=contact, font=("Calibri", 16), width=20)
txtContact.grid(row=1, column=3, padx=10, pady=10)

lblVehicle = Label(entries_frame, text="Vehicle Type", font=("Calibri", 16), bg="#535c68", fg="white")
lblVehicle.grid(row=2, column=0, padx=10, pady=10, sticky="w")
comboVehicle = ttk.Combobox(entries_frame, font=("Calibri", 15), width=20, textvariable=vehicle, state="readonly")
comboVehicle['values'] = ("Car", "Van", "3 Wheeler", "Truck","Lorry" )
comboVehicle.grid(row=2, column=1, padx=10, sticky="w")

lblNumber = Label(entries_frame, text="Vehicle Number", font=("Calibri", 16), bg="#535c68", fg="white")
lblNumber.grid(row=2, column=2, padx=10, pady=10, sticky="w")
txtNumber = Entry(entries_frame, textvariable=number, font=("Calibri", 16), width=20)
txtNumber.grid(row=2, column=3, padx=10, pady=10)

lblvehicleName = Label(entries_frame, text="Vehicle Model", font=("Calibri", 16), bg="#535c68", fg="white")
lblvehicleName.grid(row=3, column=0, padx=10, pady=10, sticky="w")
txtvehicleName = Entry(entries_frame, textvariable=vehicleName, font=("Calibri", 16), width=20)
txtvehicleName.grid(row=3, column=1, padx=10, pady=10)

lblEmail = Label(entries_frame, text="E-Mail", font=("Calibri", 16), bg="#535c68", fg="white")
lblEmail.grid(row=3, column=2, padx=10, pady=10, sticky="w")
txtEmail = Entry(entries_frame, textvariable=email, font=("Calibri", 16), width=20)
txtEmail.grid(row=3, column=3, padx=10, pady=10)

lblAddress = Label(entries_frame, text="Address", font=("Calibri", 16), bg="#535c68", fg="white")
lblAddress.grid(row=4, column=0, padx=10, pady=10, sticky="w")
txtAddress = Text(entries_frame, width=60, height=5, font=("Calibri",16))
txtAddress.grid(row=5, column=0, columnspan=4, padx=10, sticky="w")

def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    #print(row)
    name.set(row[1])
    contact.set(row[2])
    vehicle.set(row[3])
    number.set(row[4])
    vehicleName.set(row[5])
    email.set(row[6])
    txtAddress.delete(1.0, END)
    txtAddress.insert(END, row[7])

def dispalyAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("", END, values=row)


def add_employee():
    if txtName.get() == "" or txtContact.get() == "" or comboVehicle.get() == "" or txtNumber.get() == "" or txtvehicleName.get() == "" or txtEmail.get() == "" or txtAddress.get(
            1.0, END) == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    db.insert(txtName.get(),txtContact.get(), comboVehicle.get() , txtEmail.get() ,txtNumber.get(), txtvehicleName.get(), txtEmail.get(), txtAddress.get(
            1.0, END))
    messagebox.showinfo("Success", "Record Inserted")
    clearAll()
    dispalyAll()



def update_employee():
    if txtName.get() == "" or txtContact.get() == "" or comboVehicle.get() == "" or txtNumber.get() == "" or txtvehicleName.get() == "" or txtEmail.get() == "" or txtAddress.get(
            1.0, END) == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    db.update(row[0],txtName.get(),txtContact.get(), comboVehicle.get() , txtEmail.get() ,txtNumber.get(), txtvehicleName.get(), txtEmail.get(), txtAddress.get(
            1.0, END))
    messagebox.showinfo("Success", "Record Update")
    clearAll()
    dispalyAll()


def delete_employee():
    db.remove(row[0])
    clearAll()
    dispalyAll()


def clearAll():
    name.set("")
    contact.set("")
    vehicle.set("")
    number.set("")
    vehicleName.set("")
    email.set("")
    txtAddress.delete(1.0, END)


btn_frame = Frame(entries_frame, bg="#535c68")
btn_frame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="w")
btnAdd = Button(btn_frame, command=add_employee, text="Add", width=15, font=("Calibri", 16, "bold"), fg="white",
                bg="#16a085", bd=0).grid(row=0, column=0)
btnEdit = Button(btn_frame, command=update_employee, text="Update", width=15, font=("Calibri", 16, "bold"),
                 fg="white", bg="#2980b9",
                 bd=0).grid(row=0, column=1, padx=10)
btnDelete = Button(btn_frame, command=delete_employee, text="Delete", width=15, font=("Calibri", 16, "bold"),
                   fg="white", bg="#c0392b",
                   bd=0).grid(row=0, column=2, padx=10)
btnClear = Button(btn_frame, command=clearAll, text="Clear", width=15, font=("Calibri", 16, "bold"), fg="white",
                  bg="#f39c12",
                  bd=0).grid(row=0, column=3, padx=10)

# Table Frame
tree_frame = Frame(root, bg="#ecf0f1")
tree_frame.place(x=0, y=480, width=1980, height=520)
style = ttk.Style()
style.configure("mystyle.Treeview", font=('Calibri', 18),
                rowheight=50)  # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  # Modify the font of the headings
tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1", width=3)
tv.heading("2", text="Name")
tv.column("2", width=3)
tv.heading("3", text="Vehicle")
tv.column("3", width=3)
tv.heading("4", text="Vehicle Model")
tv.column("4", width=3)
tv.heading("5", text="Vehicle Number")
tv.column("5", width=3)
tv.heading("6", text="Email")
tv.column("6", width=3)
tv.heading("7", text="Contact")
tv.column("7", width=3)
tv.heading("8", text="Address")

tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)

dispalyAll()
root.mainloop()
