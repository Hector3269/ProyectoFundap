import tkinter as tk
from PIL import Image, ImageTk

from costantes.Texto import Tipo_Letra
import costantes.imagen as img
import costantes.icon as icon
# modulos
from views.ventas import Ventas
from views.inventario import Inventario
# constantes
import costantes.titulos as cns
from costantes.tamaño import Tamaños_X_Y, Alto, Ancho, GEOMETRIA, Imagen_resize, Padx_icon, Tamaño_letra
from costantes.colores import Colores

class Container(tk.Frame):
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.controlador = controlador
        self.pack()
        self.place(
            x=Tamaños_X_Y.TAM_ZERO_X.value,
            y=Tamaños_X_Y.TAM_ZERO_Y.value,
            width=Alto.MEDIO.value,
            height=Ancho.MEDIO_ANCHO.value
        )

        self.config(
            bg=Colores.HEX.value
        )
        self.widgets()

    def mostrar_frames(self, container):
        top_level = tk.Toplevel(self)
        frame = container(
            top_level
        )
        frame.config(
            bg=Colores.HEX.value
        )
        frame.pack(
            fill="both",
            expand=True
        )
        top_level.geometry(
            GEOMETRIA.GEOMETRIA_VENTANA2.value
        )
        top_level.resizable(
            False,
            False
        )

    def ventas(self):
        self.mostrar_frames(
            Ventas
        )

    def inventario(self):
        self.mostrar_frames(
            Inventario
        )

    def widgets(self):
        frame1 = tk.Frame(
            self, bg=Colores.HEX.value
        )
        frame1.pack()
        frame1.place(
            x=Tamaños_X_Y.TAM_ZERO_X.value,
            y=Tamaños_X_Y.TAM_ZERO_Y.value,
            width=Alto.MEDIO.value,
            height=Ancho.MEDIO_ANCHO.value
        )

        imagen_pil = Image.open(
            icon.ICON_VENTAS
        )
        imagen_resize = imagen_pil.resize((
            Imagen_resize.IMAGEN_TAMAÑO_RESIZE_ICONO.value
        ))
        imagen_tk = ImageTk.PhotoImage(
            imagen_resize
        )
        btnventas = tk.Button(
            frame1,
            bg=Colores.ORANGEGERED.value,
            fg=Colores.WHITE.value,
            font=(
                Tipo_Letra.ARIAL.value,
                Tamaño_letra.MEDIANA_TAMAÑO_LETRA.value
            ),
            text=cns.BTN_TITULO_VENTAS,
            command=self.ventas,
            image=imagen_tk,
            compound=tk.LEFT,  
            padx=Padx_icon.NORMAL_PADX_ICON.value
        )
        btnventas.image = imagen_tk  
        btnventas.place(
            x=Tamaños_X_Y.TAM_NORMAL_X.value,
            y=Tamaños_X_Y.TAM_NORMAL_Y.value,
            width=Alto.PEQUEÑO.value,
            height=Ancho.PEQUEÑO_ANCHO.value
        )
        imagen_pil_inventario = Image.open(
            icon.ICON_INVENTARIO
        )
        imagen_resize_inventario = imagen_pil_inventario.resize((
            Imagen_resize.IMAGEN_TAMAÑO_RESIZE_ICONO.value
        ))
        imagen_tk_inventario = ImageTk.PhotoImage(
            imagen_resize_inventario
        )

        btninventario = tk.Button(
            frame1,
            bg=Colores.ORANGE.value,
            fg=Colores.WHITE.value,
            font=(
                Tipo_Letra.ARIAL.value,
                Tamaño_letra.MEDIANA_TAMAÑO_LETRA.value
            ),
            text=cns.BTN_TITULO_INVENTARIO,
            command=self.inventario,
            image=imagen_tk_inventario,  # Asignar la imagen del icono
            compound=tk.LEFT,
            padx=Padx_icon.MEDIO_PADX_ICON.value
        )
        btninventario.image = imagen_tk_inventario  # Mantener la referencia de la imagen
        btninventario.place(
            x=Tamaños_X_Y.TAM_NORMAL_COMPLEMENTO_X.value,
            y=Tamaños_X_Y.TAM_NORMAL_COMPLEMENTO_Y.value,
            width=Alto.PEQUEÑO.value,
            height=Ancho.PEQUEÑO_ANCHO.value
        )


        self.logo_imagen = Image.open(
            img.IMAGEN_CAJA_REGISTRADORA
        )
        self.logo_imagen = self.logo_imagen.resize((
            Imagen_resize.IMAGEN_TAMAÑO_RESIZE.value
        ))
        self.logo_imagen = ImageTk.PhotoImage(
            self.logo_imagen
        )
        self.logo_label = tk.Label(
            frame1, image=self.logo_imagen, bg=Colores.HEX.value
        )
        self.logo_label.place(
            x=Tamaños_X_Y.LOGO_X.value,
            y=Tamaños_X_Y.LOGO_Y.value,
        )

        copyright_label = tk.Label(
            frame1,
            text=cns.COPYRIG,
            font=(
                Tipo_Letra.ARIAL.value,
                Tamaño_letra.NORMAL_TAMAÑO_LETRA.value
            ),
            bg=Colores.HEX.value,
            fg=Colores.GRAY.value
        )
        copyright_label.place(
            x=Tamaños_X_Y.COPYRIGHT_X.value,
            y=Tamaños_X_Y.COPYRIGHT_Y.value,
        )
