from tkinter import *
import backend
from tkinter import messagebox

window = Tk()
window.title("library app")
window.resizable(width=False,height=False)
window.configure(bg='grey')

#======================= labels ==========================

label1 = Label(window,text="title:",bg='grey',font=2)
label1.grid(row=0,column=0)

label2 = Label(window,text="author:",bg='grey',font=2)
label2.grid(row=0,column=2)

label3 = Label(window,text="year:",bg='grey',font=2)
label3.grid(row=1,column=0)

label4 = Label(window,text="serial number:",bg='grey',font=2)
label4.grid(row=1,column=2)

#======================== entries ========================

title_text = StringVar()
entry1 = Entry(window,textvariable=title_text)
entry1.grid(row=0,column=1)

author_text = StringVar()
entry2 = Entry(window,textvariable=author_text)
entry2.grid(row=0,column=3)

year_text = StringVar()
entry3 = Entry(window,textvariable=year_text)
entry3.grid(row=1,column=1)

isbn_text = StringVar()
entry4 = Entry(window,textvariable=isbn_text)
entry4.grid(row=1,column=3)

list1 = Listbox(window,width=45,height=20)
list1.grid(row=2,column=0,rowspan=7,columnspan=2,padx=10,pady=10)

scrollbar = Scrollbar(window)
scrollbar.grid(row=2,column=2,rowspan=6)
list1.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = list1.yview)

#========================== buttons ==============================

def delete_list():
    list1.delete(0, END)

def list_insert(instruction):
    for i in instruction:
        list1.insert(END,i)

def view_command():
    delete_list()
    x = backend.view()
    list_insert(x)

def add_command():

    delete_list()
    if year_text.get() != "" and title_text.get() != ""\
            and author_text.get() != "" and isbn_text.get() != "":
        backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
        view_command()

    else:
        messagebox.showerror("ERROR",'the information is not complete')
        view_command()


def search_command():
    delete_list()

    if year_text.get() != "" or title_text.get() != ""\
            or author_text.get() != "" or isbn_text.get() != "":
        x = backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
        list_insert(x)

    else:
        messagebox.showerror("ERROR", 'the information is not complete')
        view_command()


def close_command():
    window.destroy()

def select_command(event):
    global y
    x = list1.curselection()[0]
    y = list1.get(x)
    entry1.delete(0,END)
    entry1.insert(END,y[1])
    entry2.delete(0,END)
    entry2.insert(END,y[2])
    entry3.delete(0,END)
    entry3.insert(END,y[3])
    entry4.delete(0,END)
    entry4.insert(END,y[4])

def delete_command():
    delete_list()
    backend.delete(y[0])
    view_command()

def update_command():
    delete_list()
    backend.update(y[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    view_command()

list1.bind('<<ListboxSelect>>', select_command)

button1 = Button(window,text="View All",width=12,bg='orange',command=lambda:view_command())
button1.grid(row=2,column=3,pady=10)

button2 = Button(window,text="Search book",width=12,bg='orange',command=search_command)
button2.grid(row=3,column=3,pady=10)

button3 = Button(window,text="Add book",width=12,bg='orange',command=add_command)
button3.grid(row=4,column=3,pady=10)

button4 = Button(window,text="Update Selected",bg='orange',width=12,command=lambda:update_command())
button4.grid(row=5,column=3,pady=10)

button5 = Button(window,text="Delete Selected",width=12,bg='orange',command=lambda:delete_command())
button5.grid(row=6,column=3,pady=10)

button5 = Button(window,text="Close",width=12,bg='orange',command=lambda:close_command())
button5.grid(row=7,column=3,pady=10)

view_command()
window.mainloop()
