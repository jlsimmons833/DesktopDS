from ydata_profiling import ProfileReport
import pandas as pd

train_df = pd.read_csv("trainmap.csv")
train_report = ProfileReport(train_df, title="Train")

test_df = pd.read_csv("testmap.csv")
test_report = ProfileReport(test_df, title="Test")

comparison_report = train_report.compare(test_report)
comparison_report.to_file("comparison.html")