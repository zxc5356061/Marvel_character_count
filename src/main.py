from src.marvel_character_count import MarvelCharacterCount

if __name__ == "__main__":
    marvel_counter = MarvelCharacterCount()
    marvel_counter.get_all_characters()  # Fetch characters
    marvel_counter.results_to_json()  # Save to JSON file
    marvel_counter.count_appearance_frequency()  # Count frequency of appearances

    print(marvel_counter.count_appearance)