import os.path
import tkinter as tk
from tkinter import font
from tkinter import messagebox
from typing_extensions import Literal
import recurses.util_ventana as util_vent
import recurses.util_imagenes as util_img
from recurses.paleta_colores import *

class dashboard_class(tk.Toplevel):
    
    def __init__(self):
        super().__init__()
        self.boton_agregar = util_img.util_img(os.path.join(os.path.dirname(__file__), "datos/BotonAgregar.png"),(100, 50))
        self.boton_eliminar = util_img.util_img(os.path.join(os.path.dirname(__file__), "datos/BotonEliminar.png"),(100, 50))
        self.boton_modificar = util_img.util_img(os.path.join(os.path.dirname(__file__), "datos/BotonModificar.png"),(100, 50))
        self.boton_ver = util_img.util_img(os.path.join(os.path.dirname(__file__), "datos/BotonVer.png"),(100, 50))
        self.boton_familia = util_img.util_img(os.path.join(os.path.dirname(__file__), "datos/BotonFamilia.png"),(100, 50))
        self.boton_persona = util_img.util_img(os.path.join(os.path.dirname(__file__), "datos/BotonPersona.png"),(100, 50))
        self.boton_vivienda = util_img.util_img(os.path.join(os.path.dirname(__file__), "datos/BotonVivienda.png"),(100, 50))
        self.boton_beneficio = util_img.util_img(os.path.join(os.path.dirname(__file__), "datos/BotonBeneficio.png"),(100, 50))
        self.db_conf()
        self.paneles()
        self.botones_panel_izquierdo()
        self.botones_panel_agregar()
        self.botones_panel_eliminar()
        self.botones_panel_modificar()

    def db_conf(self):
        self.title("Inicio")
        self.configure(bg=uno)
        w, h = 1024, 600
        util_vent.util_vent(self, w, h)
        self.resizable(False,False)

    def paneles(self):
        self.panel_lateral_izquierdo = tk.Frame(self, bg=dos, width=100)
        self.panel_lateral_izquierdo.pack(side=tk.LEFT,fill='both')

        self.panel_lateral_agregar = tk.Frame(self, bg=cuatro, width=100)
        self.panel_lateral_agregar.pack(side=tk.LEFT, fill='both',padx=5)

        self.panel_lateral_agregar.pack_forget()

        self.panel_lateral_eliminar = tk.Frame(self, bg=cuatro, width=100)
        self.panel_lateral_eliminar.pack(side=tk.LEFT, fill='both', padx=5)

        self.panel_lateral_eliminar.pack_forget()

        self.panel_lateral_modificar = tk.Frame(self, bg=cuatro, width=100)
        self.panel_lateral_modificar.pack(side=tk.LEFT, fill='both', padx=5)

        self.panel_lateral_modificar.pack_forget()

        self.panel_principal_uno = tk.Frame(self, bg=dos, width=800, height=580)
        self.panel_principal_uno.place(x=214, y=10)

        self.panel_principal_uno.place_forget()

        self.panel_principal_dos = tk.Frame(self, bg=dos, width=895, height=580)
        self.panel_principal_dos.place(x=115, y=10)

        self.panel_principal_dos.place_forget()

    def botones_panel_izquierdo(self):
        self.lg_br_space = tk.Frame(self.panel_lateral_izquierdo, width=0, height=0, bg=dos)
        self.lg_br_space.pack(side=tk.TOP, pady=100)

        self.agregar = tk.Button(self.panel_lateral_izquierdo,border=0, image=self.boton_agregar, bg=dos, borderwidth=0,command=self.toggle_panel_agregar)
        self.agregar.pack(side=tk.TOP)

        self.ver = tk.Button(self.panel_lateral_izquierdo,border=0, image=self.boton_ver, bg=dos, borderwidth=0, command=self.toogle_panel_ver)
        self.ver.pack(side=tk.TOP)

        self.modificar = tk.Button(self.panel_lateral_izquierdo, border=0, image=self.boton_modificar, bg=dos, borderwidth=0, command=self.toggle_panel_modificar)
        self.modificar.pack(side=tk.TOP)

        self.eliminar = tk.Button(self.panel_lateral_izquierdo, border=0, image=self.boton_eliminar, bg=dos, borderwidth=0, command=self.toggle_panel_eliminar)
        self.eliminar.pack(side=tk.TOP)

    def botones_panel_agregar(self):
        self.br_space = tk.Frame(self.panel_lateral_agregar, width=0, height=0, bg=cuatro)
        self.br_space.pack(side=tk.TOP, pady=100)

        self.familia = tk.Button(self.panel_lateral_agregar, border=0, image=self.boton_familia, bg=dos, borderwidth=0)
        self.familia.pack(side=tk.TOP)

        self.persona = tk.Button(self.panel_lateral_agregar, border=0, image=self.boton_persona, bg=dos, borderwidth=0)
        self.persona.pack(side=tk.TOP)

        self.vivienda = tk.Button(self.panel_lateral_agregar, border=0, image=self.boton_vivienda, bg=dos, borderwidth=0)
        self.vivienda.pack(side=tk.TOP)

        self.beneficio = tk.Button(self.panel_lateral_agregar, border=0, image=self.boton_beneficio, bg=dos, borderwidth=0)
        self.beneficio.pack(side=tk.TOP)

    def botones_panel_eliminar(self):
        self.eliminar_space = tk.Frame(self.panel_lateral_eliminar, width=0, height=0, bg=cuatro)
        self.eliminar_space.pack(side=tk.TOP, pady=126)

        self.eliminar_familia = tk.Button(self.panel_lateral_eliminar, border=0, image=self.boton_familia, bg=dos, borderwidth=0)
        self.eliminar_familia.pack(side=tk.TOP)

        self.eliminar_persona = tk.Button(self.panel_lateral_eliminar, border=0, image=self.boton_persona, bg=dos, borderwidth=0)
        self.eliminar_persona.pack(side=tk.TOP)

        self.eliminar_beneficio = tk.Button(self.panel_lateral_eliminar, border=0, image=self.boton_beneficio, bg=dos, borderwidth=0)
        self.eliminar_beneficio.pack(side=tk.TOP)

    def botones_panel_modificar(self):
        self.md_space = tk.Frame(self.panel_lateral_modificar, width=0, height=0, bg=cuatro)
        self.md_space.pack(side=tk.TOP, pady=100)

        self.modificar_familia = tk.Button(self.panel_lateral_modificar, border=0, image=self.boton_familia, bg=dos, borderwidth=0)
        self.modificar_familia.pack(side=tk.TOP)

        self.modificar_persona = tk.Button(self.panel_lateral_modificar, border=0, image=self.boton_persona, bg=dos, borderwidth=0)
        self.modificar_persona.pack(side=tk.TOP)

        self.modificar_vivienda = tk.Button(self.panel_lateral_modificar, border=0, image=self.boton_vivienda, bg=dos, borderwidth=0)
        self.modificar_vivienda.pack(side=tk.TOP)

        self.modificar_beneficio = tk.Button(self.panel_lateral_modificar, border=0, image=self.boton_beneficio, bg=dos, borderwidth=0)
        self.modificar_beneficio.pack(side=tk.TOP)

    def toggle_panel_agregar(self):
        if self.panel_lateral_agregar.winfo_ismapped() is not True:
            self.panel_lateral_agregar.pack(side=tk.LEFT, fill='both')
            self.ver.configure(state=tk.DISABLED)
            self.modificar.configure(state=tk.DISABLED)
            self.eliminar.configure(state=tk.DISABLED)
            self.panel_principal_uno.place(x=214, y=10)
        if self.panel_lateral_agregar.winfo_ismapped():
            self.panel_lateral_agregar.pack_forget()
            self.ver.configure(state=tk.ACTIVE)
            self.modificar.configure(state=tk.ACTIVE)
            self.eliminar.configure(state=tk.ACTIVE)
            self.panel_principal_uno.place_forget()

    def toggle_panel_eliminar(self):
        if self.panel_lateral_eliminar.winfo_ismapped() is not True:
            self.panel_lateral_eliminar.pack(side=tk.LEFT, fill='both')
            self.agregar.configure(state=tk.DISABLED)
            self.modificar.configure(state=tk.DISABLED)
            self.ver.configure(state=tk.DISABLED)
            self.panel_principal_uno.place(x=214, y=10)
        if self.panel_lateral_eliminar.winfo_ismapped():
            self.panel_lateral_eliminar.pack_forget()
            self.agregar.configure(state=tk.ACTIVE)
            self.modificar.configure(state=tk.ACTIVE)
            self.ver.configure(state=tk.ACTIVE)
            self.panel_principal_uno.place_forget()

    def toggle_panel_modificar(self):
        if self.panel_lateral_modificar.winfo_ismapped() is not True:
            self.panel_lateral_modificar.pack(side=tk.LEFT, fill='both')
            self.agregar.configure(state=tk.DISABLED)
            self.ver.configure(state=tk.DISABLED)
            self.eliminar.configure(state=tk.DISABLED)
            self.panel_principal_uno.place(x=214, y=10)
        if self.panel_lateral_modificar.winfo_ismapped():
            self.panel_lateral_modificar.pack_forget()
            self.agregar.configure(state=tk.ACTIVE)
            self.ver.configure(state=tk.ACTIVE)
            self.eliminar.configure(state=tk.ACTIVE)
            self.panel_principal_uno.place_forget()

    def toogle_panel_ver(self):
        if self.panel_principal_dos.winfo_ismapped() is not True:
            self.panel_principal_dos.place(x=115, y=10)
            self.agregar.configure(state=tk.DISABLED)
            self.modificar.configure(state=tk.DISABLED)
            self.eliminar.configure(state=tk.DISABLED)
        if self.panel_principal_dos.winfo_ismapped():
            self.panel_principal_dos.place_forget()
            self.agregar.configure(state=tk.ACTIVE)
            self.modificar.configure(state=tk.ACTIVE)
            self.eliminar.configure(state=tk.ACTIVE)
