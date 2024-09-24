from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox

import costantes.titulos as cns
from costantes.tamaño import Tamaños_X_Y, Alto, Ancho, hgckness, Tamaño_letra, LABEL_FRAME_X_Y, TRE_X_Y, TRE_ALTO_T, \
    TRE_ANCHO_T, TRE_COLOMN
from costantes.Texto import Tipo_Letra, ANCHOR
from costantes.colores import Colores

class Inventario(tk.Frame):
    def __init__(self, padre):
        super().__init__(padre)
        self.widgets()

    def widgets(self):
        # Frame superior
        frame1 = tk.Frame(
            self,
            bg=Colores.ORANGEGERED.value,
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
            text=cns.TITULO_INVENTARIO,
            font=(
                Tipo_Letra.NEGRITA.value,
                Tamaño_letra.GRANDE_TAMAÑO.value
            ),
            bg=Colores.ORANGEGERED.value,
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
        # LabelFrame llenar datos
        labelframe = LabelFrame(
            frame2,
            text=cns.PRODUCTO_INVENTARIO,
            font=(
                Tipo_Letra.NEGRITA.value,
                Tamaño_letra.GRANDE_TAMAÑO.value
            ),
            bg=Colores.ORANGEGERED.value
        )
        labelframe.place(
            x=Tamaños_X_Y.LABEL_FRAME_X.value,
            y=Tamaños_X_Y.LABEL_FRAME_Y.value,
            width=Alto.LABEL_FRAME_ALTO.value,
            height=Ancho.LABEL_FRAME_ANCHO.value
        )

        lblnombre = Label(
            labelframe,
            text=cns.NOMOBRE_INVENTARIO,
            font=(
                Tipo_Letra.NEGRITA.value,
                Tamaño_letra.MEDIANA_TAMAÑO_LETRAS.value
            ),
            bg=Colores.ORANGEGERED.value
        )
        lblnombre.place(
            x=Tamaños_X_Y.LABEL_FRAME_TITULO_X.value,
            y=LABEL_FRAME_X_Y.LABEL_FRAME_NOMBRE_Y.value
        )
        self.nombre = ttk.Entry(
            labelframe,
            font=(
                Tipo_Letra.NEGRITA.value,
                Tamaño_letra.MEDIANA_TAMAÑO_LETRAS.value
            )
        )
        self.nombre.place(
            x=LABEL_FRAME_X_Y.LABEL_FRAME_TEXTO_FORM_X.value,
            y=LABEL_FRAME_X_Y.LABEL_FRAME_NOMBRE_Y.value,
            width=Alto.LABEL_FRAME_ALTO_TEXT.value,
            height=Ancho.LABEL_FRAME_ANCHO_TEXT.value
        )

        lblproveedor = Label(
            labelframe,
            text=cns.PRIVEEDOR,
            font=(
                Tipo_Letra.NEGRITA.value,
                Tamaño_letra.MEDIANA_TAMAÑO_LETRAS.value
            ),
            bg=Colores.ORANGEGERED.value
        )
        lblproveedor.place(
            x=Tamaños_X_Y.LABEL_FRAME_TITULO_X.value,
            y=LABEL_FRAME_X_Y.LABEL_FRAME_PROVEDOR_Y.value
        )
        self.proveedor = ttk.Entry(
            labelframe,
            font=(
                Tipo_Letra.NEGRITA.value,
                Tamaño_letra.MEDIANA_TAMAÑO_LETRAS.value
            ),
        )
        self.proveedor.place(
            x=LABEL_FRAME_X_Y.LABEL_FRAME_TEXTO_FORM_X.value,
            y=LABEL_FRAME_X_Y.LABEL_FRAME_PROVEDOR_Y.value,
            width=Alto.LABEL_FRAME_ALTO_TEXT.value,
            height=Ancho.LABEL_FRAME_ANCHO_TEXT.value
        )

        lblprecio = Label(
            labelframe,
            text=cns.PRECIO_INVENTARIO,
            font=(
                Tipo_Letra.NEGRITA.value,
                Tamaño_letra.MEDIANA_TAMAÑO_LETRAS.value
            ),
            bg=Colores.ORANGEGERED.value
        )
        lblprecio.place(
            x=Tamaños_X_Y.LABEL_FRAME_TITULO_X.value,
            y=LABEL_FRAME_X_Y.LABEL_FRAME_PRECIO_Y.value
        )
        self.precio = ttk.Entry(
            labelframe,
            font=(
                Tipo_Letra.NEGRITA.value,
                Tamaño_letra.MEDIANA_TAMAÑO_LETRAS.value
            )
        )
        self.precio.place(
            x=LABEL_FRAME_X_Y.LABEL_FRAME_TEXTO_FORM_X.value,
            y=LABEL_FRAME_X_Y.LABEL_FRAME_PRECIO_Y.value,
            width=Alto.LABEL_FRAME_ALTO_TEXT.value,
            height=Ancho.LABEL_FRAME_ANCHO_TEXT.value
        )

        lblcosto = Label(
            labelframe,
            text=cns.COSTO_INVENTARIO,
            font=(
                Tipo_Letra.NEGRITA.value,
                Tamaño_letra.MEDIANA_TAMAÑO_LETRAS.value
            ),
            bg=Colores.ORANGEGERED.value
        )
        lblcosto.place(
            x=Tamaños_X_Y.LABEL_FRAME_TITULO_X.value,
            y=LABEL_FRAME_X_Y.LABEL_FRAME_COSTO_Y.value
        )
        self.costo = ttk.Entry(
            labelframe,
            font=(
                Tipo_Letra.NEGRITA.value,
                Tamaño_letra.MEDIANA_TAMAÑO_LETRAS.value
            ),
        )
        self.costo.place(
            x=LABEL_FRAME_X_Y.LABEL_FRAME_TEXTO_FORM_X.value,
            y=LABEL_FRAME_X_Y.LABEL_FRAME_COSTO_Y.value,
            width=Alto.LABEL_FRAME_ALTO_TEXT.value,
            height=Ancho.LABEL_FRAME_ANCHO_TEXT.value
        )

        lblExistencias = Label(
            labelframe,
            text=cns.EXISTENCIA_INVENTARIO,
            font=(
                Tipo_Letra.NEGRITA.value,
                Tamaño_letra.MEDIANA_TAMAÑO_LETRAS.value
            ),
            bg=Colores.ORANGEGERED.value
        )
        lblExistencias.place(
            x=Tamaños_X_Y.LABEL_FRAME_TITULO_X.value,
            y=LABEL_FRAME_X_Y.LABEL_FRAME_EXISTENCIA_Y.value
        )

        self.Existencias = ttk.Entry(
            labelframe,
            font=(
                Tipo_Letra.NEGRITA.value,
                Tamaño_letra.MEDIANA_TAMAÑO_LETRAS.value
            ),
        )
        self.Existencias.place(
            x=LABEL_FRAME_X_Y.LABEL_FRAME_TEXTO_FORM_X.value,
            y=LABEL_FRAME_X_Y.LABEL_FRAME_EXISTENCIA_Y.value,
            width=Alto.LABEL_FRAME_ALTO_TEXT.value,
            height=Ancho.LABEL_FRAME_ANCHO_TEXT.value
        )

# BOTONES

        boton_agregar = tk.Button(
            labelframe,
            text=cns.INGRESAR_PRODUCTO,
            font=(
                Tipo_Letra.ARIAL.value,
                Tamaño_letra.MEDIANA_TAMAÑO_LETRAS.value
            ),
            fg=Colores.WHITE.value,
            bg=Colores.RED.value
        )
        boton_agregar.place(
            x=Tamaños_X_Y.BOTONES_INVENTARIO_X.value,
            y=Tamaños_X_Y.BOTONES_INVENTARIO_Y.value,
            width=Alto.BOTON_AGREGAR_ALTO.value,
            height=Ancho.BOTON_AGREGAR_ANCHO.value
        )

        boton_editar = tk.Button(
            labelframe,
            text=cns.EDITAR_PRODUCTO,
            font=(
                Tipo_Letra.ARIAL.value,
                Tamaño_letra.MEDIANA_TAMAÑO_LETRAS.value
            ),
            fg=Colores.WHITE.value,
            bg=Colores.RED.value
        )
        boton_editar.place(
            x=Tamaños_X_Y.BOTONES_INVENTARIO_X.value,
            y=Tamaños_X_Y.BOTONES_INVENTARIO_2_X.value,
            width=Alto.BOTON_AGREGAR_ALTO.value,
            height=Ancho.BOTON_AGREGAR_ANCHO.value
        )

# TreeView Tabla
        treFrame = Frame(
            frame2,
            bg=Colores.WHITE.value
        )
        treFrame.place(
            x=TRE_X_Y.TRE_FRAME_X.value,
            y=TRE_X_Y.TRE_FRAME_Y.value,
            width=TRE_ALTO_T.TRE_FRAME_ALTO.value,
            height=TRE_ANCHO_T.TRE_FRAME_ANCHO.value
        )
# Barra de desplazamiento vertical
        scrol_y = ttk.Scrollbar(
            treFrame
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

# Widget Treeview
        self.tre = ttk.Treeview(
            treFrame,
            yscrollcommand=scrol_y.set,
            xscrollcommand=scrol_x.set,
            height=TRE_ANCHO_T.TREE_VIEW_ANCHO_T.value,
            columns=(
                "ID",
                "PRODUCTO",
                "PROVEEDOR",
                "PRECIO",
                "COSTO",
                "EXISTENCIAS"
            ),
            show="headings"
        )
        self.tre.pack(
            expand=True,
            fill=BOTH
        )

        scrol_y.config(
            command=self.tre.yview
        )
        scrol_x.config(
            command=self.tre.xview
        )

        self.tre.heading(
            "ID",
            text=cns.T_ID
        )
        self.tre.heading(
            "PRODUCTO",
            text=cns.T_PRODUCTO
        )
        self.tre.heading(
            "PROVEEDOR",
            text=cns.T_PROVEEDOR)
        self.tre.heading(
            "PRECIO",
            text=cns.T_PRECIO
        )
        self.tre.heading(
            "COSTO",
            text=cns.T_COSTO
        )
        self.tre.heading(
            "EXISTENCIAS",
            text=cns.T_EXISTENCIAS
        )

        self.tre.column(
            "ID",
            width=TRE_COLOMN.TAM_NORMAL_COL.value,
            anchor=ANCHOR.ANCHOR_CENTRO.value
        )
        self.tre.column(
            "PRODUCTO",
            width=TRE_COLOMN.TAM_MEDIANA_COL.value,
            anchor=ANCHOR.ANCHOR_CENTRO.value
        )
        self.tre.column(
            "PROVEEDOR",
            width=TRE_COLOMN.TAM_MEDIANA_COL.value,
            anchor=ANCHOR.ANCHOR_CENTRO.value
        )
        self.tre.column(
            "PRECIO",
            width=TRE_COLOMN.TAM_MEDIANA_COL.value,
            anchor=ANCHOR.ANCHOR_CENTRO.value
        )
        self.tre.column(
            "COSTO",
            width=TRE_COLOMN.TAM_MEDIANA_COL.value,
            anchor=ANCHOR.ANCHOR_CENTRO.value
        )
        self.tre.column(
            "EXISTENCIAS",
            width=TRE_COLOMN.TAM_NORMAL_COL.value,
            anchor=ANCHOR.ANCHOR_CENTRO.value
        )


        btn_actualizar = Button(
            frame2,
            text=cns.ACTUALIZAR_T,
            font="sans 14 bold",
            bg=Colores.GREENYELLOW.value,
            fg=Colores.WHITE.value
        )
        btn_actualizar.place(
            x=Tamaños_X_Y.BOTONES_INVENTARIO_3_X.value,
            y=Tamaños_X_Y.BOTONES_INVENTARIO_3_Y.value,
            width=Alto.BOTON_AGREGAR_ALTO.value,
            height=Ancho.BOTON_AGREGAR_ANCHO.value
        )


