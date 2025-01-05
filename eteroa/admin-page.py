import streamlit as st
from pages import carte_visuelle, decouverte, legendes, actualites, statistiques, carte_des_vents

# Configuration de la page Streamlit
st.set_page_config(
    page_title="ETEROA, l'île de Rurutu",
    layout="wide",
    initial_sidebar_state="auto"
)

st.title("Découverte de l'île, légendes et mythes")

# Barre latérale avec logo et navigation
with st.sidebar:
    st.image("public/assets/logo_grayscale.png", width=70)
    st.markdown("**ETEROA, l'île de Rurutu**")
    st.markdown("---")
    st.markdown("### Menu")
    options = st.radio(
        "Changez pour découvrir :",
        ("Carte visuel", "Découverte", "Légendes", "Actualités", "Statistiques", "Carte des vents")
    )
    st.markdown("---")

# Navigation vers les pages
if options == "Carte visuel":
    carte_visuelle.display_carte_visuelle()
elif options == "Découverte":
    decouverte.display_decouverte()
elif options == "Légendes":
    legendes.display_legendes()
elif options == "Actualités":
    actualites.display_actualites()
elif options == "Statistiques":
    statistiques.display_statistiques()
elif options == "Carte des vents":
    carte_des_vents.display_carte_des_vents()

# Footer global
st.markdown("---")
st.markdown("**© 2025 ETEROA - Tous droits réservés.**")
