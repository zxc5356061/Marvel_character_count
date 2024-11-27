# Marvel Count

This is a Python project that helps find out how often Marvel characters appear in comics. It uses the Marvel API to fetch data, saves it in a file, and lets you analyze it to see which characters appear most often.

---

## What It Does
- Gets data about Marvel characters from the [Marvel API](https://developer.marvel.com/).
- Saves the character data in a json file so you can use it later without fetching again.
- Extract the counts from fetch data to see how many comics each character appears in.

---

## What You Need

To use this project, you need:

- Python 3.12 or newer.
- A [Marvel API key](https://developer.marvel.com/).

---

## What the Project Looks Like
```
Marvel_count/
|├── .venv/                 # Virtual environment folder
|├── src/
|   |├── main.py            # Main file (if needed)
|   |├── get_characters.py  # Script to fetch data
|   |├── count_appearance.py # Script to count appearances
|   |├── marvel_character_count.py # Core logic and main class
|   |├── marvel_characters.json  # File with saved character data
|├── requirements.txt       # List of Python packages needed
|├── README.md              # Instructions and info about the project
```

---

## Example Results

Here’s an example of what the results might look like:

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

## How to Get Your API Keys
To use the Marvel API, you need to sign up at the [Marvel Developer Portal](https://developer.marvel.com/) and get your public and private keys.

Add your keys to the `MarvelCharacterCount` class in `marvel_character_count.py`:
```python
public_key = "your_public_key_here"
private_key = "your_private_key_here"
```

---

## Want to Help?
Contributions are welcome! If you find a bug or have an idea to make this better:
1. Make a copy of this repository (fork it).
2. Create a new branch.
3. Send a pull request.

---

## License
This project is free to use under the MIT License. Check the `LICENSE` file for details.

---

## Thanks To
- [Marvel API](https://developer.marvel.com/) for providing the data.
- Marvel comics for inspiring this project!

