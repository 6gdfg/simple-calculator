import tkinter as tk
import math
 
class Calculate(tk.Frame):
    def __init__(self, parent):
        tk.Frame。__init__(self, parent)
        self.pack()
        
        self.startOfNextOperand = True  
 
        
        self.expr = tk.StringVar()  
        self.expr。set('')
        self.exprLabel = tk.标签(self, font = ('Helvetica', 10),
                                  fg = '#828282', width = 32, anchor='e', textvariable = self.expr)
        self.exprLabel。grid(row = 0, column = 0, columnspan = 4)
        self.result = tk.StringVar()    
        self.result。set(0)  
        self.resultLabel = tk.标签(self, font = ('Helvetica', 20),
                                    width = 16, anchor='e', textvariable=self.result)
        self.resultLabel。grid(row = 1, column = 0, columnspan = 4)
 
       
        buttons = [[ 'sin', 'cos', 'tan', 'cot'],
                   [  'C', '←', '/','√'],
                   ['7', '8', '9', '×'],
                   ['4', '5', '6', '-'],
                   ['1', '2', '3', '+'],
                   ['±', '0', '.', '=']]
 
     
        for r in range(6):
            for c in range(4):
               
                def cmd(key = buttons[r][c]):
                    self.click(密钥)
                b = tk.Button(self, text = buttons[r][c], width=8,command = cmd)
                b.grid(row = r+2, column = c)
                
    def click(self, key):
        if key == '=':   
            result = eval(self.expr。get() + self.result。get())
            self.result。set(result)
            self.expr。set('')
            self.startOfNextOperand = True
        elif 密钥 in '+-/×':
            if key == '×': key = '*'
            resultExpr = self.expr。get() + self.result。get() + key
            self.expr。set(resultExpr)
            self.result。set(0)
            self.startOfNextOperand = True
        elif key == 'C':  
            self.expr。set('')
            self.result。set(0)
        elif key == 'CE':  
            self.result。set(0)
        elif key == '←':
            oldnum = self.result。get()
            if len(oldnum) == 1:
                newnum = 0
            else:
                newnum = oldnum[:-1]
            self.result。set(newnum)
        elif key == '±': 
            oldnum = self.result。get() 
            if oldnum[0] == '-':
                newnum = oldnum[1:]
            else:
                newnum = '-' + oldnum
            self.result。set(newnum)
        elif 密钥 in ['sin', 'cos', 'tan', 'cot']:
             angle = math.radians(float(self.result。get()))
             result = 0
             if key == 'sin':
                result = math.sin(angle)
                self.result。set(result)
                self.startOfNextOperand = True
             elif key == 'cos':
                result = math.cos(angle)
                self.result。set(result)
                self.startOfNextOperand = True
             elif key == 'tan':
                result = math.tan(angle)
                self.result。set(result)
                self.startOfNextOperand = True
             elif key == 'cot':
                result = 1 / math.tan(angle)
                self.result。set(result)
                self.startOfNextOperand = True
        elif key == '√':
            result = math.sqrt(float(self.result。get()))
            self.result。set(result)
            self.startOfNextOperand = True
        else: 
            if self.startOfNextOperand:
                self.result。set(0)
                self.startOfNextOperand = False
            oldnum = self.result。get()  
            if oldnum == '0':
                self.result。set(密钥)
            else:
                newnum = oldnum + key
                self.result。set(newnum)
 
if __name__ == '__main__':
    root = tk.Tk()
    root.标题('simple calculator')
    root.geometry('400x250')
    calculate = Calculate(root)
    root.mainloop()
