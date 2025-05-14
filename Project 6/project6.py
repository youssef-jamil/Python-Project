import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename


def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if not filepath:
        return

    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)

    window.title(f"AlmdrasaTextEditor - {filepath}")


def save_file():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )

    if not filepath:
        return

    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)

    window.title(f"AlmdrasaTextEditor - {filepath}")


window = tk.Tk()
window.title("Almdrasa Text Editor")

# استخدم grid بدلاً من pack هنا
greeting = tk.Label(text="Welcome to Almdrasa Text Editor")
greeting.grid(column=0, row=0, columnspan=2, pady=10)

window.rowconfigure(1, minsize=600)
window.columnconfigure(1, minsize=800)

txt_edit = tk.Text(window)
frame_buttons = tk.Frame(window, relief=tk.RAISED)

frame_buttons.grid(column=0, row=1, sticky="ns")
txt_edit.grid(column=1, row=1, sticky="nsew")

btn_open = tk.Button(
    frame_buttons,
    text="Open File",
    command=open_file,
)
btn_save = tk.Button(
    frame_buttons,
    text="Save As",
    command=save_file,
)

btn_open.grid(column=0, row=0, sticky="ew", padx=5, pady=5)
btn_save.grid(column=0, row=1, sticky="ew", padx=5)

window.mainloop()
