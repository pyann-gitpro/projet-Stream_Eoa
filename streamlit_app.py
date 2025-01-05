#######################
# Import libraries
import streamlit as st
from eteroa.pages import carte_visuelle, decouverte, legendes, actualites, statistiques, carte_des_vents

#######################
# Page configuration
st.set_page_config(
    page_title="ETEROA, l'île de Rurutu",
    layout="wide",
    initial_sidebar_state="auto"
)

st.title("Découverte de l'île, légendes et mythes")

#######################
# Sidebar logo & navigation
with st.sidebar:
    st.image("eteroa/public/assets/logo_grayscale.png", width=70)
    st.markdown("**ETEROA, l'île de Rurutu**")
    st.markdown("---")
    st.markdown("### Menu")
    options = st.radio(
        "Changez pour découvrir :",
        ("🌍 Carte visuel", "🌟 Découverte", "📜 Légendes", "📰 Actualités", "📊 Statistiques", "🌬️ Carte des vents")
    )
    st.markdown("---")

#######################
# Pages navigation
if options == "🌍 Carte visuel":
    carte_visuelle.display_carte_visuelle()
elif options == "🌟 Découverte":
    decouverte.display_decouverte()
elif options == "📜 Légendes":
    legendes.display_legendes()
elif options == "📰 Actualités":
    actualites.display_actualites()
elif options == "📊 Statistiques":
    statistiques.display_statistiques()
elif options == "🌬️ Carte des vents":
    carte_des_vents.display_carte_des_vents()

#######################
# Footer GLOBAL
st.markdown("---")
st.markdown("**© 2025 ETEROA - Tous droits réservés.**")
