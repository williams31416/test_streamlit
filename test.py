import datetime
import time
import pandas as pd
import streamlit as st
from PIL import Image

# Permite definir que la función este en cache.
@st.cache
def run_fxn(n: int) -> list:
    return range(n)

def main():
    """Generación de la webapp con streamlit"""
    # Definir título
    st.title("Título: Tutorial de Streamlit")
    
    # Definir Header/Subheader
    st.header("Este es un header")
    st.subheader("Este es un subheader")
    
    # Definir un Texto
    st.text("Texto: Hola Streamlit")
    
    # Definición de Markdown
    st.markdown("# Este es un markdown h1 \n ## Este es un h2 \n ### Este es un h3")
    
    # Colores de Mensajes
    st.header("Colores de texto y mensajes de error")
    st.success("Successful")
    st.info("Información!")
    st.warning("warning")
    st.error("Error")
    st.exception("NameError('no está definido')")
    
    st.header("Obtener información de ayuda de Python")
    st.help(range)
    
    st.header("Widgets:")    
    # Checkbox
    st.subheader("Checkbox")
    if st.checkbox("Show/Hide"):
        st.text("Mostrar u ocultar Widget")
    
    # Radio Buttons
    st.subheader("Radio buttons")
    status = st.radio("Cual es su estatus", ("Activo", "Inactivo"))
    if status == "Activo":
        st.success("Estas activo")
    else:
        st.warning("Inactivo")
    
    # SelectBox
    st.subheader("SelectBox")
    occupation = st.selectbox(
        "Tu Ocupación", ["Programador", "Cientifico de datos", "Doctor", "Emprendedor"]
    )
    st.write("Opción seleccionada:", occupation)
    
    # MultiSelect
    st.subheader("MultiSelect")
    location = st.multiselect(
        "Donde trabajas?",
        ("Londres", "Nueva York", "Accra", "Kiev", "Nepal", "Buenos Aires", "Caracas"),
    )
    st.write("Seleccionó:", len(location), "locaciones")
    
    # Slider
    st.subheader("Slider")
    level = st.slider("Cual es tu nivel?", 1, 5)
    st.write("Nivel:", level)
    
    # Buttons
    st.subheader("Buttons")
    if st.button("Acerca"):
        st.text("Streamlit es Cool")
    else:
        st.text("")
        
    st.header("Como recibir una entrada y procesarla con streamlit?")
    # Recibir texto
    st.subheader("Recibiendo texto")
    firstname = st.text_input("Escriba su nombre:")
    if st.button("Aceptar"):
        result = firstname.title()
        st.success(result)
    
    # Text Area
    st.subheader("Área de texto")
    message = st.text_area("Escriba un mensaje")
    if st.button("Aceptar "):
        result = message.title()
        st.success(result)
    
    # Date Input
    st.subheader("Entrada de fecha")
    today = st.date_input("Hoy es", datetime.datetime.now())
    st.text(f"{today}")
    
    # Time
    st.subheader("Entrada de tiempo")
    the_time = st.time_input("La hora es:", datetime.time())
    st.text(f"{the_time}")
    
    # Images
    st.header("Trabajar con archivos de imágenes, audio o vídeos")
    st.subheader("Archivo de imagen")
    img = Image.open("robot_kuka.png")
    st.image(img, width = 500, caption = "Robot Kuka")
    
    # Videos
    st.subheader("Archivo de vídeo")
    vid_file = open("POD_explotado.mp4", "rb").read()
    # vid_bytes = vid_file.read()
    st.video(vid_file)
    
    # Writing Text/Super Fxn
    st.header("Otras opciones que permite la función write")
    st.subheader("Texto con write")
    st.write("Texto con write")
    st.write(range(10))
    
    st.header("Desplegando código puro y json")
    st.subheader("Código puro")
    st.code("import numpy as np")
    with st.echo():
        df = pd.DataFrame()
        
    st.subheader("Desplegando json")
    st.text("Mostrando JSON")
    st.json({"nombre": "Jhon", "apellido": "Doe", "genero": "masculino"})
    
    # Examples of graphs
    st.header("Mostrar barra de progreso, spinner y balloons")
    st.subheader("Barra de progreso")
    my_bar = st.progress(0)
    for p in range(10):
        my_bar.progress(p + 1)
    st.subheader("Spinner")
    with st.spinner("Espere .."):
        time.sleep(5)
        st.success("Finalizó!")
    # Balloons
    st.subheader("Balloons")
    st.balloons()
    
    # Data Science
    st.header("Trabajando con data science")
    df = pd.read_csv("example.csv", index_col=0)
    st.subheader("Dataframe")
    st.dataframe(df)
    st.subheader("Tabla")
    st.table(df.head())
    st.subheader("Gráfica")
    st.line_chart((df.head(5)))
    
    # Mostrar barra lateral
    st.sidebar.header("Acerca")
    st.sidebar.text("Probando streamlit ")
    
    # Funciones
    st.header("Trabajando con funciones")
    st.write(list(run_fxn(10)))
    
    # Mapa del mundo
    st.map()
    
if __name__ == "__main__":
    main()
