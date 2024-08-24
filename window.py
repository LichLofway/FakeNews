import tkinter as tk
import sys
import import_ipynb

root = tk.Tk()
root.title("Check news")
root.geometry("800x400")

label = tk.Label(root, text="Title of article:")
label.pack(pady=5)

entry = tk.Text(root, width=50, height=2)
entry.pack(pady=5)

tf = tk.Label()
tf.pack(pady=5)

def on():
    
    tf["text"] = entry.get("1.0", "end")
 

button = tk.Button(root, text="Check", command=on)
button.pack(pady=20)

root.mainloop()
