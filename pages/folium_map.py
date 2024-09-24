import folium
import pandas as pd
import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_folium import st_folium


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.title("SF Trees Map Using Folium")

lottie_penguin = load_lottieurl("https://lottie.host/e36ca507-eef1-49c2-8950-f982c1ad7544/sSqpEfIPkh.json")
st_lottie(lottie_penguin,height=200,speed=2)

trees_df = pd.read_csv("trees.csv")
trees_df = trees_df.dropna(subset=["longitude", "latitude"])
trees_df = trees_df.head(n=100)

lat_avg = trees_df["latitude"].mean()
lon_avg = trees_df["longitude"].mean()
m = folium.Map(location=[lat_avg, lon_avg], zoom_start=12)

for _, row in trees_df.iterrows():
    folium.Marker(
        [row["latitude"], row["longitude"]],
    ).add_to(m)

events = st_folium(m)
st.write(events)
#st_folium(m)

