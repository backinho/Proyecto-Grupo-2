import os.path
import tkinter as tk
from tkinter import font
from tkinter import messagebox
from typing_extensions import Literal
import recurses.util_ventana as util_vent
import recurses.util_imagenes as util_img
from recurses.paleta_colores import *
from recurses.administrador.login import login_class
from recurses.dashboard.dashboard import dashboard_class

class vent_pricipal(tk.Tk):

    def __init__(self):
        super().__init__()
        self.imagen_fondo = util_img.util_img(os.path.join(os.path.dirname(__file__), "datos/Fondo.png"), (250, 250))
        self.vent_principal_conf()
        self.frames()
        self.imagenes()
        self.botones()
        self.escrito()

    def vent_principal_conf(self):
        self.title("Inicio")
        self.configure(bg=dos)
        w, h = 1024, 600
        util_vent.util_vent(self,w,h)
        self.resizable(False,False)

    def frames(self):
        self.frame_Derecha = tk.Frame(self, width=350, height=350, bg=uno)
        self.frame_Derecha.place(x=623, y=125)

        self.frame_medio = tk.Frame(self, width=2, height=500, bg=uno)
        self.frame_medio.pack(side=tk.TOP, pady=50)

        self.frame_izquierda = tk.Frame(self, width=250, height=250, bg=uno)
        self.frame_izquierda.place(x=135, y=220)

    def imagenes(self):
        self.imagen_principal = tk.Label(self.frame_izquierda, image=self.imagen_fondo)
        self.imagen_principal.pack()

    def botones(self):
        self.admin = tk.Button(self, width=30, height=2, text="ADMINISTRADOR", bg=tres,fg=cuatro, command=self.administrador, font=("Segoe UI Black", 12, "bold"))
        self.admin.place(x=643, y=200)

        self.usuario = tk.Button(self, width=30, height=2, text="USUARIO", bg=tres, fg=cuatro, command=self.dashboard, font=("Segoe UI Black", 12, "bold"))
        self.usuario.place(x=643, y=340)

    def escrito(self):
        self.texto = tk.Label(self, text="Consejo Comunal Ezequiel Zamora 2",bg=dos,fg='black', font=('Exmouth', 25))
        self.texto.place(x=65, y=125)

    def administrador(self):
        login_class()

    def dashboard(self):
        dashboard_class()