import pandas as pd
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode

st.title("Streamlit AG Grid Example...")
penguins_df = pd.read_csv("penguins.csv")

#note, my string columns are not filtering, that's because you have to iterate over them.


#Note, you can import JsCode and apply to gridoptions
#https://streamlit-aggrid.readthedocs.io/en/docs/GridOptionsBuilder.html
# , gridOptions = GridOptionsBuilder.from_dataframe(penguins_df).build()

gob = GridOptionsBuilder.from_dataframe(penguins_df)
for column in penguins_df.columns:
    gob.configure_column(column, filter=True)
    gob.configure_column(column, editable=True) #once I touch columns, I can't do editable at the top AgGrid level/call

gridOptions = gob.build() #do this and my editable=True fails on the AgGrid line

#response = AgGrid(penguins_df, height=500, editable=True, gridOptions=gridOptions)
response = AgGrid(penguins_df, gridOptions=gridOptions, update_mode=GridUpdateMode.MODEL_CHANGED)
df_edited = response["data"]
st.write("Edited Data Frame")
st.dataframe(df_edited)