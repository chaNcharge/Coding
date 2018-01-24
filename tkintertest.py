import tkinter as ttk
 
window = ttk.Tk() 
window.title("chaNcharge's app")
window.geometry('350x200')

lbl = ttk.Label(window, text="Hello there!")
lbl.grid(column=0, row=0)

txt = ttk.Entry(window, width=10)
txt.grid(column=1, row=0)
txt.focus()
# Left off at 5. Add a combobox widget

def clicked():
    res = "I am " + txt.get()
    lbl.configure(text= res)

btn = ttk.Button(window, text="Click Me", command=clicked)
btn.grid(column=2, row=0)
 
window.mainloop()