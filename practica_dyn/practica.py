import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


class MiAplicacion:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Mi imagen")
        self.ventana.geometry("500x667")
        self.ventana.resizable(False, False)

        # Cargar imagen
        imagen = Image.open("5356dc7d6816917124e59312b1671d40.jpg")
        imagen = imagen.resize((500, 667))

        self.foto = ImageTk.PhotoImage(imagen)

        # Imagen de fondo
        self.etiqueta = tk.Label(
            self.ventana,
            image=self.foto
        )
        self.etiqueta.place(x=0, y=0, relwidth=1, relheight=1)

        # Botón
        self.boton = tk.Button(
            self.ventana,
            text="Presióname",
            command=self.saludar,
            font=("Arial", 12),
            bg="white",
            fg="black"
        )
        self.boton.place(relx=0.5, rely=0.9, anchor="center")

    # Función del botón
    def saludar(self):
        messagebox.showinfo("Mensaje", "¡Hola! ¿Cómo estás?")


# Ejecutar aplicación
ventana = tk.Tk()
app = MiAplicacion(ventana)
ventana.mainloop()