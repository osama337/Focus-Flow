from tkinter import *
from tkinter import messagebox


def add_tasks(event=None):
  task = write_list.get()
  if task:
        tasks.append(task)
        listbox.insert(END, task)
        write_list.delete(0, END)
        print(tasks)
  else:
      messagebox.showerror("Error", "Please enter a task to load.")

def load_tasks():
  try:
        listbox.delete(0, END) 
        tasks.clear()
        with open("tasks.txt", "r", encoding="utf-8") as f:
            for line in f:
                task = line.strip()
                tasks.append(task)
                listbox.insert(END, task)
  except FileNotFoundError:
        messagebox.showerror("Error", "Please Enter a task to load.")

def delete_tasks(event=None):
    try:
        selected_index = listbox.curselection()[0]
        listbox.delete(selected_index)
        tasks.pop(selected_index)
    except IndexError:
        messagebox.showerror("Error", "Please select a task to delete.")
        
def save_tasks(event=None):
    try:
        all_tasks = listbox.get(0, END)
        with open("tasks.txt", "w", encoding="utf-8") as f:
            for task in all_tasks:
                f.write(task + "\n")
        messagebox.showinfo("Success", "Tasks saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Could not save: {e}")
        
root = Tk()
root.title("To do list")
root.geometry("1200x600")
root.iconbitmap("P.ico")

tasks = []

root.configure(bg="#2d3436")

do = StringVar()
do.set("")

label = Label(root,
                text="Enter To Do List",
                font=("Arial", 18),
                bg="#2d3436",
                fg="lightblue",
).place(relx=0.55,
        rely=0.05,
        anchor=CENTER,
        relheight=0.1,
        relwidth=0.2)

label2 = Label(root,
                bg="#1e272e"
        ).place(relx=0.0,
        rely=0.0,
        anchor="nw",
        relheight=1.0,
        relwidth=0.2)

write_list = Entry(root,
                font=("Arial", 18),
                border=3,
                bg="white",
                fg="black",
                textvariable=do,
)
write_list.place(relx=0.55,
        rely=0.15,
        anchor=CENTER,
        relheight=0.1,
        relwidth=0.6)
write_list.focus()


listbox = Listbox(root,
                font=("Arial", 14),
                bg="#636e72", 
                fg="white",
                bd=0,
                highlightthickness=0,
                selectbackground="#00d2d3", 
                selectforeground="black"
)
listbox.place(relx=0.55,
        rely=0.55,
        anchor=CENTER,
        relwidth=0.6,
        relheight=0.6)

event = root.bind('<Return>', add_tasks)
Button(root,
        text="Add",
        font=("Arial", 14),
        bg="#00cec9",
        fg="black",
        command = add_tasks
).place(relx=0.1,
        rely=0.1,
        anchor=CENTER,
        relheight=0.05,
        relwidth=0.05)

event = root.bind('<Delete>', delete_tasks)
Button(root,
        text="delete",
        font=("Arial", 14),
        bg="#00cec9",
        fg="black",
        command = delete_tasks
).place(relx=0.1,
        rely=0.3,
        anchor=CENTER,
        relheight=0.05,
        relwidth=0.05)

Button(root,
        text="Load",
        font=("Arial", 14),
        bg="#00cec9",
        fg="black",
        command = load_tasks
).place(relx=0.1,
        rely=0.5,
        anchor=CENTER,
        relheight=0.05,
        relwidth=0.05)

Button(root,
        text="Exit",
        font=("Arial", 14),
        bg="#00cec9",
        fg="black",
        command = root.destroy
).place(relx=0.1,
        rely=0.9,
        anchor=CENTER,
        relheight=0.05,
        relwidth=0.05)
event = root.bind('<Control-s>', save_tasks)
Button(root,
        text="Save",
        font=("Arial", 14),
        bg="#00cec9",
        fg="black",
        command=save_tasks
).place(relx=0.1,
                rely=0.7,
                anchor=CENTER,
                relheight=0.05,
                relwidth=0.05)

load_tasks()

root.mainloop()