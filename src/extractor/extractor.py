import pandas as pd
import config as cfg

class Extract:

    def __init__(self):
        self.df_consoles = pd.DataFrame()
        self.df_results = pd.DataFrame()

    def get_consoles_data(self):
        self.df_consoles = pd.read_csv(cfg.consoles_data_path)

    def get_results_data(self):
        self.df_results = pd.read_csv(cfg.results_data_path)
