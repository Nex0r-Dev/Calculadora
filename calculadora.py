#!/usr/bin/env python3
"""
Calculadora - Una calculadora avanzada en Python
"""

import math
import tkinter as tk
from tkinter import messagebox

class CalculadoraPro:
    def __init__(self):
        self.historial = []

    def sumar(self, a, b):
        resultado = a + b
        self.historial.append(f"{a} + {b} = {resultado}")
        return resultado

    def restar(self, a, b):
        resultado = a - b
        self.historial.append(f"{a} - {b} = {resultado}")
        return resultado

    def multiplicar(self, a, b):
        resultado = a * b
        self.historial.append(f"{a} * {b} = {resultado}")
        return resultado

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        resultado = a / b
        self.historial.append(f"{a} / {b} = {resultado}")
        return resultado

    def potencia(self, base, exponente):
        resultado = base ** exponente
        self.historial.append(f"{base} ^ {exponente} = {resultado}")
        return resultado

    def raiz_cuadrada(self, numero):
        if numero < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
        resultado = math.sqrt(numero)
        self.historial.append(f"√{numero} = {resultado}")
        return resultado

    def seno(self, angulo_grados):
        angulo_radianes = math.radians(angulo_grados)
        resultado = math.sin(angulo_radianes)
        self.historial.append(f"sin({angulo_grados}°) = {resultado}")
        return resultado

    def coseno(self, angulo_grados):
        angulo_radianes = math.radians(angulo_grados)
        resultado = math.cos(angulo_radianes)
        self.historial.append(f"cos({angulo_grados}°) = {resultado}")
        return resultado

    def tangente(self, angulo_grados):
        angulo_radianes = math.radians(angulo_grados)
        resultado = math.tan(angulo_radianes)
        self.historial.append(f"tan({angulo_grados}°) = {resultado}")
        return resultado

    def mostrar_historial(self):
        if not self.historial:
            print("El historial está vacío")
        else:
            print("Historial de operaciones:")
            for operacion in self.historial:
                print(f"  {operacion}")

    def limpiar_historial(self):
        self.historial.clear()
        print("Historial limpiado")

class CalculadoraGUI:
    def __init__(self, root):
        self.calc = CalculadoraPro()
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry('450x550')
        self.root.configure(bg='#f0f0f0')
        self.root.resizable(False, False)
        
        # Title label
        title_label = tk.Label(root, text="Calculadora", font=('Arial', 18, 'bold'), bg='#f0f0f0', fg='#333')
        title_label.grid(row=0, column=0, columnspan=4, pady=(20,10))
        
        # Entry for input
        self.entry = tk.Entry(root, width=25, font=('Arial', 16), bg='white', fg='black', bd=2, relief='sunken', justify='right')
        self.entry.grid(row=1, column=0, columnspan=4, padx=20, pady=10)
        
        # Result label
        self.result_label = tk.Label(root, text="", font=('Arial', 14), bg='#f0f0f0', fg='#007acc')
        self.result_label.grid(row=2, column=0, columnspan=4, pady=(0,20))
        
        # Buttons
        button_config = {
            'numbers': {'bg': '#e1f5fe', 'fg': '#01579b', 'activebackground': '#b3e5fc'},
            'operators': {'bg': '#fff3e0', 'fg': '#e65100', 'activebackground': '#ffcc02'},
            'functions': {'bg': '#e8f5e8', 'fg': '#2e7d32', 'activebackground': '#c8e6c9'},
            'clear': {'bg': '#ffebee', 'fg': '#c62828', 'activebackground': '#ffcdd2'}
        }
        
        buttons = [
            ('7', 'numbers'), ('8', 'numbers'), ('9', 'numbers'), ('/', 'operators'),
            ('4', 'numbers'), ('5', 'numbers'), ('6', 'numbers'), ('*', 'operators'),
            ('1', 'numbers'), ('2', 'numbers'), ('3', 'numbers'), ('-', 'operators'),
            ('0', 'numbers'), ('.', 'numbers'), ('=', 'operators'), ('+', 'operators'),
            ('C', 'clear'), ('√', 'functions'), ('^', 'functions'), ('sin', 'functions'),
            ('cos', 'functions'), ('tan', 'functions'), ('Hist', 'functions'), ('Clear Hist', 'clear')
        ]
        
        row = 3
        col = 0
        for button_text, button_type in buttons:
            config = button_config[button_type]
            btn = tk.Button(root, text=button_text, width=6, height=2, font=('Arial', 12, 'bold'),
                            bg=config['bg'], fg=config['fg'], activebackground=config['activebackground'],
                            relief='raised', bd=3, command=lambda b=button_text: self.click(b))
            btn.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1
    
    def click(self, key):
        if key == '=':
            try:
                expression = self.entry.get()
                # Simple expression parsing
                if '+' in expression and expression.count('+') == 1:
                    a, b = map(float, expression.split('+'))
                    result = self.calc.sumar(a, b)
                elif '-' in expression and expression.count('-') == 1:
                    a, b = map(float, expression.split('-'))
                    result = self.calc.restar(a, b)
                elif '*' in expression and expression.count('*') == 1:
                    a, b = map(float, expression.split('*'))
                    result = self.calc.multiplicar(a, b)
                elif '/' in expression and expression.count('/') == 1:
                    a, b = map(float, expression.split('/'))
                    result = self.calc.dividir(a, b)
                elif '^' in expression and expression.count('^') == 1:
                    base, exp = map(float, expression.split('^'))
                    result = self.calc.potencia(base, exp)
                else:
                    result = float(expression)  # For single numbers
                self.result_label.config(text=f"Resultado: {result}")
                self.entry.delete(0, tk.END)
            except Exception as e:
                messagebox.showerror("Error", str(e))
        elif key == 'C':
            self.entry.delete(0, tk.END)
            self.result_label.config(text="")
        elif key == '√':
            try:
                num = float(self.entry.get())
                result = self.calc.raiz_cuadrada(num)
                self.result_label.config(text=f"Resultado: {result}")
                self.entry.delete(0, tk.END)
            except Exception as e:
                messagebox.showerror("Error", str(e))
        elif key == 'sin':
            try:
                ang = float(self.entry.get())
                result = self.calc.seno(ang)
                self.result_label.config(text=f"Resultado: {result}")
                self.entry.delete(0, tk.END)
            except Exception as e:
                messagebox.showerror("Error", str(e))
        elif key == 'cos':
            try:
                ang = float(self.entry.get())
                result = self.calc.coseno(ang)
                self.result_label.config(text=f"Resultado: {result}")
                self.entry.delete(0, tk.END)
            except Exception as e:
                messagebox.showerror("Error", str(e))
        elif key == 'tan':
            try:
                ang = float(self.entry.get())
                result = self.calc.tangente(ang)
                self.result_label.config(text=f"Resultado: {result}")
                self.entry.delete(0, tk.END)
            except Exception as e:
                messagebox.showerror("Error", str(e))
        elif key == 'Hist':
            hist = "\n".join(self.calc.historial)
            if hist:
                messagebox.showinfo("Historial", hist)
            else:
                messagebox.showinfo("Historial", "Vacío")
        elif key == 'Clear Hist':
            self.calc.limpiar_historial()
            messagebox.showinfo("Historial", "Limpiado")
        else:
            self.entry.insert(tk.END, key)

def main():
    root = tk.Tk()
    app = CalculadoraGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()