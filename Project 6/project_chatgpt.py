import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename


def new_file():
    txt_edit.delete("1.0", tk.END)
    window.title("Almdrasa Text Editor - New File")


def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, "r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert("1.0", text)
    window.title(f"Almdrasa Text Editor - {filepath}")


def save_file():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w", encoding="utf-8") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Almdrasa Text Editor - {filepath}")


def exit_app():
    window.destroy()


# إنشاء النافذة
window = tk.Tk()
window.title("Almdrasa Text Editor")

# قائمة Menu في الأعلى
menu_bar = tk.Menu(window)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open...", command=open_file)
file_menu.add_command(label="Save As...", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)

window.config(menu=menu_bar)

# إعداد التخطيط
window.rowconfigure(0, minsize=600)
window.columnconfigure(0, minsize=800)

# صندوق النصوص
txt_edit = tk.Text(window)
txt_edit.grid(row=0, column=0, sticky="nsew")

# تشغيل البرنامج
window.mainloop()
