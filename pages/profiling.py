import pandas as pd
import pandas_profiling
import streamlit as st
from ydata_profiling import ProfileReport

from streamlit_pandas_profiling import st_profile_report

# see
# https://okld-gallery.streamlit.app/?p=pandas-profiling

df = pd.read_csv("penguins.csv")
report = ProfileReport(df, title="My data", explorative=True)
pr = df.profile_report()

st_profile_report(report)