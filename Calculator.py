from tkinter import *

main = Tk()
main.title("Calculator")
main['bg'] = 'grey'

def operation(number):
    global blank
    blank += str(number)
    text.set(blank)

def clear():
    global blank
    blank = ""
    text.set("")

def equal():
    global blank
    sum = str(eval(blank))
    text.set(sum)

blank = ""
text = StringVar()

Disp = Entry(main, bg = "grey", fg = "white" ,font = ("arial", 20), bd = 30, # Format
textvariable = text, insertwidth = 3 ,justify = "right") # Function
Disp.grid(columnspan = 4) # Location

num7 = Button(main, bg = "grey", fg = "white", font = ("arial", 20), padx = 26, pady = 20,
text = "7", command = lambda:operation(7))
num7.grid(row = 1, column = 0)

num8 = Button(main, bg = "grey", fg = "white", font=  ("arial", 20), padx = 28, pady= 20,
text = "8", command = lambda:operation(8))
num8.grid(row = 1, column = 1)

num9 = Button(main, bg = "grey", fg ="white", font = ("arial", 20), padx = 28, pady = 20,
text = "9", command = lambda:operation(9))
num9.grid(row = 1, column = 2)

add = Button(main, bg = "grey", fg = "white", font = ("arial", 20), padx = 26, pady = 20,
text = "+", command = lambda:operation("+"))
add.grid(row = 1, column = 3)

# New row

num4 = Button(main, bg = "grey", fg ="white", font = ("arial", 20), padx = 26, pady = 20,
text = "4", command = lambda:operation(4))
num4.grid(row = 2, column = 0)

num5 = Button(main, bg = "grey", fg = "white", font = ("arial", 20), padx = 28, pady = 20,
text = "5", command = lambda:operation(5))
num5.grid(row = 2, column = 1)

num6 = Button(main, bg = "grey", fg = "white", font = ("arial", 20), padx = 28, pady = 20,
text = "6", command = lambda:operation(6))
num6.grid(row = 2, column = 2)

sub = Button(main, bg = "grey", fg = "white", font = ("arial", 20), padx = 29, pady = 20,
text = "-", command = lambda:operation("-"))
sub.grid(row = 2, column = 3)

# New row

num1 = Button(main, bg= "grey", fg = "white", font = ("arial", 20), padx = 26, pady = 20,
text = "1", command = lambda:operation(1))
num1.grid(row = 3, column = 0)

num2 = Button(main, bg = "grey", fg = "white", font = ("arial", 20), padx = 28, pady = 20,
text = "2", command = lambda:operation(2))
num2.grid(row = 3, column = 1)

num3 = Button(main, bg = "grey", fg = "white", font = ("arial", 20), padx = 28, pady = 20,
text = "3", command = lambda:operation(3))
num3.grid(row = 3, column = 2)

mul = Button(main, bg = "grey", fg = "white", font = ("arial", 20), padx = 28, pady = 20,
text = "*", command = lambda:operation("*"))
mul.grid(row = 3, column = 3)

#New row

num0 = Button(main, bg ="grey", fg = "white", font = ("arial", 20), padx = 26, pady = 20,
text = "0", command = lambda:operation(0))
num0.grid(row = 4, column = 0)

C = Button(main, bg = "grey", fg = "white", font = ("arial", 20), padx = 26, pady = 20,
text = "C", command = clear)
C.grid(row = 4, column = 1)

equals = Button(main, bg = "grey", fg = "white", font = ("arial", 20), padx = 28, pady = 20,
text = "=", command = equal)
equals.grid(row = 4,column = 2)

div = Button(main, bg = "grey", fg = "white", font = ("arial", 20), padx = 30, pady = 20,
text = "/", command = lambda:operation("/"))
div.grid(row = 4 ,column = 3)


main.mainloop()