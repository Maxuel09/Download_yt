import os
import streamlit as st
from pytube import YouTube

# import tkinter as tk


def descargar_video(url, output_path):
    try:
        yt = YouTube(url)
        st.header(f"Descargando video: {yt.title}")
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path)
        st.success("¡Descarga completada!")
    except Exception as e:
        st.error(f"Error: {str(e)}")


def main():
    st.title("Descargador de Videos de YouTube")
    st.image("conexionyt.jpg")

    # Entrada de la URL del video
    url = st.text_input("Ingrese la URL del video de YouTube:")

    # Selección del directorio de salida
    output_path = st.text_input("Ingrese el directorio de salida ", "/users/nameFile")

    if st.button("Descargar"):
        if url:
            # Crear directorio de salida si no existe
            os.makedirs(output_path, exist_ok=True)
            descargar_video(url, output_path)


if __name__ == "__main__":
    main()
