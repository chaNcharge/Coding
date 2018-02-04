import tkinter as tk
import tkinter.ttk as ttk
from tkinter import scrolledtext, messagebox
 
window = tk.Tk() 
window.title("chaNcharge's app")
window.geometry('750x550')

lbl = tk.Label(window, text="You suck!")
lbl.grid(column=1, row=0)

txt = tk.Entry(window, width=10)
txt.grid(column=2, row=0)
txt.focus()

combo = ttk.Combobox(window)
combo['values']= ("", 1, 2, 3, 4, 5, "many")
combo.current(0)
combo.grid(column=0, row=0)

chk_state = tk.BooleanVar()
chk_state.set(False)
chk = ttk.Checkbutton(window, text="Chosen?", var=chk_state)
chk.grid(column=0, row=1)

scrltxt = scrolledtext.ScrolledText(window, width=40, height=10)
scrltxt.grid(column=0, row=3)

spinvar = tk.IntVar()
spinvar.set(36)
spin = tk.Spinbox(window, from_=0, to=100, width=5, textvariable=spinvar)
spin.grid(column=0, row=4)

barlbl = tk.Label(window, text="Saltiness level:")
barlbl.grid(column=0, row=5)
bar = ttk.Progressbar(window, length=200)
bar.grid(column=1, row=5)

def clicked():
    newtext = "I am " + str(combo.get()) + " " + txt.get()
    lbl.configure(text=newtext)
    scrltxt.insert(tk.INSERT, "just kidding \n")
    bar['value'] += 10
    if bar['value'] >= 100:
        scrltxt.insert(tk.INSERT, "Reached maximum saltiness. \n")
    messagebox.showinfo("Extremely important information!", "You're useless.")
def rad2clicked():
    newtext = "You are " + str(combo.get()) + " " + txt.get()
    lbl.configure(text=newtext)
def rad3clicked():
    newtext = "We are " + str(combo.get()) + " " + txt.get()
    lbl.configure(text=newtext)
def askclicked():
    res1 = messagebox.askquestion("Question 1", "Are you stupid?")
    res2 = messagebox.askokcancel("Question 2", "Click ok if your body is Reggie.")
    if res1 == "yes":
        scrltxt.insert(tk.INSERT, "They are stupid \n")
    else:
        scrltxt.insert(tk.INSERT, "They are lying \n")
    if res2 == True:
        scrltxt.insert(tk.INSERT, "MY BODY IS REGGIE! \n")
    else:
        scrltxt.insert(tk.INSERT, "Y U NO REGGIE \n")
def close():
    window.destroy()

radstate = tk.IntVar()
radstate.set(0)
rad1 = tk.Radiobutton(window, text="Default", value=1, var=radstate, command=clicked)
rad2 = tk.Radiobutton(window, text="You are", value=2, var=radstate, command=rad2clicked)
rad3 = tk.Radiobutton(window, text="We are", value=3, var=radstate, command=rad3clicked)
rad1.grid(column=0, row=2)
rad2.grid(column=1, row=2)
rad3.grid(column=2, row=2)

btn = tk.Button(window, text="Make Sentence", command=clicked)
btn.grid(column=3, row=0)
closebtn = tk.Button(window, text="Close", command=close)
closebtn.grid(column=1, row=1)
askbtn = tk.Button(window, text="Ask", command=askclicked)
askbtn.grid(column=1, row=4)

window.mainloop()