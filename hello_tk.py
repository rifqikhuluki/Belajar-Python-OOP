import tkinter as tk

def say_hello():
    label.config(text="Hello World")

root = tk.Tk()
root.title('Tkinter Hello world')
root.geometry('300x200')

label = tk.Label(root, text="Tekan Button")
label.pack(pady=20)

tombol = tk.Button(root, text="button", command=say_hello)
tombol.pack()

root.mainloop()