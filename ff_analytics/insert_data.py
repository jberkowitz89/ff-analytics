import pandas as pd
from sqlalchemy import create_engine
from constants import PG_PROD_HOST, PG_PROD_DATABASE, PG_PROD_USER, PG_PROD_PASSWORD

# Define the database connection parameters
db_params = {
    'host': PG_PROD_HOST,
    'database': PG_PROD_DATABASE,
    'user': PG_PROD_USER,
    'password': PG_PROD_PASSWORD
}

engine = create_engine(f'postgresql://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}/{db_params["database"]}')

files = {'box_scores': 'data/box_scores.csv',
         'settings': 'data/settings.csv',
         'matchups': 'data/matchups.csv',
         'players': 'data/players.csv',
         'draft': 'data/draft.csv',
         'teams': 'data/teams.csv',
         'box_players': 'data/box_players.csv'}

if __name__ == '__main__':
    for table_name, file_name in files.items():
        df = pd.read_csv(file_name)
        df.to_sql(table_name, engine, if_exists='replace', index=False, schema='raw')
