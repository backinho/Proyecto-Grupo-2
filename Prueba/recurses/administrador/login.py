import os.path
import tkinter as tk
from tkinter import font
from tkinter import messagebox
from typing_extensions import Literal
import recurses.util_ventana as util_vent
import recurses.util_imagenes as util_img
from recurses.paleta_colores import *
from recurses.dashboard.dashboard import dashboard_class
import ast

class login_class(tk.Toplevel):

    def __init__(self):
        super().__init__()
        self.imagen_fondo = util_img.util_img(os.path.join(os.path.dirname(__file__), "datos/Fondo.png"), (250, 250))
        self.login_conf()
        self.frames()
        self.imagenes()
        self.login_ctrl()
        self.escrito()
        self.botones()

    def login_conf(self):
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
        self.iniciar = tk.Button(self, width=30, height=2, text="INICIAR", bg=tres,fg=cuatro, font=("Segoe UI Black", 12, "bold"), command=self.login)
        self.iniciar.place(x=643, y=330)

    def escrito(self):
        self.texto = tk.Label(self, text="Consejo Comunal Ezequiel Zamora 2",bg=dos,fg='black', font=('Exmouth', 25))
        self.texto.place(x=65, y=125)

    def login_ctrl(self):
        self.usuario = tk.Label(self, text="USUARIO: ", width=9, bg=uno,fg=cuatro,font=("Segoe UI Black", 12,))
        self.usuario.place(x=643, y=230)

        self.usuario_entry = tk.Entry(self, border=0)
        self.usuario_entry.configure(fg=cinco, font=("Segoe UI Black", 12,), bg=uno, width=15)
        self.usuario_entry.place(x=780, y=232)

        self.contraseña = tk.Label(self, text="CONTRASEÑA: ", width=12, bg=uno, fg=cuatro, font=("Segoe UI Black", 12,))
        self.contraseña.place(x=643, y=280)

        self.contraseña_entry = tk.Entry(self, border=0)
        self.contraseña_entry.configure(fg=cinco, font=("Segoe UI Black", 12,), bg=uno, width=15)
        self.contraseña_entry.place(x=780, y=282)


    def signal(self):
        dashboard_class()

    def login(self):
        usuario = self.usuario_entry.get()
        contraseña = self.contraseña_entry.get()

        file = open('documento.txt', 'r')
        d = file.read()
        r = ast.literal_eval(d)
        file.close()

        if usuario in r.keys() and contraseña == r[usuario]:
            self.signal()
            self.destroy()

        elif usuario != r.keys() or contraseña != r[usuario]:
            messagebox.showerror('Error', 'Error en el usuario o contraseña')
            self.destroy()