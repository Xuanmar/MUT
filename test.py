import tkinter as tk  # 3.x
root = tk.Tk()
root.title("MUT (ww^r)")
root.resizable(0,0)
root.geometry("500x500")
strings = ['First', 'Second', 'Third', 'Last', 'Closing']
strit = iter(strings)
label = tk.Label(root, text=next(strit), width=(50), height=(25))
label.pack()

def refresh():
    try:
        label['text'] = next(strit)
        root.after(1000, refresh)
    except StopIteration:
        root.destroy()

root.after(1000, refresh)
root.mainloop()