import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk

# Datos del carrusel
productos = [
    {"imagen": "zapato1.jpg", "precio": "$250000", "descripcion": "rojo primavera", "referencia": "REF001"},
    {"imagen": "zapato2.jpg", "precio": "$175000", "descripcion": "bota negra ", "referencia": "REF002"},
    {"imagen": "zapato3.jpg", "precio": "$280.000", "descripcion": "Zapato Beige", "referencia": "REF004"},
]

class CarruselCalzado:
    def __init__(self, root):
        self.root = root
        self.root.title("Carrusel de Calzado")
        
        self.indice = 0
        
        self.imagen_label = Label(root)
        self.imagen_label.pack()
        
        self.precio_label = Label(root, text="", font=("Arial", 14))
        self.precio_label.pack()
        
        self.descripcion_label = Label(root, text="", font=("Arial", 12))
        self.descripcion_label.pack()
        
        self.referencia_label = Label(root, text="", font=("Arial", 10))
        self.referencia_label.pack()
        
        self.btn_anterior = Button(root, text="Anterior", command=self.anterior)
        self.btn_anterior.pack(side=tk.LEFT)
        
        self.btn_siguiente = Button(root, text="Siguiente", command=self.siguiente)
        self.btn_siguiente.pack(side=tk.RIGHT)
        
        self.mostrar_producto()
    
    def mostrar_producto(self):
        producto = productos[self.indice]
        imagen = Image.open(producto["imagen"])
        imagen = imagen.resize(400, 400),
        self.imagen_tk = ImageTk.PhotoImage(imagen)
        
        self.imagen_label.config(image=self.imagen_tk)
        self.precio_label.config(text=f"Precio: {producto['precio']}")
        self.descripcion_label.config(text=f"Descripción: {producto['descripcion']}")
        self.referencia_label.config(text=f"Referencia: {producto['referencia']}")
    
    def anterior(self):
        self.indice = (self.indice - 1) % len(productos)
        self.mostrar_producto()
    
    def siguiente(self):
        self.indice = (self.indice + 1) % len(productos)
        self.mostrar_producto()

if __name__ == "__main__":
    root = tk.Tk()
    carrusel = CarruselCalzado(root)
    root.mainloop()
