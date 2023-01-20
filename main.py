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
        self.create_number_buttons()
        self.create_functions_buttons()
        self.create_visor()
        self.canva.pack()

    def create_buttom(self, column, row, simbol, color, font_color, func) -> None:
        button = Button(self.canva, text= f'{simbol}', height = 2, command = func, bg = color, fg=font_color, borderwidth=0, font=("Helvetica",12), highlightthickness=0)
        button.grid(column = column, row = row, sticky='EW')

        if simbol == '0':
            button.grid(columnspan=2, column=column - 1)

    def create_number_buttons(self):
        # sourcery skip: convert-to-enumerate, use-itertools-product

        keyboard = ['9', '8', '7',
                    '6', '5', '4',
                    '3', '2', '1',
                    '.','0']

        button_number = -1
        for row in range(3, 7):
            for column in range(2, -1, -1):
                button_number += 1
                if button_number <= 10:
                    self.create_buttom(column, row, keyboard[button_number], '#505050', 'white', lambda x = keyboard[button_number]:self.draw_number(f'{x}'))
                else:   
                    break

    def create_functions_buttons(self):
       
        keyboard = [' x ' , ' / ', ' - ', ' + ', '=', '%', '+/-', 'Ac']
        colors = '#FF9500'
        row = 2
        colum = 3
        for func in range(len(keyboard)):
            if keyboard[func] == '%':
                colors = '#D4D4D2'
                colum = 2
                row = 2

            if keyboard[func] == '%':
                self.create_buttom(colum, row, keyboard[func], colors, 'black', self.calculus)
                colum -=1

            elif keyboard[func] == '+/-':
                self.create_buttom(colum, row, keyboard[func], colors, 'black', self.calculus)
                colum -=1

            elif keyboard[func] == 'Ac':
                self.create_buttom(colum, row, keyboard[func], colors, 'black', self.clear)
                colum -=1

            elif keyboard[func] == '=':
                self.create_buttom(colum, row, keyboard[func], colors, 'white', self.calculus)
                colum -=1
            else:
                self.create_buttom(colum, row, keyboard[func], colors, 'white', lambda x = keyboard[func]:self.draw_number(f'{x}'))
                row += 1

    def create_visor(self):

        #Visor
        self.text_area = Label(self.canva, anchor='sw', textvariable = self.numero, font=("Helvetica",12), bg ='#1C1C1C', fg='white', borderwidth=0)
        self.text_area.config(width = 30)
        self.text_area.grid(columnspan = 4, row = 1)

        self.calculus_area = Text(self.canva, font=("Helvetica",12), state=DISABLED, fg='white', bg ='#1C1C1C', borderwidth=0, highlightthickness=0)
        self.calculus_area.config(width = 30, height = 10)
        self.calculus_area.grid(columnspan = 4, row = 0)
        self.window.bind('<Return>', self.calculus)
        self.window.bind('<BackSpace>', self.clear_char)

        
    def draw_number(self, num):

        self.string = self.string + num
        self.numero.set(self.string)

    def calculus(self, event = None):
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

    def clear_char(self, event = None):
        self.string = self.string[:-1]
        self.numero.set(self.string)

    def start(self):
        self.window.mainloop()

if __name__ == '__main__':
    interface = Calculator(768, 1024).start()
