import os

consoles_data_path = "https://raw.githubusercontent.com/walmartdigital/de-challenge/main/data/consoles.csv"
results_data_path = "https://raw.githubusercontent.com/walmartdigital/de-challenge/main/data/result.csv"

database_location = "sqlite:///gamereviews.sqlite"

report_filename = "games_report.xlsx"
report_metrics = ['userscore', 'metascore', 'avg_score']