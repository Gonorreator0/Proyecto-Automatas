try:
    import ttkbootstrap as ttk
    from ttkbootstrap.constants import *
    from tkinter import font  # Importar font desde tkinter
    usando_ttkbootstrap = True
except ImportError:
    import tkinter as tk
    from tkinter import font, ttk  # Importar font y ttk desde tkinter
    usando_ttkbootstrap = False

from automata import es_balanceada

def verificar_cadena():
    cadena = entrada.get()
    cadena_filtrada = "".join([c for c in cadena if c in "()"])
    
    if not cadena_filtrada:
        resultado_label.config(text="La cadena no contiene paréntesis para verificar.", style="danger.TLabel")
    else:
        es_bal = es_balanceada(cadena_filtrada)
        resultado_label.config(
            text=f"La cadena '{cadena}' está balanceada" if es_bal else f"La cadena '{cadena}' no está balanceada",
            style="success.TLabel" if es_bal else "danger.TLabel"
        )

# Configuración de la ventana principal
if usando_ttkbootstrap:
    ventana = ttk.Window(themename="superhero")
else:
    ventana = tk.Tk()

# Configuración general de la ventana
ventana.title("Paréntesis Balanceados")
ventana.geometry("700x700")  # Tamaño más grande
ventana.configure(bg="#fcf8e8")  # Fondo beige claro más suave

# Fuentes personalizadas
fuente_titulo = font.Font(family="Times New Roman", size=28, weight="bold")  # Fuente más formal
fuente_texto = font.Font(family="Times New Roman", size=18)

# Título
titulo = ttk.Label(
    ventana, text="Verificador de Paréntesis Balanceados", 
    font=fuente_titulo, bootstyle="primary" if usando_ttkbootstrap else None, background="#fcf8e8", foreground="#333"
)
titulo.pack(pady=30)

# Etiqueta y campo de entrada
etiqueta = ttk.Label(
    ventana, text="Introduce una cadena:", font=fuente_texto, background="#fcf8e8", foreground="#333"
)
etiqueta.pack(pady=10)

# Caja de texto con borde personalizado y texto visible
entrada = ttk.Entry(ventana, font=fuente_texto, justify="center", width=40, bootstyle="default")
entrada.configure(style="Custom.TEntry")  # Estilo personalizado
entrada.pack(pady=10)

# Botón de verificación con borde visible
verificar_btn = ttk.Button(
    ventana, text="Verificar", command=verificar_cadena, 
    bootstyle="success", width=20
)
verificar_btn.configure(style="Custom.TButton")  # Estilo personalizado
verificar_btn.pack(pady=20)

# Etiqueta de resultado
resultado_label = ttk.Label(ventana, text="", font=fuente_texto, background="#fcf8e8", foreground="#333")
resultado_label.pack(pady=30)

# Descripción del proyecto
descripcion_label = ttk.Label(
    ventana, text="¿Qué es un Paréntesis Balanceado?\n\n"
                  "Un paréntesis balanceado ocurre cuando cada paréntesis abierto "
                  "tiene su correspondiente paréntesis de cierre y están correctamente "
                  "anidados en una cadena. Este verificador analiza cadenas para determinar "
                  "si los paréntesis cumplen estas condiciones.\n\n"
                  "Esta herramienta es útil para programadores y desarrolladores, "
                  "especialmente en lenguajes de programación que dependen de la estructura "
                  "correcta de paréntesis, como expresiones matemáticas o código fuente.",
    font=fuente_texto, wraplength=600, justify="left", background="#fcf8e8", foreground="#333"
)
descripcion_label.pack(pady=20)

# Estilos personalizados para entrada y botón
estilo = ttk.Style()
estilo.configure(
    "Custom.TEntry",
    borderwidth=3,  # Borde más grueso
    relief="solid",  # Borde sólido
    padding=5,       # Espaciado interno
    fieldbackground="#ffffff",  # Fondo blanco
    foreground="#000000",  # Texto negro (para que sea visible)
    bordercolor="#333"  # Color del borde
)
estilo.configure(
    "Custom.TButton",
    borderwidth=3,  # Borde más grueso
    relief="solid",  # Borde sólido
    padding=5,       # Espaciado interno
    background="#4CAF50",  # Fondo del botón
    foreground="#fff",     # Color del texto
    bordercolor="#333"     # Color del borde
)

ventana.mainloop()
