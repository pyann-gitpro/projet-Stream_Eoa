import streamlit as st
import pandas as pd

def display_statistiques():
    st.write("## Statistiques de l'île")
    st.write("""
        Découvrez les données fascinantes sur Rurutu :
        - Population : 2,500 habitants
        - Superficie : 32 km²
        - Points d'intérêt : 10 sites historiques
    """)

    # Exemple de graphique interactif : Touristes
    data = pd.DataFrame({
        "Année": [2021, 2022, 2023, 2024],
        "Touristes": [1500, 1800, 2000, 2500]
    })

    st.write("### Évolution des touristes")
    st.line_chart(data, x="Année", y="Touristes", use_container_width=True)

    # Exemple de graphique interactif : Population
    population_data = pd.DataFrame({
        "Année": [2000, 2010, 2020],
        "Population": [2300, 2500, 2600]
    })

    st.write("### Évolution de la population")
    st.bar_chart(population_data, x="Année", y="Population", use_container_width=True)
