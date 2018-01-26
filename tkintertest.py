import tkinter as tk
import tkinter.ttk as ttk
 
window = tk.Tk() 
window.title("chaNcharge's app")
window.geometry('500x300')

lbl = tk.Label(window, text="You suck!")
lbl.grid(column=1, row=0)

txt = tk.Entry(window, width=10)
txt.grid(column=2, row=0)
txt.focus()

combo = ttk.Combobox(window)
combo['values']= (1, 2, 3, 4, 5, "many")
combo.current(0)
combo.grid(column=0, row=0)

chk_state = tk.BooleanVar()
chk_state.set(False)
chk = ttk.Checkbutton(window, text="Chosen?", var=chk_state)
chk.grid(column=0, row=1)
# Left off at 7 Add radio buttons widgets

def clicked():
    res = "I am " + str(combo.get()) + " " + txt.get()
    lbl.configure(text= res)
def close():
    window.destroy()

btn = tk.Button(window, text="Click Me", command=clicked)
btn.grid(column=3, row=0)
closebtn = tk.Button(window, text="Close", command=close)
closebtn.grid(column=1, row=1)
 
window.mainloop()