import streamlit as st

def display_legendes():
    st.write("## Mythes et légendes de Rurutu")
    st.write("""
        Découvrez les histoires captivantes transmises de génération en génération :
        - **La légende du lac mystérieux**
        - **Le guerrier de Rurutu**
        - **L'origine du nom 'ETEROA'**
    """)
    st.image("eteroa/public/assets/legends.webp", caption="Les contes traditionnels de Rurutu")
