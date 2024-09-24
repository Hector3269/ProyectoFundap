from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox

from PIL import Image, ImageTk

# contantes
import costantes.icon as icon
import costantes.titulos as cns
from costantes.colores import Colores
from costantes.tamaño import Tamaños_X_Y, Alto, Ancho, hgckness, Tamaño_letra, Padx_icon, Imagen_resize
from costantes.Texto import Tipo_Letra, ANCHOR
from costantes.comportamiento import Comportamiento
from costantes.ubicacion import UBICACION

class Ventas(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.widgets()

    def widgets(self):
        frame1 = tk.Frame(
            self,
            bg=Colores.ORANGE.value,
            highlightbackground=Colores.GRAY.value,
            highlightthickness=hgckness.TAMAÑO_NESS.value

        )
        frame1.pack()
        frame1.place(
            x=Tamaños_X_Y.TAM_ZERO_X.value,
            y=Tamaños_X_Y.TAM_ZERO_Y.value,
            width=Alto.NORMAL.value,
            height=Ancho.NORMAL_ANCHO.value
        )

        titulo = tk.Label(
            frame1,
            text=cns.TITULO_VENTAS,
            font=(
                Tipo_Letra.NEGRITA.value,
                Tamaño_letra.GRANDE_TAMAÑO.value
            ),
            bg=Colores.ORANGE.value,
            anchor=ANCHOR.ANCHOR_CENTRO.value
        )
        titulo.pack()
        titulo.place(
            x=Tamaños_X_Y.TAM_COMPLEMENTO_X.value,
            y=Tamaños_X_Y.TAM_ZERO_Y.value,
            width=Alto.NORMAL_COMPLEMENTO.value,
            height=Ancho.NORMAL_ANCHO_COMPLEMENTO.value
        )

        frame2 = tk.Frame(
            self,
            bg=Colores.HEX_ASUL.value,
            highlightbackground=Colores.GRAY.value,
            highlightthickness=hgckness.TAMAÑO_NESS.value
        )
        frame2.place(
            x=Tamaños_X_Y.TAM_ZERO_X.value,
            y=Tamaños_X_Y.TAM_COMOLEMENTO_FRAME2.value,
            width=Alto.NORMAL.value,
            height=Ancho.COMPLEMENTO_ANCHO_FRAME2.value
        )
        lblframe = LabelFrame(
            frame2,
            text=cns.INFORMACION_VENTA,
            bg=Colores.LIME.value,
            font=(
                Tipo_Letra.NEGRITA.value,
                Tamaño_letra.MEDIANA_TAMAÑO_LETRAS.value
            ),
        )
        lblframe.place(
            x=Tamaños_X_Y.LBLFRAME_X.value,
            y=Tamaños_X_Y.LBLFRAME_Y.value,
            width=Alto.ALTO_LBLFRAME.value,
            height=Ancho.ANCHO_LBLFRAME.value
        )
        label_numero_factura = tk.Label(
            lblframe,
            text=cns.NUMERO_FACTURA,
            bg=Colores.LIME.value,
            font=(
                Tipo_Letra.NEGRITA.value,
                Tamaño_letra.NORMAL_TAMAÑO_LETRA.value
            )
        )

        label_numero_factura.place(
            x=Tamaños_X_Y.LBLFRAME_FACTURA_X.value,
            y=Tamaños_X_Y.LBLFRAME_FACTURA_Y.value
        )
        self.numero_factura = tk.StringVar()

        self.entry_numero_factura = ttk.Entry(
            lblframe,
            textvariable=self.numero_factura,
            state=Comportamiento.SOLO_LECTURA.value,
            font=(
                Tipo_Letra.NEGRITA.value,
                Tamaño_letra.NORMAL_TAMAÑO_LETRA.value
            )
        )
        self.entry_numero_factura.place(
            x=Tamaños_X_Y.ENTRY_FACTURA_X.value,
            y=Tamaños_X_Y.ENTRY_FACTURA_Y.value,
            width=Alto.ENTRY_FACTURA_ALTO.value
        )
        label_nombre = tk.Label(
            lblframe,
            text=cns.PRODUCTO_NOMBRE,
            bg=Colores.LIME.value,
            font=(
                Tipo_Letra.NEGRITA.value,
                Tamaño_letra.NORMAL_TAMAÑO_LETRA.value
            )
        )
        label_nombre.place(
            x=Tamaños_X_Y.LBLFRAME_NOMBRE_X.value,
            y=Tamaños_X_Y.LBLFRAME_NOMBRE_Y.value
        )
        self.entry_nombre = ttk.Combobox(
            lblframe,
            font=(
                Tipo_Letra.NEGRITA.value,
                Tamaño_letra.NORMAL_TAMAÑO_LETRA.value
            ),
            state=Comportamiento.SOLO_LECTURA.value,
        )
        self.entry_nombre.place(
            x=Tamaños_X_Y.ENTRY_NOMBRE_X.value,
            y=Tamaños_X_Y.ENTRY_NOMBRE_Y.value,
            width=Alto.ENTRY_NOMBRE_ALTO.value
        )

        label_valor = tk.Label(
            lblframe,
            text=cns.VALOR,
            bg=Colores.LIME.value,
            font=(
                Tipo_Letra.NEGRITA.value,
                Tamaño_letra.NORMAL_TAMAÑO_LETRA.value
            )
        )
        label_valor.place(
            x=Tamaños_X_Y.LBLFRAME_VALOR_X.value,
            y=Tamaños_X_Y.LBLFRAME_VALOR_Y.value,
        )
        self.entry_valor = ttk.Entry(
            lblframe,
            font=(
                Tipo_Letra.NEGRITA.value,
                Tamaño_letra.NORMAL_TAMAÑO_LETRA.value
            ),
            state=Comportamiento.SOLO_LECTURA.value,
        )
        self.entry_valor.place(
            x=Tamaños_X_Y.ENTRY_VALOR_X.value,
            y=Tamaños_X_Y.ENTRY_VALOR_Y.value,
            width=Alto.ENTRY_VALOR_ALTO.value
        )

        label_cantidad = tk.Label(
            lblframe,
            text=cns.CANIDAD,
            bg=Colores.LIME.value,
            font=(
                Tipo_Letra.NEGRITA.value,
                Tamaño_letra.NORMAL_TAMAÑO_LETRA.value
            )
        )
        label_cantidad.place(
            x=Tamaños_X_Y.LBLFRAME_CANTIDAD_X.value,
            y=Tamaños_X_Y.LBLFRAME_CANTIDAD_Y.value,
        )
        self.entry_cantidad = ttk.Entry(
            lblframe,
            font=(
                Tipo_Letra.NEGRITA.value,
                Tamaño_letra.NORMAL_TAMAÑO_LETRA.value
            )
        )
        self.entry_cantidad.place(
            x=Tamaños_X_Y.ENTRY_CANIDAD_X.value,
            y=Tamaños_X_Y.ENTRY_CANIDAD_Y.value,
            width=Alto.ENTRY_CANIDAD_ALTO.value
        )

        # Crear el contenedor del Treeview
        treFrame = tk.Frame(
            frame2,
            bg=Colores.HEX_ASUL.value
        )
        treFrame.place(
            x=Tamaños_X_Y.TRE_FRAME_X.value,
            y=Tamaños_X_Y.TRE_FRAME_Y.value,
            width=Alto.TRE_FRAME_ALTO.value,
            height=Ancho.TRE_FRAME_ANCHO.value
        )

        # Barra de desplazamiento vertical
        scrol_y = ttk.Scrollbar(
            treFrame,
            orient=VERTICAL
        )
        scrol_y.pack(
            side=RIGHT,
            fill=Y
        )

        # Barra de desplazamiento horizontal
        scrol_x = ttk.Scrollbar(
            treFrame,
            orient=HORIZONTAL
        )
        scrol_x.pack(
            side=BOTTOM,
            fill=X
        )

        # TreeView para mostrar la lista de artículos
        self.tree = ttk.Treeview(
            treFrame,
            columns=(
                cns.PRODUCTO,
                cns.PRECIO,
                cns.CANTIDAD_TABLA,
                cns.SUPTOTAL
            ),
            show="headings",
            height=Ancho.TRE_FRAME_ANCHO_V.value,
            yscrollcommand=scrol_y.set,
            xscrollcommand=scrol_x.set

        )
        scrol_y.config(
            command=self.tree.yview
        )
        scrol_x.config(
            command=self.tree.xview
        )

        self.tree.heading(
            UBICACION.UBI1.value,
            text=cns.PRODUCTO
        )
        self.tree.heading(
            UBICACION.UBI2.value,
            text=cns.PRECIO
        )
        self.tree.heading(
            UBICACION.UBI3.value,
            text=cns.CANTIDAD_TABLA
        )
        self.tree.heading(
            UBICACION.UBI4.value,
            text=cns.SUPTOTAL
        )
        self.tree.column(
            cns.PRODUCTO,
            anchor=ANCHOR.ANCHOR_CENTRO.value
        )
        self.tree.column(
            cns.PRECIO,
            anchor=ANCHOR.ANCHOR_CENTRO.value
        )
        self.tree.column(
            cns.CANTIDAD_TABLA,
            anchor=ANCHOR.ANCHOR_CENTRO.value
        )
        self.tree.column(
            cns.SUPTOTAL,
            anchor=ANCHOR.ANCHOR_CENTRO.value
        )
        self.tree.pack(
            expand=True,
            fill=BOTH
        )
        # LabelFrame inferior
        lblframe1 = LabelFrame(
            frame2,
            text=cns.OPCION,
            bg=Colores.LIME.value,
            font=(
                Tipo_Letra.NEGRITA.value,
                Tamaño_letra.MEDIANA_TAMAÑO_LETRA.value
            )
        )
        lblframe1.place(
            x=Tamaños_X_Y.LBLFRAME1_X.value,
            y=Tamaños_X_Y.LBLFRAME1_Y.value,
            width=Alto.ALTO_LBLFRAME.value,
            height=Ancho.ANCHO_LBLFRAME1.value
        )
        # botones
        imagen_pil_boton_agregar = Image.open(
            icon.ICON_BT_AGREGAR
        )
        imagen_resize_boton_agregar = imagen_pil_boton_agregar.resize((
            Imagen_resize.IMAGEN_TAMAÑO_RESIZE_ICONO.value
        ))
        imagen_tk_boton_agregar = ImageTk.PhotoImage(imagen_resize_boton_agregar)
        boton_agregar = tk.Button(
            lblframe1,
            bg=Colores.LAWNGREEN.value,
            fg=Colores.WHITE.value,
            font=(
                Tipo_Letra.ARIAL.value,
                Tamaño_letra.MEDIANA_TAMAÑO_LETRA.value
            ),
            text=cns.AGREGAR_BOTON,
            image=imagen_tk_boton_agregar,
            compound=tk.LEFT,
            padx=Padx_icon.PEQUEÑO_PADX_ICON.value
        )
        boton_agregar.image = imagen_tk_boton_agregar  # Mantener la referencia de la imagen
        boton_agregar.place(
            x=Tamaños_X_Y.BOTON_AGREGAR_X.value,
            y=Tamaños_X_Y.BOTON_AGREGAR_Y.value,
            width=Alto.BOTON_AGREGAR_ALTO.value,
            height=Ancho.BOTON_AGREGAR_ANCHO.value
        )

        # Botón agregar
        imagen_pil_boton_agregar = Image.open(
            icon.ICON_BT_AGREGAR
        )
        imagen_resize_boton_agregar = imagen_pil_boton_agregar.resize((
            Imagen_resize.IMAGEN_TAMAÑO_RESIZE_ICONO.value
        ))
        imagen_tk_boton_agregar = ImageTk.PhotoImage(
            imagen_resize_boton_agregar
        )

        boton_agregar = tk.Button(
            lblframe1,
            bg=Colores.ORANGEGERED.value,
            fg=Colores.WHITE.value,
            font=(
                Tipo_Letra.ARIAL.value,
                Tamaño_letra.MEDIANA_TAMAÑO_LETRA.value
            ),
            text=cns.AGREGAR_BOTON,
            image=imagen_tk_boton_agregar,
            compound=tk.LEFT,
            padx=Padx_icon.PEQUEÑO_PADX_ICON.value
        )
        boton_agregar.image = imagen_tk_boton_agregar  # Mantener la referencia de la imagen
        boton_agregar.place(
            x=Tamaños_X_Y.BOTON_AGREGAR_X.value,
            y=Tamaños_X_Y.BOTON_AGREGAR_Y.value,
            width=Alto.BOTON_AGREGAR_ALTO.value,
            height=Ancho.BOTON_AGREGAR_ANCHO.value
        )

        # Botón pagar
        imagen_pil_boton_pagar = Image.open(
            icon.ICON_BT_PAGAR
        )
        imagen_resize_boton_pagar = imagen_pil_boton_pagar.resize((
            Imagen_resize.IMAGEN_TAMAÑO_RESIZE_ICONO.value
        ))
        imagen_tk_boton_pagar = ImageTk.PhotoImage(
            imagen_resize_boton_pagar
        )

        boton_pagar = tk.Button(
            lblframe1,
            text=cns.PAGAR_BOTON,
            bg=Colores.GOLD.value,
            fg=Colores.WHITE.value,
            font=(
                Tipo_Letra.ARIAL.value,
                Tamaño_letra.MEDIANA_TAMAÑO_LETRA.value
            ),
            image=imagen_tk_boton_pagar,
            compound=tk.LEFT,
            padx=Padx_icon.PEQUEÑO_PADX_ICON.value
        )
        boton_pagar.image = imagen_tk_boton_pagar
        boton_pagar.place(
            x=Tamaños_X_Y.BOTON_PAGAR_X.value,
            y=Tamaños_X_Y.BOTON_PAGAR_Y.value,
            width=Alto.BOTON_AGREGAR_ALTO.value,
            height=Ancho.BOTON_AGREGAR_ANCHO.value
        )

        # Botón ver facturas
        imagen_pil_boton_ver_facturas = Image.open(
            icon.ICON_BT_VER_FACTURA
        )
        imagen_resize_boton_ver_facturas = imagen_pil_boton_ver_facturas.resize((
            Imagen_resize.IMAGEN_TAMAÑO_RESIZE_ICONO.value
        ))
        imagen_tk_boton_ver_facturas = ImageTk.PhotoImage(imagen_resize_boton_ver_facturas)
        boton_ver_facturas = tk.Button(
            lblframe1,
            text=cns.VER_FACTURA,
            bg=Colores.ORANGEGERED.value,
            fg=Colores.WHITE.value,
            font=(Tipo_Letra.ARIAL.value, Tamaño_letra.MEDIANA_TAMAÑO_LETRA.value),
            image=imagen_tk_boton_ver_facturas,
            compound=tk.LEFT,
            padx=Padx_icon.PEQUEÑO_PADX_ICON.value
        )
        boton_ver_facturas.image = imagen_tk_boton_ver_facturas
        boton_ver_facturas.place(
            x=Tamaños_X_Y.BOTON_VER_FACTURA_X.value,
            y=Tamaños_X_Y.BOTON_VER_FACTURA_Y.value,
            width=Alto.BOTON_AGREGAR_ALTO.value,
            height=Ancho.BOTON_AGREGAR_ANCHO.value
        )

        # Label Suma Total
        self.label_suma_total = tk.Label(
            frame2,
            text=cns.SUMA,
            bg=Colores.HEX_ASUL.value,
            font=(
                Tipo_Letra.ARIAL.value,
                Tamaño_letra.GRANDE_TAMAÑO.value
            ),
        )
        self.label_suma_total.place(
            x=Tamaños_X_Y.SUMA_TOTAL_X.value,
            y=Tamaños_X_Y.SUMA_TOTAL_Y.value
        )

        copyright_label = tk.Label(
            frame2,
            text=cns.COPYRIG,
            font=(
                Tipo_Letra.ARIAL.value,
                Tamaño_letra.NORMAL_TAMAÑO_LETRA.value
            ),
            bg=Colores.HEX_ASUL.value,
            fg=Colores.GRAY.value
        )
        copyright_label.place(
            x=Tamaños_X_Y.COPYRIGHT_VENTAS_X.value,
            y=Tamaños_X_Y.COPYRIGHT_VENTAS_Y.value,
        )