from tkinter import *
from tkinter.font import *


class PyCalci:

    def __init__(self):
        self.root = Tk()
        self.currentext = None
        self.result = None
        self.entryframe = Frame(self.root, bd='10')
        self.entryframe.pack()
        self.expressiontext = StringVar()
        self.fontt = Font(family='Consolas', size='10', weight='bold')
        self.expression = Entry(self.entryframe, width='35', bg='yellow', fg='blue', font=self.fontt, textvariable=self.expressiontext)
        self.expression.pack(side=BOTTOM)
        self.btnframe = Frame(self.root, bd='5')
        self.btnframe.pack()
        self.btn1 = Button(self.btnframe, text='1', width='10', bg='green', fg='white', command=lambda : self.btnpressed('1'))
        self.btn2 = Button(self.btnframe, text='2', width='10', bg='green', fg='white', command=lambda : self.btnpressed('2'))
        self.btn3 = Button(self.btnframe, text='3', width='10', bg='green', fg='white', command=lambda : self.btnpressed('3'))
        self.btn4 = Button(self.btnframe, text='4', width='10', bg='green', fg='white', command=lambda : self.btnpressed('4'))
        self.btn5 = Button(self.btnframe, text='5', width='10', bg='green', fg='white', command=lambda : self.btnpressed('5'))
        self.btn6 = Button(self.btnframe, text='6', width='10', bg='green', fg='white', command=lambda : self.btnpressed('6'))
        self.btn7 = Button(self.btnframe, text='7', width='10', bg='green', fg='white', command=lambda : self.btnpressed('7'))
        self.btn8 = Button(self.btnframe, text='8', width='10', bg='green', fg='white', command=lambda : self.btnpressed('8'))
        self.btn9 = Button(self.btnframe, text='9', width='10', bg='green', fg='white', command=lambda : self.btnpressed('9'))
        self.btn0 = Button(self.btnframe, text='0', width='10', bg='green', fg='white', command=lambda : self.btnpressed('0'))
        self.btnadd = Button(self.btnframe, text='+', width='10', bg='blue', fg='white', command=lambda : self.btnpressed('+'))
        self.btnsub = Button(self.btnframe, text='-', width='10', bg='blue', fg='white', command=lambda : self.btnpressed('-'))
        self.btnmul = Button(self.btnframe, text='*', width='10', bg='blue', fg='white', command=lambda : self.btnpressed('*'))
        self.btndiv = Button(self.btnframe, text='/', width='10', bg='blue', fg='white', command=lambda : self.btnpressed('/'))
        self.btneq = Button(self.btnframe, text='=', width='10', bg='blue', fg='white', command=lambda : self.btnpressed('='))
        self.btndel = Button(self.btnframe, text='DEL', width='10', bg='red', fg='white', command=lambda : self.btnpressed('del'))
        self.btn1.grid(row=0, column=0)
        self.btn2.grid(row=0, column=1)
        self.btn3.grid(row=0, column=2)
        self.btn4.grid(row=1, column=0)
        self.btn5.grid(row=1, column=1)
        self.btn6.grid(row=1, column=2)
        self.btn7.grid(row=2, column=0)
        self.btn8.grid(row=2, column=1)
        self.btn9.grid(row=2, column=2)
        self.btn0.grid(row=3, column=1)
        self.btneq.grid(row=3, column=0)
        self.btndel.grid(row=3, column=2)
        self.btnadd.grid(row=0, column=3)
        self.btnsub.grid(row=1, column=3)
        self.btnmul.grid(row=2, column=3)
        self.btndiv.grid(row=3, column=3)
        self.root.mainloop()

    def btnpressed(self, keyid):
        if keyid != '=' and keyid != 'del':
            self.display(keyid)
        elif keyid == '=':
            try:
                self.result = eval(self.expressiontext.get())
                self.expressiontext.set(self.result)
            except (SyntaxError, NameError, TypeError, ZeroDivisionError):
                self.expressiontext.set("ERROR")
        elif keyid == 'del':
            self.currentext = self.expressiontext.get()[:len(self.expressiontext.get())-1]
            self.expressiontext.set(self.currentext)


    def display(self, keyid):
        self.currentext = self.expressiontext.get() + keyid
        self.expressiontext.set(self.currentext)

#use lambda in command



instancePyCalci = PyCalci()
