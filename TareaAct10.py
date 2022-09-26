
import tkinter as tk
from tkinter import messagebox
"""Se creo una función en la cual abarcariamos todos los datos de nuestra aplicación"""
class Progra1:
    def __init__(self):
        self.ventana1=tk.Tk()
        #Establecimos el tamaño de la ventana
        self.ventana1.geometry("325x150")
        #Se inserto un label de bienvenida
        self.label3=tk.Label(self.ventana1,text="¡Cajero automatico!")
        #Procedemos a agregar los labels los cuales nos ayudaran a dar información al usuario
        self.label1=tk.Label(self.ventana1,text="Ingrese el precio del producto:")
        
        self.dato1=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1, width=20, textvariable=self.dato1)
        
        self.label2=tk.Label(self.ventana1,text="Ingrese la cantidad de productos:")
        
        self.dato2=tk.StringVar()
        self.entry2=tk.Entry(self.ventana1, width=20, textvariable=self.dato2)
        
        self.seleccion=tk.IntVar()
        #Creamos las opción de nuestros radiobuttons, les asignamos el valor que contrendran
        self.radio1=tk.Radiobutton(self.ventana1,text="Pagar con efectivo", variable=self.seleccion, value=1)
        self.radio2=tk.Radiobutton(self.ventana1,text="Pagar con tarjeta", variable=self.seleccion, value=2)

        #Se estableció un boton que imprimiría el recibo
        self.boton1=tk.Button(self.ventana1, text="Pagar", command=self.calcular)

        
        #Asignamos la estructura y organización de los elementos: labels, botones, y radiobuttons
        self.label3.grid(column=1, row=0)
        self.label3['bg']='#cc66ff'
        self.label1.grid(column=0, row=1)
        #Se asigno color
        self.label1['bg']='#b3d9ff'
        self.entry1.grid(column=1, row=1)
        self.label2.grid(column=0, row=2)
        self.label2['bg']='#b3d9ff'
        self.entry2.grid(column=1, row=2)
        self.radio1.grid(column=1, row=3)
        self.radio1['bg']='#ffffcc'
        self.radio2.grid(column=1, row=4)
        self.radio2['bg']='#ffffcc'
        self.boton1.grid(column=1, row=5)
        self.boton1['bg']='#ff5050'

        
        self.ventana1['bg'] ='#ccccff'
        self.ventana1.mainloop()        

    #Se creo otra funcion para realizar todas las operaciones necesarias.
    def calcular(self):
        if self.seleccion.get()==1:
            #establecimos los datos como float para que no genere error al momento de que el usuario ingrese los datos.
            result=float(self.dato1.get())*float(self.dato2.get())
            messagebox.showinfo(title="Resultado", message="El total a pagar es: "+str(result))
        if self.seleccion.get()==2:
            #En este apartado se realiza el descuento del 20% al pagar con tarjeta
            results=((float(self.dato1.get())*float(self.dato2.get()))-(float(self.dato1.get())*float(self.dato2.get())*(20/100)))
            result=float(self.dato1.get())*float(self.dato2.get())
            messagebox.showinfo(title="Resultado", message="El total es de "+str(result)+" pero se aplicó un descuento del 20%, el monto a pagar es de: "+str(results))

programa=Progra1()