from model.WebScraper import WebScraper
from view.UI import UI

class WebScraperController:
    def __init__(self, webScraper: WebScraper, view: UI):
        self.webScraper = webScraper
        self.view = view

    def start(self):
        input_file = self.view.get_input_file()
        keyword = self.view.get_keyword()
        output_file = self.view.get_output_file()

        if self.view.get_summary(input_file, keyword, output_file):
            self.webScraper.scrape(input_file, keyword, output_file)