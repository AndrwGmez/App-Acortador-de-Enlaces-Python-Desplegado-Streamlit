import streamlit as st
import pyshorteners

st.title("Acortar Enlaces")
st.write("Ingrese el enlace a acortar por favor")


url = st.text_input("Introduce el enlace que desea acortar:")


if st.button("Acortar"):
    if url:
        s = pyshorteners.Shortener()
        try:
            # Acortar el enlace
            short_url = s.tinyurl.short(url)
            st.success("Enlace acortado con éxito!")
            st.write("Enlace acortado:", short_url)
        except Exception as e:
            st.error("Error al acortar el enlace. Asegúrate de que el enlace es válido.")
    else:
        st.error("Por favor, introduce un enlace válido.")


