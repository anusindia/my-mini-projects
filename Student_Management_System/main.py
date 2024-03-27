from tkinter import *
from tkinter import ttk
from studentdb import StudentDatabase
from tkinter import messagebox

studentdb=StudentDatabase()
root=Tk()
root.geometry('1350x695+0+0')
root.title("Student Database System")
root.resizable(height="false", width="false")
root.configure(bg="#212121")

#Assigning Variables
id=StringVar()
fname=StringVar()
lname=StringVar()
gender=StringVar()
dob=StringVar()
dept=StringVar()
cont=StringVar()
email=StringVar()
#addr=StringVar()
com_search=StringVar()
ent_search=StringVar()

#Style for student detail frame
style=ttk.Style()
style.configure('TFrame', background='#212121', foreground="white")
#heading Label

head_label=ttk.Label(master=root, text="STUDENT DATABASE MANAGEMENT SYSTEM", font=('Britannic Bold',30,"bold"),border=12, relief="raise" ,background="#212121", foreground="#175EAE",padding=(240,10))
head_label.pack(side="top",expand=False,fill="none")

#FRAMES

#student details Frame
stu_frame=ttk.Frame(master=root,width=400, height=605, borderwidth=10,relief="raise", style="TFrame")
stu_frame.place(x=4,y=77)

#Main Db Table Frame 
main_frame=ttk.Frame(master=root, width=880, height=600, borderwidth=10,relief="groove" ,style="TFrame")
main_frame.pack_propagate("false")
main_frame.pack(side="right")

#Detail Frame Widgets

stu_det_label=ttk.Label(master=stu_frame, text="Enter Student Details:", font=('TimesNewRoman',25,"underline"),background="#212121", foreground="#175EAE")
stu_det_label.place(x=2, y=5)

stu_label1=ttk.Label(master=stu_frame, text="First Name:", font=('TimesNewRoman',15), background="#212121", foreground="white")
stu_label1.place(x=2, y=60)
stu_label2=ttk.Label(master=stu_frame, text="Last Name:", font=('TimesNewRoman',15), background="#212121", foreground="white")
stu_label2.place(x=2, y=110)
stu_label3=ttk.Label(master=stu_frame, text="Gender:", font=('TimesNewRoman',15), background="#212121", foreground="white")
stu_label3.place(x=2, y=160)
stu_label4=ttk.Label(master=stu_frame, text="Date Of Birth:", font=('TimesNewRoman',15), background="#212121", foreground="white")
stu_label4.place(x=2, y=210)
stu_label5=ttk.Label(master=stu_frame, text="Department:", font=('TimesNewRoman',15), background="#212121", foreground="white")
stu_label5.place(x=2, y=260)
stu_label6=ttk.Label(master=stu_frame, text="Contact:", font=('TimesNewRoman',15), background="#212121", foreground="white")
stu_label6.place(x=2, y=310)
stu_label7=ttk.Label(master=stu_frame, text="Email:", font=('TimesNewRoman',15), background="#212121", foreground="white")
stu_label7.place(x=2, y=360)
stu_label8=ttk.Label(master=stu_frame, text="Address:", font=('TimesNewRoman',15), background="#212121", foreground="white")
stu_label8.place(x=2, y=410)

 
#Entries

stu_fnentry=ttk.Entry(master=stu_frame, textvariable=fname, font=("calibri",11), width=30)
stu_fnentry.place(x=130, y=61)
stu_lnentry=ttk.Entry(master=stu_frame, textvariable=lname, font=("calibri",11), width=30)
stu_lnentry.place(x=130, y=111)
stu_dobentry=ttk.Entry(master=stu_frame, textvariable=dob,font=("calibri",11), width=30)
stu_dobentry.place(x=130, y=211)
stu_deptentry=ttk.Entry(master=stu_frame, textvariable=dept,font=("calibri",11), width=30)
stu_deptentry.place(x=130, y=261)
stu_contentry=ttk.Entry(master=stu_frame,textvariable=cont,font=("calibri",11), width=30)
stu_contentry.place(x=130, y=311)
stu_emlentry=ttk.Entry(master=stu_frame, textvariable=email,font=("calibri",11), width=30)
stu_emlentry.place(x=130, y=361)
stu_addrtext=Text(master=stu_frame, background="white", foreground="black", height = 5, width = 45)
stu_addrtext.place(x=6, y=435)

#combobox entry
combo_gender=ttk.Combobox(master=stu_frame, textvariable=gender,state="readonly",font=("calibri",11),  width=30)
combo_gender["values"]=("Male","Female")
combo_gender.place(x=130,y=161)

def getData(event):
    """
    Update the entry fields with the data of the selected row in the Treeview widget.
    Args:
        event: The event that triggered this function, typically a click event.
    Returns:
        None
    """
    selected_row=details.focus()
    data=details.item(selected_row)
    global row
    row=data["values"]
    #print(row)
    fname.set(row[1])
    lname.set(row[2])
    gender.set(row[3])
    dob.set(row[4])
    dept.set(row[5])
    cont.set(row[6])
    email.set(row[7])
    stu_addrtext.delete(1.0,END)
    stu_addrtext.insert(END,row[8])

def displayall():
    """
    Display all records from the database in the Treeview widget.

    This function retrieves all records from the database using the fetch_data method of the studentdb object.
    It then iterates over each record and inserts them into the Treeview widget.

    Returns:
        None
    """
    details.delete(*details.get_children())
    for rows in studentdb.fetch_data():
        details.insert("",END,values=rows)

def add_stu():
    """
    Add a new student record to the database.

    This function retrieves the values entered by the user in the GUI fields (first name, last name, gender, date of birth, department, contact, email, and address).
    It then checks if any of the required fields are empty. If any of them are empty, it displays an error message and returns.
    Otherwise, it calls the stu_insert method of the studentdb object to insert the new record into the database.
    After successful insertion, it displays a success message, clears all the input fields, and updates the display to show the newly inserted record.

    Returns:
        None
    """
    if fname.get()=="" or lname.get()=="" or gender.get()=="" or dob.get()=="" or dept.get()=="" or cont.get()=="" or email.get()==""  or stu_addrtext.get(1.0,END)=="":
        messagebox.showerror("Error Message","Please Fill all the Details!")
        return
    studentdb.stu_insert((fname.get(),lname.get(),gender.get(), dob.get(), dept.get(),cont.get(),email.get(),stu_addrtext.get(1.0,END)))
    messagebox.showinfo("Success","Record inserted!!!")
    clearall()
    displayall()

def update_stu():
    """
    Update an existing student record in the database.

    This function first checks if all the required fields are filled by the user in the GUI.
    If any required field is empty, it displays an error message and returns.
    Otherwise, it calls the stu_update method of the studentdb object to update the selected record in the database.
    After successful update, it displays a success message, clears all the input fields, and updates the display to reflect the changes.

    Returns:
        None
    """

    if fname.get()=="" or lname.get()=="" or gender.get()==""or dob.get()=="" or dept.get()=="" or cont.get()=="" or email.get()=="" or stu_addrtext.get(1.0,END)=="":
        messagebox.showerror("Error Message","Please Fill all the Details!")
        return
    studentdb.stu_update(row[0],fname.get(),lname.get(),gender.get(), dob.get(), dept.get(), cont.get(),email.get(),stu_addrtext.get(1.0,END))
    messagebox.showinfo("Success","Record Updated!!!")
    clearall()
    displayall()

def delete_stu():
    """
    Delete a student record from the database.

    This function deletes the currently selected student record from the database by calling the stu_delete method of the studentdb object.
    After deletion, it clears all the input fields and updates the display to reflect the changes.

    Returns:
        None
    """
    studentdb.stu_delete(row[0])
    clearall()
    displayall()

def clearall():
    """
    Delete a student record from the database.

    This function deletes the currently selected student record from the database by calling the stu_delete method of the studentdb object.
    After deletion, it clears all the input fields and updates the display to reflect the changes.

    Returns:
        None
    """
    fname.set("")
    lname.set("")
    gender.set("")
    dob.set("")
    dept.set("")
    cont.set("")
    email.set("")
    stu_addrtext.delete(1.0,END)

def search_data():
    """
    Search for student records in the database.

    This function first checks if the search criteria are provided by the user in the GUI.
    If any required field is empty, it displays an error message and returns.
    Otherwise, it calls the stu_search method of the studentdb object to search for records based on the provided criteria.

    Returns:
        None
    """
    if com_search.get()=="" or ent_search.get()=="":  
        messagebox.showerror("Error", "Please select the Correct Option")
        return
    rows=studentdb.stu_search(com_search.get(),ent_search.get())
    details.delete(*details.get_children())
    for row in rows :
        details.insert("",END,values=row)
    clearall()


#Buttons

stu_button1=Button(master=stu_frame, command=add_stu, text="ADD RECORD",width=10,background="green", foreground="white")
stu_button1.place(x=2, y=535)
stu_button2=Button(master=stu_frame, command=update_stu, text="UPDATE RECORD", width=13,background="blue", foreground="white")
stu_button2.place(x=92, y=535)
stu_button2=Button(master=stu_frame, command=delete_stu,text="DELETE RECORD", width=13,background="red", foreground="white")
stu_button2.place(x=205, y=535)
stu_button2=Button(master=stu_frame, command=clearall,text="CLEAR ALL", width=8,background="#FFA833", foreground="white")
stu_button2.place(x=315, y=535)

#====== SEARCH ====#

#search Frame
search_frame=ttk.Frame(master=main_frame, width=860,height=50, borderwidth=10,relief="raised", style="TFrame")
search_frame.pack(side="top")
#Search Buttons and entries
search_label=ttk.Label(master=search_frame, text="Search By", font=('TimesNewRoman',17), background="#212121", foreground="white")
search_label.place(x=4,y=0)
search_in=ttk.Combobox(master=search_frame,font=('TimesNewRoman',14),textvariable=com_search,  width=20, state="readonly")
search_in["values"] =("ID", "First_name", "Last_name","Department", "Contact")
search_in.place(x=125,y=0)
search_entry=ttk.Entry(master=search_frame, textvariable=ent_search, font=("calibri",14), width=19)
search_entry.place(x=380, y=0)
search_btn=Button(master=search_frame, text="Search", command=search_data, width=10,background="blue", foreground="white" )
search_btn.place(x=600, y=2)
showall_btn=Button(master=search_frame, text="Show All", command=displayall, width=12,background="green", foreground="white" )
showall_btn.place(x=695, y=2)

#===== STUDENT DB TREEVIEW ====#
x_scroll=ttk.Scrollbar(master=main_frame,orient=HORIZONTAL)
y_scroll=ttk.Scrollbar(master=main_frame,orient=VERTICAL)

#style
#style.configure("Treeview", font=("times",12), rowheight=30)
#style.configure("Treeeview.Heading",font=("calibri",16,"bold"))

details=ttk.Treeview(master=main_frame,columns=("ID","First Name","Last Name","Gender","DOB","Department","Contact","email","Address"), xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set)
details.heading("ID", text="ID")
details.column("ID", width=50)
details.heading("First Name", text="First Name")
details.column("First Name", width=110)
details.heading("Last Name", text="Last Name")
details.column("Last Name", width=110)
details.heading("Gender", text="Gender")
details.column("Gender", width=60)
details.heading("DOB", text="Date Of Birth")
details.column("DOB", width=100)
details.heading("Department", text="Department")
details.column("Department", width=110)
details.heading("Contact", text="Contact")
details.column("Contact", width=130)
details.heading("email", text="E-mail")
details.column("email", width=130)
details.heading("Address", text="Address", anchor="sw")
details.column("Address", width=200)
details['show']='headings'
details.bind("<ButtonRelease-1>",getData)
y_scroll.config(command=details.yview)
x_scroll.config(command=details.xview)
y_scroll.pack(side=RIGHT, fill=Y)
x_scroll.pack(side=BOTTOM,fill=X)
details.pack(fill=BOTH, expand=True)
displayall() 
root.mainloop()






