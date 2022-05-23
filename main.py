# Name: Group 8
# File: main.py
# Course: COP 3710
# Description: This file is intended to be the main application file
# in order to display all database internship information using tkinter
# ----------------------------------------------------------------------------------------------------------------------


# GUI libraries
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview

# local python files
import Select
import delete
import insert
import update

# create frame for main functionalities
app = Tk()
frame_search = Frame(app)
frame_search.grid(row=0, column=0)

# allows user to search by internship name and creates section for the search bar
lbl_search = Label(frame_search, text='Search by Internship',
                   font=('bold', 12), pady=20)
lbl_search.grid(row=0, column=0, sticky=W)
internship_search = StringVar()
internship_search_entry = Entry(frame_search, textvariable=internship_search)
internship_search_entry.grid(row=0, column=1)

# allows user to search by a standard DML query and creates a section for it
lbl_search = Label(frame_search, text='Search by Query',
                   font=('bold', 12), pady=20)
lbl_search.grid(row=1, column=0, sticky=W)
query_search = StringVar()
query_search.set("SELECT * FROM internship where internship_name = 'software developer'")
query_search_entry = Entry(frame_search, textvariable=query_search, width=40)
query_search_entry.grid(row=1, column=1)

# creates frame for database information to be displayed
frame_fields = Frame(app)
frame_fields.grid(row=1, column=0)

frame_internship = Frame(app)
frame_internship.grid(row=4, column=0, columnspan=4, rowspan=6, pady=20, padx=20)

# creates table to display all database information
columns = ['id', 'Internship Name', 'Internship ID', 'Salary', 'Company']
internship_tree_view = Treeview(frame_internship, columns=columns, show="headings")
internship_tree_view.column("id", width=40)
for col in columns[1:]:
    internship_tree_view.column(col, width=120)
    internship_tree_view.heading(col, text=col)
internship_tree_view.bind('<<TreeviewSelect>>')
internship_tree_view.pack(side="left", fill="y")
scrollbar = Scrollbar(frame_internship, orient='vertical')  # creates scroll bar
scrollbar.configure(command=internship_tree_view.yview)
scrollbar.pack(side="right", fill="y")
internship_tree_view.config(yscrollcommand=scrollbar.set)

frame_fields = Frame(app)
frame_fields.grid(row=1, column=0)
# Internship ID label
internship_ID_text = StringVar()
internship_ID_label = Label(frame_fields, text='Internship ID', font=('bold', 12))
internship_ID_label.grid(row=0, column=0, sticky=E)
internship_ID_entry = Entry(frame_fields, textvariable=internship_ID_text)
internship_ID_entry.grid(row=0, column=1, sticky=W)
# Internship Name label
internship_name_text = StringVar()
internship_name_label = Label(frame_fields, text='Job Title', font=('bold', 12))
internship_name_label.grid(row=0, column=2, sticky=E)
internship_name_entry = Entry(frame_fields, textvariable=internship_name_text)
internship_name_entry.grid(row=0, column=3, sticky=W)
# Company label
company_text = StringVar()
company_label = Label(frame_fields, text='Company', font=('bold', 12))
company_label.grid(row=1, column=0, sticky=E)
company_entry = Entry(frame_fields, textvariable=company_text)
company_entry.grid(row=1, column=1, sticky=W)
# Salary label
salary_text = StringVar()
salary_label = Label(frame_fields, text='Salary', font=('bold', 12), pady=20)
salary_label.grid(row=1, column=2, sticky=E)
salary_entry = Entry(frame_fields, textvariable=salary_text)
salary_entry.grid(row=1, column=3, sticky=W)


# create a populate function to get internship names
def populate_list(internship_name=''):
    for i in internship_tree_view.get_children():
        internship_tree_view.delete(i)
    for row in Select.Select.fetch(internship_name):
        internship_tree_view.insert('', 'end', values=row)


# create a populate function to get information only from the internship table
def populate_list2(query='select * from INTERNSHIP'):
    for i in internship_tree_view.get_children():
        internship_tree_view.delete(i)
    for row in Select.Select.fetch2(query):
        internship_tree_view.insert('', 'end', values=row)


# create function to add internship
def add_internship():
    if internship_name_text.get() == '' or internship_ID_text.get() == '' or company_text.get() == '' or salary_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    insert.Insert.insert(internship_ID_text.get(), internship_name_text.get(),
                         company_text.get(), salary_text.get())
    clear_text()
    populate_list()


# create select internship function that can select information from the given fields below
def select_internship(event):
    try:
        global selected_item
        index = internship_tree_view.selection()[0]
        selected_item = internship_tree_view.item(index)['values']
        internship_ID_entry.delete(0, END)
        internship_ID_entry.insert(END, selected_item[1])
        internship_name_entry.delete(0, END)
        internship_name_entry.insert(END, selected_item[2])
        company_entry.delete(0, END)
        company_entry.insert(END, selected_item[3])
        salary_entry.delete(0, END)
        salary_entry.insert(END, selected_item[4])
    except IndexError:
        pass


# create function to remove internships
def remove_internship():
    delete.Delete.remove(selected_item[0])
    clear_text()
    populate_list()


# create function to update internships
def update_internship():
    update.Update.update(selected_item[0], internship_ID_text.get(), internship_name_text.get(),
                         company_text.get(), salary_text.get())
    populate_list()


# create function to clear written text in the search bar
def clear_text():
    internship_name_entry.delete(0, END)
    internship_ID_entry.delete(0, END)
    company_entry.delete(0, END)
    salary_entry.delete(0, END)


# create function to search for internships
def search_internship():
    internship = internship_search.get()
    populate_list(internship)


# create function to execute a query to get all internship information
def execute_query():
    query = query_search.get()
    populate_list2(query)


# create button variables and display them on the front end page
frame_btns = Frame(app)
frame_btns.grid(row=3, column=0)

add_btn = Button(frame_btns, text='Add Internship', width=12, command=add_internship)
add_btn.grid(row=0, column=0, pady=20)

remove_btn = Button(frame_btns, text='Remove internship',
                    width=12, command=remove_internship)
remove_btn.grid(row=0, column=1)

update_btn = Button(frame_btns, text='Update internship',
                    width=12, command=update_internship)
update_btn.grid(row=0, column=2)

clear_btn = Button(frame_btns, text='Clear Input',
                   width=12, command=clear_text)
clear_btn.grid(row=0, column=3)

search_btn = Button(frame_search, text='Search',
                    width=12, command=search_internship)
search_btn.grid(row=0, column=2)

search_query_btn = Button(frame_search, text='Search Query',
                          width=12, command=execute_query)
search_query_btn.grid(row=1, column=2)

# front end page size and name
app.title('Internship Search')
app.geometry('700x550')

# Start program
app.mainloop()
