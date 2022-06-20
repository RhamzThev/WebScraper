from model.WebScraper import WebScraper
from view.CLI import CLI
from controller.WebScraperController import WebScraperController

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