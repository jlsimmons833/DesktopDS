import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
from ydata_profiling import ProfileReport


train_df = pd.read_csv("trainmap.csv")
train_report = ProfileReport(train_df, title="Train")

test_df = pd.read_csv("testmap.csv")
test_report = ProfileReport(test_df, title="Test")

comparison_report = train_report.compare(test_report)
comparison_report.to_file("comparison.html")

#comparison_report.to_widgets()
st_profile_report(comparison_report)
