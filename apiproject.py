import requests
import sqlalchemy as db
import pandas as pd


def is_pokemon(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        return True
    else:
        return False


# Extract relevant data from pokemon_data dictionary
def info_pokemon(data):
    pokemon_info = {
        'Name': [data['name']],
        'Height': [data['height']],
        'Weight': [data['weight']],
        'Base Experience': [data['base_experience']],
    }
    return pokemon_info


def to_database(info):
    df = pd.DataFrame(info)
    engine = db.create_engine('sqlite:///data_base_name.db')
    df.to_sql('table_name', con=engine, if_exists='replace', index=False)

    with engine.connect() as connection:
        databaseText = "SELECT * FROM table_name;"
        query_result = connection.execute(db.text(databaseText)).fetchall()
        print(pd.DataFrame(query_result))
    return pd.DataFrame(query_result)


def main():
    pokemon_name = input("Enter a Pokémon name: ")
    if is_pokemon(pokemon_name):
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
        response = requests.get(url)
        pokemon_data = response.json()
        info = info_pokemon(pokemon_data)
        to_database(info)
    else:
        print(f"{pokemon_name} is not a Pokémon.")


if __name__ == "__main__":
    main()
