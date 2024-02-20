from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        try:
            if scvalue.get().isnumeric():
                value = int(scvalue.get())
            else:
                value = eval(scvalue.get())
            scvalue.set(value)
        except Exception as e:
            scvalue.set("Error")
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("400x550")
root.title("Hardik Calculator")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font=("Arial", 24), bd=5, relief=RIDGE)
screen.pack(fill=X, ipadx=10, ipady=10, padx=10)

f = Frame(root, bg="light grey")
button_texts = ["7", "8", "9", "+", "4", "5", "6", "-", "1", "2", "3", "*", "0", ".", "/", "%", "="]
for i in range(0, len(button_texts), 4):
    for text in button_texts[i:i+4]:
        b = Button(f, text=text, padx=20, pady=15, font=("Arial", 16), bd=3, relief=RAISED, bg="blue", fg="white") # Change button size
        b.pack(side=LEFT, padx=10, pady=6)
        b.bind("<Button-1>", click)
    f.pack()
    f = Frame(root, bg="light grey")

root.mainloop()
