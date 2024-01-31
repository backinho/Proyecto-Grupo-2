def util_vent(ventana,aplicacion_ancho,aplicacion_largo):
    panel_ancho = ventana.winfo_screenwidth()
    panel_largo = ventana.winfo_screenheight()
    x = int((panel_ancho/2) - (aplicacion_ancho/2))
    y = int((panel_largo/2) - (aplicacion_largo/2))
    return ventana.geometry(f"{aplicacion_ancho}x{aplicacion_largo}+{x}+{y}")