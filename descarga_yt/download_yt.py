import os
import tkinter as tk
from pytube import YouTube


def descargar_video():
    url = url_entry.get()
    try:
        yt = YouTube(url)
        log_text.insert(tk.END, f"Descargando video: {yt.title}...\n")
        yt.streams.get_highest_resolution().download(output_path.get())
        log_text.insert(tk.END, f"{yt.title} descarga finalizada\n")
    except Exception as e:
        log_text.insert(tk.END, f"Error al descargar el video: {e}\n")


def select_output_path():
    output_directory = tk.filedialog.askdirectory()
    output_path.set(output_directory)


# Configuración de la ventana principal
root = tk.Tk()
root.title("Descargar Video")

# Marco para el campo de entrada y botones
input_frame = tk.Frame(root)
input_frame.pack(padx=20, pady=10)

url_label = tk.Label(input_frame, text="Ingrese la URL del video:")
url_label.grid(row=0, column=0)

url_entry = tk.Entry(input_frame, width=40)
url_entry.grid(row=0, column=1)

path_label = tk.Label(input_frame, text="Directorio de salida:")
path_label.grid(row=1, column=0)

output_path = tk.StringVar()
path_entry = tk.Entry(input_frame, textvariable=output_path, width=30)
path_entry.grid(row=1, column=1)

browse_button = tk.Button(input_frame, text="Buscar", command=select_output_path)
browse_button.grid(row=1, column=2)

download_button = tk.Button(root, text="Descargar", command=descargar_video)
download_button.pack(pady=10)

# Configuración del área de registro de actividades
log_text = tk.Text(root, height=10, width=50)
log_text.pack(padx=20, pady=10)

root.mainloop()
