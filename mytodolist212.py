import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def edit_task():
    try:
        task_index = task_listbox.curselection()[0]
        selected_task = task_listbox.get(task_index)
        task_entry.delete(0, tk.END)
        task_entry.insert(tk.END, selected_task)
        delete_task()
    except IndexError:
        pass

def delete_task():
    try:
        task_index = task_listbox.curselection()[0]
        task_listbox.delete(task_index)
    except IndexError:
        pass

def complete_task():
    try:
        task_index = task_listbox.curselection()[0]
        task_listbox.itemconfig(task_index, {'bg':'light yellow'})
    except IndexError:
        pass

root = tk.Tk()
root.title("My To-Do List")

root.geometry("300x400") # Set the window size
root.configure(bg="light grey") # Set the background color

tasks_frame = tk.Frame(root, bg="light grey")
tasks_frame.pack(pady=12)

task_listbox = tk.Listbox(tasks_frame, height=10, width=50, bg="white", fg="black", border=0)
task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

tasks_scrollbar = tk.Scrollbar(tasks_frame)
tasks_scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

task_listbox.config(yscrollcommand=tasks_scrollbar.set)
tasks_scrollbar.config(command=task_listbox.yview)

task_entry = tk.Entry(root, width=50)
task_entry.pack()

buttons_frame = tk.Frame(root, bg="light grey")
buttons_frame.pack(pady=10)

button_add_task = tk.Button(buttons_frame, text="Add Task", command=add_task, bg="blue", fg="white")
button_add_task.pack(side=tk.LEFT)

button_edit_task = tk.Button(buttons_frame, text="Edit Task", command=edit_task, bg="blue", fg="white")
button_edit_task.pack(side=tk.LEFT)

button_delete_task = tk.Button(buttons_frame, text="Delete Task", command=delete_task, bg="blue", fg="white")
button_delete_task.pack(side=tk.LEFT)

button_complete_task = tk.Button(buttons_frame, text="Complete Task", command=complete_task, bg="blue", fg="white")
button_complete_task.pack(side=tk.LEFT)

root.mainloop()
