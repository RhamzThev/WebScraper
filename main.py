from model.web_scraper import WebScraper
from view.cli import CLI
from controller.web_scraper_controller import WebScraperController

class Main:
    def __init__(self):
        self.model = WebScraper()
        self.view = CLI()
        self.controller = WebScraperController(self.model, self.view)

    def main(self):
        self.controller.start()

if __name__ == "__main__": 
    main = Main()
    main.main()