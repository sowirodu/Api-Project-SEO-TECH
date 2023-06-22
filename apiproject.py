import requests
import sqlalchemy as db
import pandas as pd

response = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')
pokemon_data = response.json()

# Extract relevant data from pokemon_data dictionary
pokemon_info = {
    'Name': [pokemon_data['name']],
    'Height': [pokemon_data['height']],
    'Weight': [pokemon_data['weight']],
    'Base Experience': [pokemon_data['base_experience']],
}

df = pd.DataFrame(pokemon_info)
engine = db.create_engine('sqlite:///data_base_name.db')
df.to_sql('table_name', con=engine, if_exists='replace', index=False)

with engine.connect() as connection:
   query_result = connection.execute(db.text("SELECT * FROM table_name;")).fetchall()
   print(pd.DataFrame(query_result))


