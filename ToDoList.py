import tkinter as tk
from tkinter import messagebox, font

# Initialize main application window
root = tk.Tk()
root.title("To-Do List Application")
root.geometry("500x500")
root.config(bg="#f5f5f5")  # Background color

# Global list to store tasks
tasks = []

# Function to update the listbox display
def update_listbox():
    listbox.delete(0, tk.END)  # Clear current tasks
    for task in tasks:
        listbox.insert(tk.END, task)

# Function to add a task
def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        task_entry.delete(0, tk.END)  # Clear entry field
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to delete a selected task
def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        tasks.pop(selected_task_index)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Function to mark a task as completed
def mark_task_complete():
    try:
        selected_task_index = listbox.curselection()[0]
        tasks[selected_task_index] += " - Completed"
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as complete.")

# GUI Layout and Styles
title_font = font.Font(family="Helvetica", size=16, weight="bold")
button_font = font.Font(family="Helvetica", size=10, weight="bold")
task_font = font.Font(family="Helvetica", size=12)

title_label = tk.Label(root, text="My To-Do List", font=title_font, bg="#f5f5f5", fg="#333")
title_label.pack(pady=10)

# Entry Frame
frame = tk.Frame(root, bg="#f5f5f5")
frame.pack(pady=10)

task_entry = tk.Entry(frame, width=35, font=task_font, borderwidth=2, relief="groove")
task_entry.pack(side=tk.LEFT, padx=10, pady=10)

add_task_button = tk.Button(frame, text="Add Task", font=button_font, bg="#4CAF50", fg="white", command=add_task)
add_task_button.pack(side=tk.LEFT, padx=10)

# Listbox with Scrollbar
listbox_frame = tk.Frame(root)
listbox_frame.pack(pady=10)

listbox = tk.Listbox(listbox_frame, width=50, height=15, font=task_font, selectbackground="#87CEEB", borderwidth=2, relief="groove")
scrollbar = tk.Scrollbar(listbox_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
listbox.pack()

# Control Buttons
button_frame = tk.Frame(root, bg="#f5f5f5")
button_frame.pack(pady=10)

delete_task_button = tk.Button(button_frame, text="Delete Task", font=button_font, bg="#FF6347", fg="white", command=delete_task)
delete_task_button.grid(row=0, column=0, padx=10)

complete_task_button = tk.Button(button_frame, text="Mark as Complete", font=button_font, bg="#FFA500", fg="white", command=mark_task_complete)
complete_task_button.grid(row=0, column=1, padx=10)

# Start the Tkinter event loop
root.mainloop()
