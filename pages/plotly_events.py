import pandas as pd
import plotly.express as px
import streamlit as st
from streamlit_plotly_events import plotly_events

st.title("Streamlit Plotly Events Example...")
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