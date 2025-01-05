import streamlit as st
import folium
import json
from streamlit_folium import st_folium

@st.cache_data
def load_geojson(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)

def display_carte_visuelle():
    st.write("### Vue générale (avec filtre interactif à droite)")
    geojson_path = "eteroa/rurutu-data/rurutu.geojson"

    try:
        geojson_data = load_geojson(geojson_path)
    except FileNotFoundError:
        st.error("Le fichier GeoJSON est introuvable. Vérifiez le chemin.")
        return

    m = folium.Map(
        location=[-22.471705, -151.340019],  # coordonnées de RURUTU
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

    st_folium(m, height=700, width=1000)
    
    

