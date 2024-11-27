# Marvel Count

This is a Python project that calculates how often Marvel characters appear in comics using data from the Marvel API. The scripts fetch, process, and analyze character data, saving the results in JSON files for easy use.

---

## Features

- Fetch data about all Marvel characters from the "get/v1/public/characters".
- Save the data to a JSON file for offline access without fetching the data again.
- Extract counts values from `comics` in fetched data to show how often each character appears in Marvel comics.
- Stored final results as a JSON file for easy reference

---

## Requirements

To run this project, you need:

- Python 3.12 or higher
- A [Marvel API key](https://developer.marvel.com/)

---

## Usage

The project is organised into several scripts to handle specific tasks:

#### 1. API Authentication

To use the Marvel API, you need to generate your own public and private keys from the [Marvel Developer Portal](https://developer.marvel.com/).

Update the `public_key` and `private_key` in `marvel_character_count.py` with your keys:
```python
public_key = "your_public_key_here"
private_key = "your_private_key_here"
```

#### 2. Fetch Marvel Characters

Run the `main.py` script to fetch data about Marvel characters from the API and save it to a JSON file:
```bash
python src/main.py
```

In details:

- The scripts fetch Marvel character data via 'get/v1/public/characters'
- Fetched data is stored as `marvel_characters.json` for offline access or debugging
- Appearance count values are extracted from `comics` in API responses, which list containing comics that feature each character
- Final results are stored as `result.json` for reference.

---

## Project Structure
```
Marvel_count/
|├── .venv/                         # Virtual environment directory
|├── src/
|   |├── main.py            
|   |├── marvel_character_count.py  # class to fetch and extract character appearance frequency
|├── marvel_characters.json         # Fetched character data (generated)
|├── result.json                    # Results output (generated)
|├── README.md
|├── .gitignore
```

---

## Example Output

Here is an example of the output in `result.json`:
```json
{
  "Spider-Man": 1534,
  "Iron Man": 1450,
  "Hulk": 1203,
  "Thor": 1102,
  "Captain America": 1034
}
```

---


