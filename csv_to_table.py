import pandas as pd

cities = pd.read_csv("Resources/cities.csv")

cities.to_html('data.html', index=False, classes=["table", "table-stripped", "table-hover"])
