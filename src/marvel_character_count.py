import json
import logging
import time
from hashlib import md5

import httpx

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class MarvelCharacterCount:
    def __init__(self,
                 public_key='f25aed1b3626fe65d815613e35092c63',
                 private_key='ccb12970d393ae3e244b3ed67a77392be8044c16',
                 json_file_path='marvel_characters.json'):
        self.public_key = public_key
        self.private_key = private_key
        self.ts = str(time.time())
        self.hash_str = md5(f"{self.ts}{self.private_key}{self.public_key}".encode("utf8")).hexdigest()
        self.limit = 100
        self.offset = 0

        self.params = {
            "apikey": self.public_key,
            "ts": self.ts,
            "hash": self.hash_str,
            "limit": self.limit,
            "offset": self.offset,
            "orderBy": "name",
        }

        self.json_file_path = json_file_path
        self.all_characters = []
        self.count_appearance = {}

    def fetch_characters_batch(self, client):
        """Fetch a single batch of characters from the Marvel API."""
        try:
            response = client.get('https://gateway.marvel.com/v1/public/characters', params=self.params)

            if response.status_code != 200:
                logger.warning(f"Failed to fetch characters, status code: {response.status_code}")
                return []

            data = response.json()
            return data.get("data", {}).get("results", [])

        except Exception as e:
            logger.error(f"Error during API request: {e}")
            return []

    def get_all_characters(self):
        """Fetches all Marvel characters, handling pagination."""
        try:
            with httpx.Client(verify=False, timeout=30.0) as client:
                while True:
                    # Fetch characters batch
                    characters_batch = self.fetch_characters_batch(client)
                    if not characters_batch:  # Break the loop if no more characters to be captured
                        break

                    # Add current batch back to the list
                    self.all_characters.extend(characters_batch)

                    # Handling pagination
                    self.offset += self.limit
                    self.params["offset"] = self.offset

                    logger.info(f"Fetched {len(characters_batch)} characters, Total: {len(self.all_characters)}")

            logger.info(f"Total characters fetched: {len(self.all_characters)}")
            return self.all_characters

        except Exception as e:
            logger.error(f"Error during character fetching: {e}")
            return []

    def results_to_json(self):
        """Saves the fetched characters to a JSON file for offline references or debugging."""
        try:
            with open(self.json_file_path, 'w', encoding='utf-8') as f:
                json.dump(self.all_characters, f, ensure_ascii=False, indent=4)
            logger.info(f"Data saved to {self.json_file_path}")
        except Exception as e:
            logger.error(f"Error saving to file: {e}")

    def count_appearance_frequency(self):
        """Reads the JSON file and retrieve the frequency of comic appearances for each character."""
        try:
            with open(self.json_file_path, 'r', encoding='utf-8') as f:
                characters = json.load(f)

            for character in characters:
                character_name = character.get("name", "Unknown")  # Error handling for missing names
                quantity = character.get("comics", {}).get("available", 0)
                self.count_appearance[character_name] = quantity

            logger.info(f"Total characters in frequency count: {len(self.count_appearance)}")
            return self.count_appearance

        except FileNotFoundError:
            logger.error(f"File not found: {self.json_file_path}")
            return {}

        except json.JSONDecodeError:
            logger.error(f"Error decoding JSON from {self.json_file_path}")
            return {}

        except Exception as e:
            logger.error(f"Error processing file: {e}")
            return {}
