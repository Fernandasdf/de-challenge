from loader.data_model import Company, Console, Game, GameScore, ConsoleCompany
from sqlalchemy.exc import IntegrityError

class Load:
    def __init__(self, session, df_consoles, df_results):
        self.session = session
        self.df_consoles = df_consoles
        self.df_results = df_results

    def load_company(self):
        for company_ in list(self.df_consoles['company'].unique()):
            company = Company(company_name=company_)
            self.session.add(company)

    def load_console(self):
        for console_ in list(self.df_consoles['console'].unique()):
            console = Console(console_name=console_)
            self.session.add(console)

    def load_game(self):
        for game_ in list(self.df_results['name'].unique()):
            game = Game(game_name=game_)
            self.session.add(game)

    def load_console_company(self):
        for row in self.df_consoles.to_dict(orient='records'):
            try:
                company_id = self.session.query(Company).filter(Company.company_name==row['company']).first().id
                console_id = self.session.query(Console).filter(Console.console_name==row['console']).first().id
                console_company = ConsoleCompany(company_id=company_id, console_id=console_id)
                self.session.add(console_company)
            except IntegrityError:
                self.session.rollback()

    def load_game_score(self):
        for row in self.df_results.to_dict(orient='records'):
            try:
                game_id = self.session.query(Game).filter(Game.game_name==row['name']).first().id
                console_id = self.session.query(Console).filter(Console.console_name==row['console']).first().id
                game_score = GameScore(console_id=console_id, game_id=game_id, release_dt=row['release_dt'], metascore=row['metascore'], userscore=row['userscore'])
                self.session.add(game_score)
            except IntegrityError:
                self.session.rollback()

    def commit(self):
        self.session.commit()