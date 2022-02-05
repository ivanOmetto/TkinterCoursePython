from tkinter import *

root = Tk()
root.title("Simple Calculator")
buttons = []

def callback():
    global buttonClicked
    print(buttonClicked)


for i in range(10):
    new_button = Button(root, text=9 - i, padx=10, pady=10, width=15, command=callback)
    buttons.append(new_button)

    buttonClicked = i

    if i % 2:
        buttons[i].grid(row=1 + i, column=1)
    else:
        buttons[i].grid(row=2 + i, column=0)



equalButton = Button(root, text="=", padx=10, pady=10, width=15)
equalButton.grid(row=0, column=1, padx=5, pady=5)

plusButton = Button(root, text="+", padx=10, pady=10, width=15)
plusButton.grid(row=12, column=0, padx=5, pady=5)

clearButton = Button(root, text="clear", padx=10, pady=10, width=15)
clearButton.grid(row=12, column=1, padx=5, pady=5)

e = Entry(root, width=15, borderwidth=3)
e.grid(row=0, column=0, padx=5, pady=5)

root.mainloop()
