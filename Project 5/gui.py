import tkinter as tk
from tkinter import messagebox

# إنشاء النافذة الرئيسية
root = tk.Tk()
root.title("مثال على واجهة GUI")
root.geometry("300x200")


# دالة عند الضغط على الزر
def say_hello():
    name = entry.get()
    messagebox.showinfo("مرحبًا", f"مرحبًا يا {name}!")


# تسمية
label = tk.Label(root, text="أدخل اسمك:")
label.pack(pady=5)

# مربع إدخال
entry = tk.Entry(root)
entry.pack(pady=5)

# زر
button = tk.Button(root, text="اضغط هنا", command=say_hello)
button.pack(pady=10)

# بدء تشغيل البرنامج
root.mainloop()
