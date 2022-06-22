import requests
from bs4 import BeautifulSoup

class WebScraper:

    def _find_keyword(self, url: str, keyword: str) -> bool:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        text = soup.get_text()

        return keyword in text

    def _find_dirs(self, url: str) -> list[str]:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")

        subdirs = {url + '/' + node.get('href') 
        for node in soup.find_all('a') 
        if node.get('href').endswith("")}

        subdirs.add(url)

        return subdirs

    def _add_to_output(self, url: str, output_folder: str) -> None :
        with open(output_folder + "/output.txt", "a") as file:
            file.write(url + "\n")

    def _find(self, url: str, keyword: str, output_folder: str) -> None:
        # FOR EACH DIRECTORY + SUBDIRECTORY
        dirs = self._find_dirs(url)

        for dir in dirs:

            # IF KEYWORD SPOTTED
            if self._find_keyword(dir, keyword):

                # ADD TO THE OUTPUT FILE
                self._add_to_output(dir, output_folder)

    def scrape(self, input_file: str, keyword: str, output_folder: str) -> None:
        
        # CREATE OUTPUT FILE OR CLEAR OUTPUT FILE IF IT EXISTS
        try:
            with open(output_folder + "/output.txt", "x") as file:
                pass
        except:
            with open(output_folder + "/output.txt", "w") as file:
                pass
        
        # FOR EVERY WEBSITE IN THE INPUT TEXT FILE
        with open(input_file) as file:
            lines = file.readlines()

            for line in lines:
                print(f"Looking in { line }...")
                # IF THERE'S A KEYWORD WITHIN THAT WEBSITE
                self._find(line.strip(), keyword, output_folder)

        print("=======================")
        print("IT ALL WORKS!")
        print("=======================")
