import pandas as pd
import config as cfg

def start(data):
    with pd.ExcelWriter(cfg.report_filename) as writer:
        for metric in cfg.report_metrics:
            make_report(writer, data, by=metric, groupby=['company','console'])
            make_report(writer, data, by=metric, level='all')

def make_report(writer, df, by, groupby=None, level='console'):
    if level=='console':
        rep = df.groupby(groupby)['name', by, 'release_dt'].apply(lambda x: x.nlargest(10, columns=by)).copy()
        rep.to_excel(writer, sheet_name=f"top10{by}_{''.join(groupby)}")

        rep = df.groupby(groupby)['name', by, 'release_dt'].apply(lambda x: x.nsmallest(10, columns=by)).copy()
        rep.to_excel(writer, sheet_name=f"worst10{by}_{''.join(groupby)}")
    elif level=='all':
        rep = df[['company', 'console', 'name', by, 'release_dt']].nlargest(10, by).copy()
        rep.to_excel(writer, sheet_name=f"top10{by}_allconsoles")

        rep = df[['company', 'console', 'name', by, 'release_dt']].nsmallest(10, by).copy()
        rep.to_excel(writer, sheet_name=f"worst10{by}_allconsoles")
