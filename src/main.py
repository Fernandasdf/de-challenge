# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import extractor.extractor as ext
import transformer.transformer as trf
from loader import db_conn, loader
import report

def extract():
    extractor = ext.Extract()
    extractor.get_consoles_data()
    extractor.get_results_data()

    return extractor

def transform(extractor):
    transformer = trf.Transform(extractor.df_consoles, extractor.df_results)

    transformer.to_uppercase()
    transformer.trim()
    transformer.drop_duplicates()
    transformer.set_numeric_type()
    transformer.drop_key_duplicates()
    transformer.handle_dates()
    transformer.avg_score()

    return transformer

def load(transformer):
    print("Connecting to db...")
    engine = db_conn.create_conn()
    session = db_conn.access_db(engine)

    print("Loading data...")
    ldr = loader.Load(session, transformer.df_consoles, transformer.df_results)

    ldr.load_company()
    ldr.load_console()
    ldr.load_game()
    ldr.load_console_company()
    ldr.load_game_score()

    ldr.commit()

    session.close()

def main():
    print("Extracting from source...")
    extractor = extract()

    print("Doing some data transformations...")
    transformer = transform(extractor)

    # load(transformer)

    data = transformer.df_results.merge(transformer.df_consoles, how='inner', on='console')

    print("Building report...")
    report.start(data)

    print('Done.')

if __name__ == '__main__':
    main()
