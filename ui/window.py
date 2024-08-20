import tkinter as tk

root = tk.Tk()
root.title("Check news")
root.geometry("800x600")

label1 = tk.Label(root, text="Title of article:")
label1.pack(pady=5)
entry1 = tk.Text(root, width=50, height=2)
entry1.pack(pady=5)

label2 = tk.Label(root, text="Text of article:")
label2.pack(pady=5)
entry2 = tk.Text(root, width=80, height=25)
entry2.pack(pady=5)

button = tk.Button(root, text="Check")
button.pack(pady=20)

root.mainloop()
