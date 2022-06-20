from model.WebScraper import WebScraper
from view.UI import UI

class WebScraperController:
    def __init__(self, webScraper: WebScraper, view: UI):
        self.webScraper = webScraper
        self.view = view

    def start(self):
        input = self.view.get_input_file()
        keyword = self.view.get_keyword()
        output = self.view.get_output_file()