import pandas as pd
import plotly.express as px
import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_plotly_events import plotly_events

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#lottie_penguin = load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_lntyk83o.json")
#have to sign in and create an asset link for your image
lottie_penguin = load_lottieurl("https://lottie.host/e36ca507-eef1-49c2-8950-f982c1ad7544/sSqpEfIPkh.json")

st_lottie(lottie_penguin,height=200,speed=2)

st.title("Streamlit Plotly Events and Lottie Example...")
df = pd.read_csv("penguins.csv")

#didn't fix colors
#df.dropna(inplace=True)

fig = px.scatter(df, x="bill_length_mm", y="bill_depth_mm", color="island")
selected_point = plotly_events(fig, click_event=True)
if len(selected_point) == 0:
    st.stop()

selected_x_value = selected_point[0]['x']
selected_y_value = selected_point[0]['y']

df_selected = df[
    (df["bill_length_mm"] == selected_x_value)
    & (df["bill_depth_mm"] == selected_y_value)
]

st.write("Data for Selected Point:")
st.write(df_selected)
#st.plotly_chart(fig)
#PLOTLY EVENTS ISN'T HANDLING THE COLOR :(
#ah...could update the component... https://github.com/null-jones/streamlit-plotly-events/blob/master/src/streamlit_plotly_events/frontend/src/StreamlitPlotlyEventsComponent.tsx

#fig.update_layout(color="species")
#plotly_events(fig)

st.write(df.head(10)) #is my color issue due to nulls?