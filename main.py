import tkinter as tki

root=tki.Tk()

root.title("Simple Calculator")

e=tki.Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=15,pady=15)

###------FUNCTIONS BEGIN------###

#button number 
def buttonClick(number):

    current=e.get()
    e.delete(0,tki.END)
    e.insert(0,str(current)+str(number))

#button addition
def buttonAdd():
    first_number=e.get()
    global f_num
    global math
    math="Addition"
    f_num=int(first_number)
    e.delete(0,tki.END)

#button multiplication
def buttonMultiply():
    first_number=e.get()
    global f_num
    global math
    math="Multiply"
    f_num=int(first_number)
    e.delete(0,tki.END)

#button divide
def buttonDivide():
    first_number=e.get()
    global f_num
    global math
    math="Divide"
    f_num=int(first_number)
    e.delete(0,tki.END)

#button substract
def buttonSubtract():
    first_number=e.get()
    global f_num
    global math
    math="Substract"
    f_num=int(first_number)
    e.delete(0,tki.END)

#button equal
def buttonEqual():
    second_number=e.get()
    e.delete(0,tki.END)

    if math=="Addition":
        e.insert(0,f_num+int(second_number))
    if math=="Multiply":
        e.insert(0,f_num*int(second_number))
    if math=="Divide":
        e.insert(0,f_num/int(second_number))
    if math=="Substract":
        e.insert(0,f_num-int(second_number))
    

def buttonClear():
    e.delete(0,tki.END)

###------FUNCTION END-------###

#define buttons and put on screen
button_1=tki.Button(root,text="1",padx=40,pady=20,command=lambda : buttonClick(1))
button_1.grid(row=1,column=0)

button_2=tki.Button(root,text="2",padx=40,pady=20,command=lambda : buttonClick(2))
button_2.grid(row=1,column=1)

button_3=tki.Button(root,text="3",padx=40,pady=20,command=lambda : buttonClick(3))
button_3.grid(row=1,column=2)

button_4=tki.Button(root,text="4",padx=40,pady=20,command=lambda : buttonClick(4))
button_4.grid(row=2,column=0)

button_5=tki.Button(root,text="5",padx=40,pady=20,command=lambda : buttonClick(5))
button_5.grid(row=2,column=1)

button_6=tki.Button(root,text="6",padx=40,pady=20,command=lambda : buttonClick(6))
button_6.grid(row=2,column=2)

button_7=tki.Button(root,text="7",padx=40,pady=20,command=lambda : buttonClick(7))
button_7.grid(row=3,column=0)

button_8=tki.Button(root,text="8",padx=40,pady=20,command=lambda : buttonClick(8))
button_8.grid(row=3,column=1)

button_9=tki.Button(root,text="9",padx=40,pady=20,command=lambda : buttonClick(9))
button_9.grid(row=3,column=2)

button_0=tki.Button(root,text="0",padx=40,pady=20,command=lambda : buttonClick(0))
button_0.grid(row=4,column=0)

button_add=tki.Button(root,text="+",padx=39,pady=20,command=lambda : buttonAdd())
button_add.grid(row=5,column=0)

button_add=tki.Button(root,text="-",padx=40,pady=20,command=lambda : buttonSubtract())
button_add.grid(row=6,column=0)

button_add=tki.Button(root,text="*",padx=41,pady=20,command=lambda : buttonMultiply())
button_add.grid(row=6,column=1)

button_add=tki.Button(root,text="/",padx=41,pady=20,command=lambda : buttonDivide())
button_add.grid(row=6,column=2)

button_equal=tki.Button(root,text="=",padx=89,pady=20,command=lambda : buttonEqual())
button_equal.grid(row=5,column=1,columnspan=2)

button_clear=tki.Button(root,text="Clear",padx=79,pady=20,command=lambda : buttonClear())
button_clear.grid(row=4,column=1,columnspan=2)


root.mainloop()