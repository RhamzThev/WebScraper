from model.web_scraper import WebScraper

EXAMPLE_STATIC = "https://realpython.github.io/fake-jobs/jobs/senior-python-developer-0.html"

EXAMPLE_ONE = "https://www.demoblaze.com/"
EXAMPLE_TWO = "https://demo.opencart.com/"
EXAMPLE_THREE = "https://www.phptravels.net/"

INPUT_FILE = "./input.txt"
OUTPUT_FILE = "./output.txt"

def test_find_keyword_static():
    webScraper = WebScraper()
    assert WebScraper._find_keyword(webScraper, EXAMPLE_THREE, "Library")

def test_add_to_output():
    assert False

def test_scrape():
    assert False
