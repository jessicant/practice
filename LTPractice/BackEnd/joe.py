from msilib.schema import ListBox
import tkinter
import tkinter.messagebox

root = tkinter.Tk()
root.title("To-Do List Practice by Joe Sluis")


def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="Enter task")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except: 
        tkinter.messagebox.showwarning(title="Warning!", message="Select task")

def load_tasks():
    pass

#create GUI

listbox_tasks = tkinter.Listbox(root, height=20, width=75)
listbox_tasks.pack()

entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

button_add_task = tkinter.Button(root, text="Add task", width=48, command=add_task)
button_add_task.pack()

button_delete_task = tkinter.Button(root, text="Delete task", width=48, command=delete_task)
button_delete_task.pack()

root.mainloop()
