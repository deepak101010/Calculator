from tkinter import *
import mysql.connector
from tkinter.messagebox import *
import math as m
 
# some usefull variable
font = ('Verdana', 22, 'bold')

# important functions
def clear():
    ex = textFeild.get()
    ex = ex[0:len(ex) - 1]
    textFeild.delete(0, END)
    textFeild.insert(0, ex)

def all_clear():
    textFeild.delete(0, END)

def click_btn_function(event):
    print("btn clicked")
    b = event.widget
    text = b['text']
    print(text)
    print(database.get())

    if text == 'x':
        textFeild.insert(END, "*")
        return
    if text == '=':
        try:
            ex = textFeild.get()
            anser = eval(ex)
            textFeild.delete(0, END)
            textFeild.insert(0, anser)
            a=textFeild.get()
            mydb=mysql.connector.connect(host="localhost", user="root", password="", database="calcidb")
            mycursor = mydb.cursor()
            insert = ("INSERT INTO total (total) VALUES  (%s)")
            values = [textFeild.get()]
            mycursor.execute(insert,values)
            mydb.commit()
            print(a)
        except Exception as e:
            print("Error..", e)
            showerror("Error", e)
        return
    textFeild.insert(END, text)

# creating a win
win = Tk()
win.title('my calculator')
win.geometry('480x420')

# heading label
heading = Label(win, text='MY CALCULATOR', font=font)
heading.pack(side=TOP)

def database():
    print(database.get())

# textfeild
textFeild = Entry(win, textvariable=database ,font=font, justify=CENTER)
textFeild.pack(side=TOP, pady=10, fill=X, padx=10)
database=StringVar()

# buttons
buttonFrame = Frame(win)
buttonFrame.pack(side=TOP, padx=10)

# adding button
temp = 1
for i in range(0, 3):
    for j in range(0, 3):
        btn = Button(buttonFrame, text=str(temp), font=font, width=5, relief='ridge', activebackground='Blue',
                     activeforeground='white')
        btn.grid(row=i, column=j)
        temp = temp + 1
        btn.bind('<Button-1>', click_btn_function)

zeroBtn = Button(buttonFrame, text='0', font=font, width=5, relief='ridge', activebackground='Blue',
                 activeforeground='white')
zeroBtn.grid(row=3, column=0)

dotBtn = Button(buttonFrame, text='.', font=font, width=5, relief='ridge', activebackground='Blue',
                activeforeground='white')
dotBtn.grid(row=3, column=1)

equalBtn = Button(buttonFrame, text='=', command=database ,font = font, width = 5, relief = 'ridge',
                activebackground = 'Blue', activeforeground = 'white')
equalBtn.grid(row=3, column=2)

plusBtn = Button(buttonFrame, text='+', font=font, width=5, relief='ridge', activebackground='Blue',
                 activeforeground='white')
plusBtn.grid(row=0, column=3)

minusBtn = Button(buttonFrame, text='-', font=font, width=5, relief='ridge', activebackground='Blue',
                  activeforeground='white')
minusBtn.grid(row=1, column=3)

multBtn = Button(buttonFrame, text='x', font=font, width=5, relief='ridge', activebackground='Blue',
                 activeforeground='white')
multBtn.grid(row=2, column=3)

divideBtn = Button(buttonFrame, text='/', font=font, width=5, relief='ridge', activebackground='Blue',
                   activeforeground='white')
divideBtn.grid(row=3, column=3)

clearBtn = Button(buttonFrame, text='<--', font=font, width=11, relief='ridge', activebackground='Blue',
                  activeforeground='white', command=clear)
clearBtn.grid(row=4, column=0, columnspan=2)

allClearBtn = Button(buttonFrame, text='AC', font=font, width=11, relief='ridge', activebackground='Blue',
                     activeforeground='white', command=all_clear)
allClearBtn.grid(row=4, column=2, columnspan=2)

# binding all btns
plusBtn.bind('<Button-1>', click_btn_function)
minusBtn.bind('<Button-1>', click_btn_function)
multBtn.bind('<Button-1>', click_btn_function)
divideBtn.bind('<Button-1>', click_btn_function)
zeroBtn.bind('<Button-1>', click_btn_function)
dotBtn.bind('<Button-1>', click_btn_function)
equalBtn.bind('<Button-1>', click_btn_function)

###########################################################################
# functions
scFrame = Frame(win)

sqrtBtn = Button(scFrame, text='√', font=font, width=5, relief='ridge', activebackground='orange',
                 activeforeground='white')
sqrtBtn.grid(row=0, column=0)

powBtn = Button(scFrame, text='^', font=font, width=5, relief='ridge', activebackground='orange',
                activeforeground='white')
powBtn.grid(row=0, column=1)

facBtn = Button(scFrame, text='x!', font=font, width=5, relief='ridge', activebackground='orange',
                activeforeground='white')
facBtn.grid(row=0, column=2)

radBtn = Button(scFrame, text='toRad', font=font, width=5, relief='ridge', activebackground='orange',
                activeforeground='white')
radBtn.grid(row=0, column=3)

degBtn = Button(scFrame, text='toDeg', font=font, width=5, relief='ridge', activebackground='orange',
                activeforeground='white')
degBtn.grid(row=1, column=0)

sinBtn = Button(scFrame, text='sinθ', font=font, width=5, relief='ridge', activebackground='orange',
                activeforeground='white')
sinBtn.grid(row=1, column=1)

cosBtn = Button(scFrame, text='cosθ', font=font, width=5, relief='ridge', activebackground='orange',
                activeforeground='white')
cosBtn.grid(row=1, column=2)

tanBtn = Button(scFrame, text='tanθ', font=font, width=5, relief='ridge', activebackground='orange',
                activeforeground='white')
tanBtn.grid(row=1, column=3)

normalcal = True


def calculate_sc(event):
    print('btn..')
    btn = event.widget
    text = btn['text']
    print(text)
    ex = textFeild.get()
    answer = ''
    if text == 'toDeg':
        print("cal degree")
        answer = str(m.degrees(float(ex)))
    elif text == '√':
        print("sqrt")
        answer = str(m.sqrt(float(ex)))
    elif text == '^':
        print("power")
        answer = str(m.power(float(ex)))
    elif text == 'toRad':
        print("radian")
        answer = str(m.radians(float(ex)))
    elif text == 'x!':
        print("cal factorial")
        answer = str(m.factorial(int(ex)))
    elif text == 'sinθ':
        print("cal sin")
        answer = str(m.sin(m.radians(int(ex))))
    elif text == 'cosθ':
        print("cal cos")
        answer = str(m.cos(m.radians(int(ex))))
    elif text == 'tanθ':
        print("cal tan")
        answer = str(m.tan(m.radians(int(ex))))
    textFeild.delete(0, END)
    textFeild.insert(0, answer)
def sc_click():
    global normalcal
    if normalcal:
        # sc
        buttonFrame.pack_forget()
        # add sc frame
        scFrame.pack(side=TOP, pady=20)
        buttonFrame.pack(side=TOP)
        win.geometry("510x600")

        print('show sc')
        normalcal = False
    else:
        print('show normal')
        scFrame.pack_forget()
        win.geometry("510x450")
        normalcal = True

# binding sc buttons
sqrtBtn.bind("<Button-1>", calculate_sc)
powBtn.bind("<Button-1>", calculate_sc)
facBtn.bind("<Button-1>", calculate_sc)
radBtn.bind("<Button-1>", calculate_sc)
degBtn.bind("<Button-1>", calculate_sc)
sinBtn.bind("<Button-1>", calculate_sc)
cosBtn.bind("<Button-1>", calculate_sc)
tanBtn.bind("<Button-1>", calculate_sc)

fontmenu = ('', 15)
menubar = Menu(win)

mode = Menu(menubar, font=fontmenu, tearoff=0)
mode.add_checkbutton(label='Scientific Calculator', command=sc_click)

menubar.add_cascade(label='Mode', menu=mode)
win.config(menu=menubar)
win.mainloop()
