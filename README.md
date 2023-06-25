# Pokémon Information Retrieval

This Python script allows you to retrieve information about Pokemon.

## Features

- Retrieve information about a Pokémon by providing its name.
- Check if a name corresponds to a valid Pokémon using the PokeAPI.
- Extract relevant data from the Pokémon's API response.
- Store the extracted data in a SQLite database table.
- Display the retrieved data in a table format.

## Requirements 

Before running the script, make sure you have the following installed:

- Python 3.x: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- `requests` library: Install using `pip install requests`
- `sqlalchemy` library: Install using `pip install sqlalchemy`
- `pandas` library: Install using `pip install pandas`

## Usage

1. Run the script by executing the following command: `python apiproject`

2. When prompted, enter the name of a Pokémon you want to retrieve information for.

3. The script will check if the entered name corresponds to a valid Pokémon. If it is valid, it will fetch the Pokémon's information using the PokeAPI.

4. The relevant data, including the Pokémon's name, height, weight, and base experience, will be displayed in a tabular format.

5. The retrieved data will be stored in a SQLite database named `data_base_name.db` in a table named `table_name`.

## Examples

1. Retrieve information for Pikachu:

   ```
   Enter a Pokémon name: Pikachu

   Name      Height    Weight    Base Experience
   --------- --------- --------- ---------------
   Pikachu   4         60        112
   ```

2. Retrieve information for a non-existent Pokémon:

   ```
   Enter a Pokémon name: NotAPokémon

   NotAPokémon is not a Pokémon.
   ```
