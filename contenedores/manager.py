from tkinter import Tk, Frame
from contenedores.container import Container
import costantes.titulos as cns
from costantes.colores import Colores
from costantes.tamaño import GEOMETRIA

class Manager(Tk):
    def __init__(self, *args, **kwar):
        super().__init__(*args, **kwar)
        self.title(cns.TIULOMANAGER)
        self.configure(bg=Colores.HEX.value)
        self.geometry(
            GEOMETRIA.GEOMETRIA_VENTANA.value
        )

        self.container = Frame(self, bg=Colores.HEX.value)
        self.container.pack(fill="both", expand=True)

        self.frames = {
            Container: None
        }
        self.carga_frames()
        self.mostrar_frames(Container)

    def carga_frames(self):
        for FrameClass in self.frames.keys():
            frame = FrameClass(self.container, self)
            self.frames[FrameClass] = frame

    def mostrar_frames(self, FrameClass):
        frame = self.frames[FrameClass]
        frame.tkraise()

def main():
    app = Manager()
    app.mainloop()

if __name__ == "__main__":
    main()
