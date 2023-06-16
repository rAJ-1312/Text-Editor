import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def new_file():
    text.delete("1.0", tk.END)

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            text.delete("1.0", tk.END)
            text.insert(tk.END, content)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        content = text.get("1.0", tk.END)
        with open(file_path, "w") as file:
            file.write(content)
        messagebox.showinfo("Information", "File saved successfully.")

def copy_text():
    text.clipboard_clear()
    text.clipboard_append(text.selection_get())

def paste_text():
    text.insert(tk.INSERT, text.clipboard_get())

def undo_text():
    try:
        text.edit_undo()
    except tk.TclError:
        pass

def redo_text():
    try:
        text.edit_redo()
    except tk.TclError:
        pass

def set_bold():
    text.tag_add("bold", "sel.first", "sel.last")
    text.tag_config("bold", font=("TkDefaultFont", 11, "bold"))

def set_italic():
    text.tag_add("italic", "sel.first", "sel.last")
    text.tag_config("italic", font=("TkDefaultFont", 11, "italic"))

def set_normal():
    text.tag_remove("bold", "sel.first", "sel.last")
    text.tag_remove("italic", "sel.first", "sel.last")

root = tk.Tk()
root.title("Text Editor")

text = tk.Text(root)
text.pack()

menu = tk.Menu(root)
file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=file_menu)

edit_menu = tk.Menu(menu, tearoff=0)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)
edit_menu.add_command(label="Undo", command=undo_text)
edit_menu.add_command(label="Redo", command=redo_text)
menu.add_cascade(label="Edit", menu=edit_menu)

format_menu = tk.Menu(menu, tearoff=0)
format_menu.add_command(label="Bold", command=set_bold)
format_menu.add_command(label="Italic", command=set_italic)
format_menu.add_command(label="Normal", command=set_normal)
menu.add_cascade(label="Format", menu=format_menu)

root.config(menu=menu)
root.mainloop()
