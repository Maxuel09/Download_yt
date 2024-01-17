# descaga_videos_yt


Un codigo con una interfaz sencilla para descarga videos de [Youtube](https://www.youtube.com/) 

## Uso

```mermain
sequenceDiagram
   user ->>+ input: https://www.youtube.com/
   input ->>+ pytube: Download
   pytube ->>+ rutaCarpeta: Completado
```

## Librerias 
- [Streamlit](https://streamlit.io/)
- [pytube](https://pypi.org/project/pytube3/)


```python
import os  #menejo de carpetas y rutas
import streamlit as st
from pytube import YouTube
```