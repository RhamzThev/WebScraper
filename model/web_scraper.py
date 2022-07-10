from urllib.error import HTTPError, URLError
import requests
from bs4 import BeautifulSoup

class WebScraper:

    def _find_keyword(self, url: str, keyword: str) -> bool:
        try:
            page = requests.get(url)
            soup = BeautifulSoup(page.content, "html.parser")
            text = soup.get_text()

            return keyword.lower() in text.lower()
        except HTTPError as error:
            print(f"{url} is not available: {error}")
            return False
        except URLError as error:
            print(f"{url} is an invalid URL: {error}")
            return False

    def _find_dirs(self, url: str) -> set[str]:
        try:
            page = requests.get(url)
            soup = BeautifulSoup(page.content, "html.parser")

            subdirs = {url + node.get('href') 
            for node in soup.find_all('a', href=True)
            if not node.get('href').startswith("http")}

            subdirs.add(url)

            return subdirs
        except HTTPError as error:
            print(f"{url} is not available: {error}")
            return set()
        except URLError as error:
            print(f"{url} is an invalid URL: {error}")
            return set()

    def _add_to_output(self, url: str, output_folder: str) -> None :
        with open(output_folder + "/output.txt", "a") as file:
            print(f"*** ADDED { url } TO THE OUTPUT FILE. ***")
            file.write(url + "\n")

    def _find(self, url: str, keyword: str, output_folder: str) -> None:
        # FOR EACH DIRECTORY + SUBDIRECTORY
        dirs = self._find_dirs(url)

        for dir in dirs:
            print(f"Looking in { dir }...")
            # IF KEYWORD SPOTTED
            if self._find_keyword(dir, keyword):

                # ADD TO THE OUTPUT FILE
                self._add_to_output(dir, output_folder)

    def scrape(self, input_file: str, keyword: str, output_folder: str) -> None:
        
        try:
            # CREATE OUTPUT FILE OR CLEAR OUTPUT FILE IF IT EXISTS
            try:
                with open(output_folder + "/output.txt", "x") as file:
                    pass
            except FileExistsError:
                print("'output.txt' already exists. Overwriting file.")
                with open(output_folder + "/output.txt", "w") as file:
                    pass
            
            # FOR EVERY WEBSITE IN THE INPUT TEXT FILE
            with open(input_file) as file:
                lines = file.readlines()

                for line in lines:
                    line = line.strip()
                    # IF THERE'S A KEYWORD WITHIN THAT WEBSITE
                    self._find(line, keyword, output_folder)
        except FileNotFoundError as error:
            print(f"{input_file} is not found: {error}")
