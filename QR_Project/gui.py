import tkinter as tk
from tkinter import filedialog, messagebox
from utils import generar_qr, decodificar_qr


def generar_qr_desde_gui():
    data = entry_data.get()
    if not data:
        messagebox.showwarning("Advertencia", "Por favor ingresa datos para generar el código QR")
        return

    filename = entry_filename.get() or "codigo_qr"
    filepath = generar_qr(data, filename)
    messagebox.showinfo("Éxito", f"Código QR guardado en {filepath}")


def decodificar_qr_desde_gui():
    filepath = filedialog.askopenfilename(title="Seleccionaa una imagen de código QR",
                                          filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if not filepath:
        return

    data = decodificar_qr(filepath)
    if data:
        messagebox.showinfo("Datos Decodificados", f"Datos del QR: {data}")
    else:
        messagebox.showerror("Error", "No se pudo decodificar el código QR")


app = tk.Tk()
app.title("Generador y Decodificador de QR")
app.geometry("400x200")

tk.Label(app, text="Datos para el Código QR:").pack()
entry_data = tk.Entry(app)
entry_data.pack(pady=5)

tk.Label(app, text="Nombre del archivo:").pack()
entry_filename = tk.Entry(app)
entry_filename.pack(pady=5)

tk.Button(app, text="Generar Código QR", command=generar_qr_desde_gui).pack(pady=10)
tk.Button(app, text="Decodificar Código QR", command=decodificar_qr_desde_gui).pack(pady=10)

app.mainloop()
