from model.web_scraper import WebScraper
import os

EXAMPLE_STATIC = "https://realpython.github.io/fake-jobs/jobs/senior-python-developer-0.html"

EXAMPLE_ONE = "https://www.demoblaze.com/"
EXAMPLE_TWO = "https://demo.opencart.com/"
EXAMPLE_THREE = "https://www.phptravels.net/"

INPUT_FILE = "C:/Users/coolr/OneDrive/GitHub/WebScraper/model/test/txt/input.txt"
OUTPUT_FILE = "C:/Users/coolr/OneDrive/GitHub/WebScraper/model/test/txt/output.txt"

TXT_FOLDER = "C:/Users/coolr/OneDrive/GitHub/WebScraper/model/test/txt/"

def test_find_keyword_true():
    webScraper = WebScraper()
    assert WebScraper._find_keyword(webScraper, EXAMPLE_STATIC, "Python")

def test_find_keyword_false():
    webScraper = WebScraper()
    assert not WebScraper._find_keyword(webScraper, EXAMPLE_STATIC, "False Keyword")

def test_find_dirs_zero():
    webScraper = WebScraper()
    length = len(WebScraper._find_dirs(webScraper, EXAMPLE_STATIC))
    assert length == 1

def test_find_dirs_non_zero():
    webScraper = WebScraper()
    length = len(WebScraper._find_dirs(webScraper, EXAMPLE_ONE))
    assert length > 1

def test_add_to_output():
    webScraper = WebScraper()
    WebScraper._add_to_output(webScraper, EXAMPLE_ONE, TXT_FOLDER)

    with open(OUTPUT_FILE) as file:
        line = file.readlines()[-1].strip()

    assert line == EXAMPLE_ONE

def test_find():
    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)

    webScraper = WebScraper()
    WebScraper._find(webScraper, EXAMPLE_ONE, "Home", TXT_FOLDER)

    with open(OUTPUT_FILE) as file:
        line = len(file.readlines())

    assert line == 6

def test_scrape_create_output():
    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)

    webScraper = WebScraper()
    WebScraper.scrape(webScraper, INPUT_FILE, "Laptops", TXT_FOLDER)

    with open(OUTPUT_FILE) as file:
        line = len(file.readlines())

    assert line == 9

def test_scrape_clear_output():
    webScraper = WebScraper()
    WebScraper.scrape(webScraper, INPUT_FILE, "Laptops", TXT_FOLDER)

    with open(OUTPUT_FILE) as file:
        line = len(file.readlines())

    assert line == 9
