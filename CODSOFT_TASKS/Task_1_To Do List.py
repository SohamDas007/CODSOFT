import tkinter
from tkinter import *
from tkinter import messagebox

def Task_New():
    task=my_entry.get()
    if task!="":
        lb.insert(END, task)
        my_entry.delete(0,"end")
    else:
        messagebox.showwarning("Warning", "Please Enter some task")

def Task_Del():
    lb.delete(ANCHOR)

ws=Tk()
ws.geometry("500x450+500+200")
ws.title("To Do Lists GUI")
ws.config(bg="#223441")
ws.resizable(False,False)

frame=Frame(ws)
frame.pack(pady=10)

lb=Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle='none',
)

lb.pack(side=LEFT, fill=BOTH)

task_list=[
    "Eat Lunch",
    "Drink Water",
    "Go to Swimming",
    "Complete the Assignment",
    "Sleep",
    "Read a Book",
    "Practice Cricket",
    "Take a Walk"
    ]

for item in task_list:
    lb.insert(END, item)

scroll=Scrollbar(frame)
scroll.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=scroll.set)
scroll.config(command=lb.yview)

my_entry=Entry(
    ws,
    font=('times',24)
    )

my_entry.pack(pady=20)

button_Frame=Frame(ws)
button_Frame.pack(pady=20)

addTask_btn= Button(
    button_Frame,
    text="Add Task",
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=Task_New
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_Frame,
    text='Delete Task',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=Task_Del
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

ws.mainloop()
