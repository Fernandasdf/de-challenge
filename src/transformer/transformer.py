import pandas as pd
import numpy as np
from datetime import datetime

class Transform():

    def __init__(self, df_consoles, df_results):
        self.df_consoles = df_consoles
        self.df_results = df_results

    def drop_duplicates(self):
        self.df_consoles.drop_duplicates(inplace=True)
        self.df_results.drop_duplicates(inplace=True)

    def drop_key_duplicates(self):
        dups = self.df_results[self.df_results.duplicated(subset=['name', 'console'], keep=False)]
        ix = dups[self.df_results[self.df_results.duplicated(subset=['name', 'console'], keep=False)].isna().any(axis=1)].index
        indices = self.df_results.index.difference(ix)
        indx = pd.IndexSlice[indices.values]
        self.df_results = self.df_results.iloc[indx]


    def set_numeric_type(self):
        self.df_results[['metascore','userscore']] = self.df_results[['metascore','userscore']].apply(pd.to_numeric, errors='coerce')
        self.df_results[['userscore']] = self.df_results[['userscore']].apply(lambda x: (x * 10))

        # self.df_results.fillna(-1, inplace=True)

    def handle_dates(self):
        self.df_results['release_dt'] = pd.to_datetime(self.df_results['date'], format="%b %d, %Y", errors='coerce')

    def to_uppercase(self):
        self.df_results = self.df_results.apply(lambda x: x.astype(str).str.upper())
        self.df_consoles = self.df_consoles.apply(lambda x: x.astype(str).str.upper())

    def trim(self):
        self.df_results = self.df_results.apply(lambda x: x.astype(str).str.strip())
        self.df_consoles = self.df_consoles.apply(lambda x: x.astype(str).str.strip())

    def avg_score(self):
        self.df_results['avg_score'] = self.df_results[['metascore', 'userscore']].mean(numeric_only=True, axis=1)