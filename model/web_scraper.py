import requests
from bs4 import BeautifulSoup

class WebScraper:

    def _find_keyword(self, url, keyword):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        text = soup.get_text()

        return keyword in text

    def _find_dirs(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")

        subdirs = {url + '/' + node.get('href') 
        for node in soup.find_all('a') 
        if node.get('href').endswith("")}

        return subdirs.add(url)

    def _find(self, url, keyword, output_folder):

        # FOR EACH DIRECTORY + SUBDIRECTORY
        dirs = self._find_dirs(url)
        for dir in dirs:

            # IF KEYWORD SPOTTED
            if self._find_keyword(dir, keyword):

                # ADD TO THE OUTPUT FILE
                self._add_to_output(dir, output_folder)

    def _add_to_output(self, url, output_folder):
        pass

    def scrape(self, input_file, keyword, output_folder):
        # FOR EVERY WEBSITE IN THE INPUT TEXT FILE
        with open(input_file) as file:
            lines = file.readlines()

            for line in lines:

                # IF THERE'S A KEYWORD WITHIN THAT WEBSITE
                self._find(line, keyword, output_folder)

        print("=======================")
        print("IT ALL WORKS!")
        print("=======================")
