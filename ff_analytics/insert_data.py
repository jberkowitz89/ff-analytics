import pandas as pd
from sqlalchemy import create_engine

# Define the database connection parameters
db_params = {
    'host': '127.0.0.1',
    'database': 'ff_analytics',
    'user': 'jberkowitz',
    'password': 'password'
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
