import pandas as pd
from ydata_profiling import ProfileReport

# Make sure this CSV file is in the same folder as the script
df = pd.read_csv("your_data.csv")

# Generate the profiling report
profile = ProfileReport(df, title="My Data Report", explorative=True)

# Save the report as an HTML file
profile.to_file("report.html")
