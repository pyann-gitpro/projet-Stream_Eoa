import streamlit as st
import folium
import json
from streamlit_folium import st_folium
import pandas as pd
import requests

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

# Fonction pour charger le fichier GeoJSON
@st.cache_data
def load_geojson(path):
    """
    Charge un fichier GeoJSON depuis le chemin spécifié.
    Utilise un cache pour optimiser les performances.
    """
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)

# Fonction pour récupérer les données des vents via Open-Meteo
@st.cache_data
def get_wind_data_open_meteo(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=windspeed_10m,winddirection_10m"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["hourly"]
    else:
        st.error("Impossible de récupérer les données des vents.")
        return None

# Bloc conditionnel pour chaque page
if options == "Carte visuel":
    # Page Carte visuelle
    geojson_path = "rurutu-data/rurutu.geojson"

    try:
        geojson_data = load_geojson(geojson_path)
    except FileNotFoundError:
        st.error("Le fichier GeoJSON est introuvable. Vérifiez le chemin.")
        st.stop()

    # Création de la carte
    m = folium.Map(
        location=[-22.471705, -151.340019], # coordonnées de RURUTU
        zoom_start=13,
        tiles="OpenStreetMap"
    )

    folium.GeoJson(
        geojson_data,
        name="Communes approx.",
        style_function=lambda x: {
            "color": x["properties"].get("stroke", "#000000"),
            "weight": x["properties"].get("stroke-width", 2),
            "fillColor": x["properties"].get("fill", "#ffffff"),
            "fillOpacity": x["properties"].get("fill-opacity", 0.5),
        }
    ).add_to(m)

    folium.LayerControl().add_to(m)

    # Affichage de la carte
    with st.spinner("Chargement de la carte..."):
        st.write("### Vue générale (avec filtre interactif à droite)")
        st_folium(m, height=700, width=1000)

elif options == "Découverte":
    # Page Découverte
    st.write("## Bienvenue dans la section Découverte !")
    st.write("""
        Explorez les trésors cachés de Rurutu : sa faune, sa flore et ses paysages spectaculaires.
        Ici, nous partagerons des informations fascinantes et des guides pour les aventuriers.
    """)
    st.image("public/assets/discovers.webp", caption="Paysage pittoresque de Rurutu")

elif options == "Légendes":
    # Page Légendes
    st.write("## Mythes et légendes de Rurutu")
    st.write("""
        Découvrez les histoires captivantes transmises de génération en génération :
        - **La légende du lac mystérieux**
        - **Le guerrier de Rurutu**
        - **L'origine du nom 'ETEROA'**
    """)
    st.image("public/assets/legends.webp", caption="Les contes traditionnels de Rurutu")

elif options == "Actualités":
    # Page Actualités
    st.write("## Actualités de Rurutu")
    st.write("""
        Restez informé des derniers événements, festivals et initiatives communautaires.
        Vous trouverez ici des nouvelles fraîches et pertinentes sur l'île.
    """)
    st.markdown("""
        - 🎉 **Festival culturel de Rurutu** - Du 15 au 20 Janvier 2025.
        - 🐋 **Observation des baleines** - Période optimale : Mai à Novembre.
        - 🌱 **Initiative écologique** : Plantation de 1000 arbres.
    """)

elif options == "Statistiques":
    # Page Statistiques
    st.write("## Statistiques de l'île")
    st.write("""
        Découvrez les données fascinantes sur Rurutu :
        - Population : 2,500 habitants
        - Superficie : 32 km²
        - Points d'intérêt : 10 sites historiques
    """)

    # Exemple de graphique interactif
    data = pd.DataFrame({
        "Année": [2021, 2022, 2023, 2024],
        "Touristes": [1500, 1800, 2000, 2500]
    })

    st.line_chart(data, x="Année", y="Touristes", use_container_width=True)

    st.write("### Évolution de la population")
    population_data = pd.DataFrame({
        "Année": [2000, 2010, 2020],
        "Population": [2300, 2500, 2600]
    })
    st.bar_chart(population_data, x="Année", y="Population", use_container_width=True)

elif options == "Carte des vents":
    # Page Carte des vents
    latitude = -22.471705
    longitude = -151.340019

    # Récupération des données des vents
    wind_data = get_wind_data_open_meteo(latitude, longitude)

    if wind_data:
        st.write("## Carte des vents")

        # Extraction des données
        wind_speed = wind_data["windspeed_10m"][0]
        wind_direction = wind_data["winddirection_10m"][0]

        st.write(f"### Direction : {wind_direction}° | Vitesse : {wind_speed} m/s")

        # Création de la carte avec plusieurs types de fonds
        m = folium.Map(location=[latitude, longitude], zoom_start=10)

        # Ajout des différents types de tuile
        folium.TileLayer(
            tiles="https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png",
            attr="© CartoDB Dark Matter, OpenStreetMap contributors",
            name="CartoDB Dark"
        ).add_to(m)

        # Ajout d'un marqueur avec les informations sur les vents
        folium.Marker(
            [latitude, longitude],
            popup=f"Direction : {wind_direction}°<br>Vitesse : {wind_speed} m/s",
            icon=folium.Icon(color="blue", icon="info-sign"),
        ).add_to(m)

        # Ajout du contrôle des couches
        folium.LayerControl().add_to(m)

        # Affichage de la carte
        st_folium(m, height=500, width=700)
    else:
        st.warning("Les données des vents ne sont pas disponibles pour le moment.")



# Footer global
st.markdown("---")
st.markdown("**© 2025 ETEROA - Tous droits réservés.**")
