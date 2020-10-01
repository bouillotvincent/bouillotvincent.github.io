from tkinter import *
from exercice5_7_corrige import bin2dec, dec2bin

class calculatrice(Tk):
    _listOp = ['+', '-', '*']

    def __init__(self, width = 500, height = 500):
        Tk.__init__(self)        # constructeur de la classe parente
        self.can = Canvas(self, width = width, height = height, bg ="white")
        self.can.update()
        self.title('Calculette')
        self.tex1 = Label(self, text = '', relief='sunken')
        self.tex1.grid(row = 0, column=0, columnspan=3, sticky='EW')
        self.tex2 = Label(self, text = '', relief='sunken', background='grey')
        self.tex2.grid(row = 0, column=4, columnspan=3, sticky='EW')

        self.but = [Button(self, text = str(i), command = lambda x=i: self._maj(str(x)) ) for i in range(10)]
        self.but.insert(0, Button(self, text = 'b', command = lambda x=1: self._maj('b') ))
        self.but.append(Button(self, text = '='))
        for i in range(11):
            self.but[i].grid(row = i//3+1, column=i%3)
        self.but.append(Button(self, text = 'CE', command = lambda x=1: self._maj(-1)))
        self.but[12].grid(row = 5, column=0, columnspan=3, sticky='EW')

        for i in range(len(self._listOp)):
            self.but.append(Button(self, text = self._listOp[i]))
            self.but[13+i].grid(row = 1, column=4+i, sticky='EW')
            
        self.b2d = Button(self, text = 'Base 2 vers Base 10', command = lambda x=1: self._resultat(self.tex1.cget("text"), bin2dec))
        self.d2b = Button(self, text = 'Base 10 vers Base 2', command = lambda x=1: self._resultat(self.tex1.cget("text"), dec2bin))
        self.b2d.grid(row = 2, column = 4, columnspan=3)
        self.d2b.grid(row = 3, column = 4, columnspan=3)

    def _maj(self, buttonText):
        if buttonText == -1:
            self.tex1.configure(text='')
            self.tex2.configure(text='')
        else:
            text = self.tex1.cget("text") + buttonText
            self.tex1.configure(text=text)

    def _resultat(self, text, f):
        print(text)
        self.tex2.configure(text = str(f(text)))


if __name__ == "__main__":
    calculatrice().mainloop()