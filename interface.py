import tkinter as tk

root = tk.Tk()
root.title("B.V.C")
root.geometry("300x250")

label = tk.Label(root, text="Скажите что-нибудь", wraplength=280)
label.pack()

def set_text(text):
    root.after(0, lambda: label.config(text=text))