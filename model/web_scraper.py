import requests
from bs4 import BeautifulSoup

class WebScraper:

    def _find_keyword(self, line, keyword):
        page = requests.get(line)
        soup = BeautifulSoup(page.content, "html.parser")
        text = soup.get_text()

        return keyword in text

    def _add_to_output(self, line, output):
        return

    def scrape(self, input_file, keyword, output_file):
        # FOR EVERY WEBSITE IN THE INPUT TEXT FILE
        with open(input_file) as file:
            lines = file.readlines()

            for line in lines:

                # IF THERE'S A KEYWORD WITHIN THAT WEBSITE
                if self._find_keyword(line, keyword):

                    # ADD TO THE OUTPUT FILE
                    self._add_to_output(line, output_file)

        print("=======================")
        print("IT ALL WORKS!")
        print("=======================")
