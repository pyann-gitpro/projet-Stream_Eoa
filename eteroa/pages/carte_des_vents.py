import streamlit as st
import folium
from streamlit_folium import st_folium
import requests

@st.cache_data
def get_wind_data_open_meteo(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=windspeed_10m,winddirection_10m"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["hourly"]
    else:
        return None

def display_carte_des_vents():
    latitude = -22.471705
    longitude = -151.340019

    wind_data = get_wind_data_open_meteo(latitude, longitude)

    if wind_data:
        st.write("## Carte des vents")
        wind_speed = wind_data["windspeed_10m"][0]
        wind_direction = wind_data["winddirection_10m"][0]

        st.write(f"### Direction : {wind_direction}° | Vitesse : {wind_speed} m/s")

        m = folium.Map(location=[latitude, longitude], zoom_start=10)

        folium.TileLayer(
            tiles="https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png",
            attr="© CartoDB Dark Matter, OpenStreetMap contributors",
            name="CartoDB Dark"
        ).add_to(m)

        folium.Marker(
            [latitude, longitude],
            popup=f"Direction : {wind_direction}°<br>Vitesse : {wind_speed} m/s",
            icon=folium.Icon(color="blue", icon="info-sign"),
        ).add_to(m)

        folium.LayerControl().add_to(m)

        st_folium(m, height=500, width=700)
    else:
        st.warning("Les données des vents ne sont pas disponibles pour le moment.")
