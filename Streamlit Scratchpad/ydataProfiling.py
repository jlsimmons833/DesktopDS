import numpy as np
import pandas as pd
from ydata_profiling import ProfileReport
import streamlit as st
import streamlit_pandas_profiling
from streamlit_pandas_profiling import st_profile_report
import ipywidgets as widgets

df = pd.DataFrame(np.random.rand(100, 5), columns=["a", "b", "c", "d", "e"])

profile = ProfileReport(df, title="Profiling Report")

st.dataframe(profile.to_widgets())