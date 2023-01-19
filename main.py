from tkinter import  *

class Calculator:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.window = Tk()
        self.calcu = StringVar()
        self.numero = StringVar()
        self.string = ""
        self.historico = ""
        self.window.title("Calculator")
        self.window.configure(bg='#1C1C1C', background='#1C1C1C')
        self.canva = Canvas(self.window, width = self.width, height = self.height, bg='#1C1C1C', background='#1C1C1C')
        self.canva.grid(columns = 3, rows = 6)
        self.canva.configure(bg='#1C1C1C', background='#1C1C1C')

        self.create_widgets()
        self.canva.pack()

        #variables count

    def create_widgets(self):
        
        #Number Buttons
        self.button0 = Button(self.canva, text= '0', height = 2, command = lambda:self.draw_number('0'), bg = '#505050', fg='white', borderwidth=0, font=("Helvetica",12), highlightthickness=0)
        self.button0.grid(column = 0, row = 6, columnspan = 2, sticky='EW')
        #self.button0.pack()

        self.button1 = Button(self.canva, text= '1', height = 2, command = lambda:self.draw_number('1'), bg = '#505050', fg='white', borderwidth=0, font=("Helvetica",12), highlightthickness=0)
        self.button1.grid(column = 0, row = 5, sticky='EW')

        self.button2 = Button(self.canva, text= '2', height = 2, command = lambda:self.draw_number('2'), bg = '#505050', fg='white', borderwidth=0, font=("Helvetica",12), highlightthickness=0)
        self.button2.grid(column = 1, row = 5, sticky='EW')

        self.button3 = Button(self.canva, text= '3', height = 2, command = lambda:self.draw_number('3'), bg = '#505050', fg='white', borderwidth=0, font=("Helvetica",12), highlightthickness=0)
        self.button3.grid(column = 2, row = 5, sticky='EW')

        self.button4 = Button(self.canva, text= '4', height = 2, command = lambda:self.draw_number('4'), bg = '#505050', fg='white', borderwidth=0, font=("Helvetica",12), highlightthickness=0)
        self.button4.grid(column = 0, row = 4, sticky='EW')

        self.button5 = Button(self.canva, text= '5', height = 2, command = lambda:self.draw_number('5'), bg = '#505050', fg='white', borderwidth=0, font=("Helvetica",12), highlightthickness=0)
        self.button5.grid(column = 1, row = 4, sticky='EW')

        self.button6 = Button(self.canva, text= '6', height = 2, command = lambda:self.draw_number('6'), bg = '#505050', fg='white', borderwidth=0, font=("Helvetica",12), highlightthickness=0)
        self.button6.grid(column = 2, row = 4, sticky='EW')

        self.button7 = Button(self.canva, text= '7', height = 2, command = lambda:self.draw_number('7'), bg = '#505050', fg='white', borderwidth=0, font=("Helvetica",12), highlightthickness=0)
        self.button7.grid(column = 0, row = 3, sticky='EW')

        self.button8 = Button(self.canva, text= '8', height = 2, command = lambda:self.draw_number('8'), bg = '#505050', fg='white', borderwidth=0, font=("Helvetica",12), highlightthickness=0)
        self.button8.grid(column = 1, row = 3, sticky='EW')

        self.button9 = Button(self.canva, text= '9', height = 2, command = lambda:self.draw_number('9'), bg = '#505050', fg='white', borderwidth=0, font=("Helvetica",12), highlightthickness=0)
        self.button9.grid(column = 2, row = 3, sticky='EW')

        #Functions Buttons
        self.buttonAdd = Button(self.canva, text= '+', height = 2, command = lambda:self.draw_number(' + '), bg = '#FF9500', fg='white', borderwidth=0, font=("Helvetica",12), highlightthickness=0)
        self.buttonAdd.grid(column = 3, row = 5, sticky='EW')

        self.buttonSub = Button(self.canva, text= '-', height = 2, command = lambda:self.draw_number(' - '), bg = '#FF9500', fg='white', borderwidth=0, font=("Helvetica",12), highlightthickness=0)
        self.buttonSub.grid(column = 3, row = 4, sticky='EW')

        self.buttonMult = Button(self.canva, text= 'X', height = 2, command = lambda:self.draw_number(' x '), bg = '#FF9500', fg='white', borderwidth=0, font=("Helvetica",12), highlightthickness=0)
        self.buttonMult.grid(column = 3, row = 3, sticky='EW')

        self.buttonDiv = Button(self.canva, text= '/', height = 2, command = lambda:self.draw_number(' / '), bg = '#FF9500', fg='white', borderwidth=0, font=("Helvetica",12), highlightthickness=0)
        self.buttonDiv.grid(column = 3, row = 2, sticky='EW')

        self.buttonDot = Button(self.canva, text= '.', height = 2, command = lambda:self.draw_number('.'), bg = '#505050', fg='white', borderwidth=0, font=("Helvetica",12), highlightthickness=0)
        self.buttonDot.grid(column = 2, row = 6, sticky='EW')

        self.buttonEqual = Button(self.canva, text= '=', height = 2, command = self.calculus, bg = '#FF9500', fg='white', borderwidth=0, font=("Helvetica",12), highlightthickness=0)
        self.buttonEqual.grid(column = 3, row = 6, sticky='EW')

        self.buttonAc = Button(self.canva, text= 'Ac', height = 2, command = self.clear, bg = '#D4D4D2', borderwidth=0, font=("Helvetica",12), highlightthickness=0)
        self.buttonAc.grid(column = 0, row = 2, sticky='EW')

        self.buttonAbs = Button(self.canva, text= '+/-', height = 2, bg = '#D4D4D2', borderwidth=0, font=("Helvetica",12), highlightthickness=0)
        self.buttonAbs.grid(column = 1, row = 2, sticky='EW')

        self.buttonPerct = Button(self.canva, text= '%', height = 2, bg = '#D4D4D2', borderwidth=0, font=("Helvetica",12), highlightthickness=0)
        self.buttonPerct.grid(column = 2, row = 2, sticky='EW')

        
        
        #Visor
        self.text_area = Label(self.canva, anchor='sw', textvariable = self.numero, font=("Helvetica",12), bg ='#1C1C1C', fg='white', borderwidth=0)
        self.text_area.config(width = 30)
        self.text_area.grid(columnspan = 4, row = 1)

        self.calculus_area = Text(self.canva, font=("Helvetica",12), state=DISABLED, fg='white', bg ='#1C1C1C', borderwidth=0, highlightthickness=0)
        self.calculus_area.config(width = 30, height = 10)
        self.calculus_area.grid(columnspan = 4, row = 0)

        
    def draw_number(self, num):

        self.string = self.string + num
        self.numero.set(self.string)

    def calculus(self):
        teste = self.string.split()
        if(len(teste) >= 3):

            resultado = float(teste[0])
            for x in range(1, len(teste)):
                if teste[x] == '+':
                    resultado += float(teste[x + 1])

                elif teste[x] == '-':
                    resultado -= float(teste[x + 1])
                
                elif teste[x] == 'x':
                    resultado *= float(teste[x + 1])
 
                elif teste[x] == '/':
                    resultado /= float(teste[x + 1])

            if type(resultado) == int:
                resultado = int(resultado)

        self.calculus_area.configure(state=NORMAL)
        form = f"{self.string} = {str(resultado)}" + '\n'
        self.calculus_area.insert(END, form)
        self.calculus_area.configure(state=DISABLED)

        self.string = str(resultado)
        self.numero.set(str(resultado))
        


    def clear(self):
        self.string = ""
        self.numero.set(" ")

    def start(self):
        self.window.mainloop()

if __name__ == '__main__':
    interface = Calculator(768, 1024).start()
