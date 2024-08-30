# WebScraper

## Overview
WebScraper is a Python-based application designed to scrape websites for specific keywords. The application allows users to input a list of URLs, specify a keyword, and generate a report of which URLs contain the keyword. The output is saved to a specified directory.

## Features
- **Keyword Search:** Scrapes websites to find the specified keyword within the content.
- **Directory Search:** Automatically navigates through subdirectories of the given URLs to ensure comprehensive scraping.
- **Output Report:** Generates a text file containing the URLs where the keyword was found.

## Components
The WebScraper application is structured into the following key components:

1. **Model (`model/web_scraper.py`):** Handles the core scraping logic, including sending requests to URLs, parsing HTML, and checking for the presence of keywords.

2. **View (`view/CLI.py` & `view/UI.py`):** Manages the user interface, offering both a command-line interface and abstract methods for handling input/output operations.

3. **Controller (`controller/web_scraper_controller.py`):** Coordinates interactions between the model and view, ensuring the correct sequence of operations based on user inputs.

4. **Main Entry Point (`main.py`):** Initializes the application by creating instances of the model, view, and controller, and starts the scraping process.

5. **Tests (`model/test/test_web_scraper.py`):** Includes unit tests for validating the functionality of the WebScraper.

## How to Use
1. **Input File:** Prepare a text file containing the list of URLs you want to scrape.
2. **Keyword:** Decide on the keyword you want to search for within these URLs.
3. **Run the Application:**
   - Execute `main.py` to start the application.
   - Follow the on-screen prompts to select your input file, enter the keyword, and choose an output directory.
   - Confirm the pre-run summary and let the application process the URLs.

4. **Output:** The application generates an `output.txt` file in the specified directory, listing all URLs where the keyword was found.

## License
This project is licensed under the terms of the [MIT License](LICENSE).

## Future Prospects
Please note that this repository will be archived. No further updates or support will be provided.
