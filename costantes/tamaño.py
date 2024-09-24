from enum import Enum

class Tamaños_X_Y(Enum):
    TAM_ZERO_X = 0
    TAM_ZERO_Y = 0

    TAM_NORMAL_X = 500
    TAM_NORMAL_Y = 30

    TAM_NORMAL_COMPLEMENTO_X = 500
    TAM_NORMAL_COMPLEMENTO_Y = 130
    # tamaño titulo
    TAM_COMPLEMENTO_X =5
    TAM_COMOLEMENTO_FRAME2 = 100

    # tamaño lblframe x,y
    LBLFRAME_X = 10
    LBLFRAME_Y = 10

    # Label factura
    LBLFRAME_FACTURA_X = 10
    LBLFRAME_FACTURA_Y = 5

    # label_nombre
    LBLFRAME_NOMBRE_X = 200
    LBLFRAME_NOMBRE_Y = 10

    # label_valor
    LBLFRAME_VALOR_X = 470,
    LBLFRAME_VALOR_Y = 12,

    # label_cantidad
    LBLFRAME_CANTIDAD_X = 750
    LBLFRAME_CANTIDAD_Y = 12

    # entry_numero_factura
    ENTRY_FACTURA_X = 100
    ENTRY_FACTURA_Y = 10

    # entry_nombre
    ENTRY_NOMBRE_X = 280
    ENTRY_NOMBRE_Y = 10

    #entry_valor
    ENTRY_VALOR_X = 540
    ENTRY_VALOR_Y = 10

    # entry_cantidad
    ENTRY_CANIDAD_X = 860
    ENTRY_CANIDAD_Y = 10


    # treFrame
    TRE_FRAME_X = 150
    TRE_FRAME_Y = 120

    # lblframe1
    LBLFRAME1_X = 10
    LBLFRAME1_Y = 380

    # label_suma_total
    SUMA_TOTAL_X =360
    SUMA_TOTAL_Y = 335

    # BOTONES
    BOTON_AGREGAR_X =90
    BOTON_AGREGAR_Y =10

    # boton pagar
    BOTON_PAGAR_X = 400
    BOTON_PAGAR_Y = 10

    # boton ver factura
    BOTON_VER_FACTURA_X = 750
    BOTON_VER_FACTURA_Y = 10
    #x y LOGO
    LOGO_X =100
    LOGO_Y = 30

    # copyright_label x y
    COPYRIGHT_X = 180
    COPYRIGHT_Y = 350
    # copyright_label ventas x y
    COPYRIGHT_VENTAS_X = 320
    COPYRIGHT_VENTAS_Y = 500

    # Inventario
    LABEL_FRAME_X = 30
    LABEL_FRAME_Y = 10

    LABEL_FRAME_TITULO_X = 10

    # botone inventario
    BOTONES_INVENTARIO_X = 80
    BOTONES_INVENTARIO_Y = 340
    BOTONES_INVENTARIO_2_X = 400

    # ACTUALIZAR
    BOTONES_INVENTARIO_3_X = 440
    BOTONES_INVENTARIO_3_Y = 500



class Alto(Enum):
    NORMAL = 1100
    NORMAL_COMPLEMENTO = 1090
    MEDIO = 800
    PEQUEÑO = 240

    # entry_numero_factura
    ENTRY_FACTURA_ALTO=80

    # entry_nombre
    ENTRY_NOMBRE_ALTO =180

    # entry_valor
    ENTRY_VALOR_ALTO = 200

    # entry_cantidad
    ENTRY_CANIDAD_ALTO = 180

    # tamaño lblframe
    ALTO_LBLFRAME = 1060


    # treFrame
    TRE_FRAME_ALTO = 800

    # botones
    BOTON_AGREGAR_ALTO = 250

    # labelframe
    LABEL_FRAME_ALTO =400

    #
    LABEL_FRAME_ALTO_TEXT = 240


class Ancho(Enum):
    NORMAL_ANCHO = 100
    NORMAL_ANCHO_COMPLEMENTO = 90
    MEDIO_ANCHO = 400
    PEQUEÑO_ANCHO = 60

    #frame
    COMPLEMENTO_ANCHO_FRAME2 = 550

    # tamaño lblframe
    ANCHO_LBLFRAME = 80

    # tamaño lblframe
    ANCHO_LBLFRAME1 = 100

    # treFrame
    TRE_FRAME_ANCHO = 200

    # treFrame vista ancho
    TRE_FRAME_ANCHO_V = 200

    # botones
    BOTON_AGREGAR_ANCHO =50

    # labelframe
    LABEL_FRAME_ANCHO = 550

    # labelframe texto
    LABEL_FRAME_ANCHO_TEXT = 50


class GEOMETRIA(Enum):
    GEOMETRIA_VENTANA= "800x400+120+20"
    GEOMETRIA_VENTANA2 = "1100x670+120+20"

class hgckness(Enum):
    TAMAÑO_NESS = 1

class Imagen_resize(Enum):
   IMAGEN_TAMAÑO_RESIZE = 280,280
   IMAGEN_TAMAÑO_RESIZE_ICONO = 50, 50

class Padx_icon(Enum):
    NORMAL_PADX_ICON = 30
    MEDIO_PADX_ICON = 20
    PEQUEÑO_PADX_ICON =10

class Tamaño_letra(Enum):
    NORMAL_TAMAÑO_LETRA = 12
    MEDIANA_TAMAÑO_LETRAS = 16
    MEDIANA_TAMAÑO_LETRA= 18
    GRANDE_TAMAÑO = 30

class LABEL_FRAME_X_Y (Enum):

    # para todas las x en los formularios
    LABEL_FRAME_TEXTO_FORM_X =140

# label y de los

    # nombre
    LABEL_FRAME_NOMBRE_Y = 20

    # probedor
    LABEL_FRAME_PROVEDOR_Y = 80

    # precio
    LABEL_FRAME_PRECIO_Y = 140

    # costo
    LABEL_FRAME_COSTO_Y = 260

    # EXISTENCIA
    LABEL_FRAME_EXISTENCIA_Y = 200


class TRE_X_Y (Enum):

    #treFrame
    TRE_FRAME_X = 440
    TRE_FRAME_Y = 20



class TRE_ALTO_T (Enum):

    # treFrame
    TRE_FRAME_ALTO = 670


class TRE_ANCHO_T(Enum):
    TRE_ANCHO_VIEW = 40
    # treFrame
    TRE_FRAME_ANCHO = 500

    # Widget Treeview
    TREE_VIEW_ANCHO_T = 400

class TRE_COLOMN (Enum):
    TAM_NORMAL_COL =70
    TAM_MEDIANA_COL = 100



