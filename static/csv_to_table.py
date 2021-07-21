import pandas as pd

cities = pd.read_csv("Ressources/cities.csv")

cities.to_html('data.html', index=False, classes=["table", "table-stripped"])
