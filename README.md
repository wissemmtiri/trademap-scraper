# **TradeMap Scraper**
A Selenium-based Python script designed to automate data extraction from **TradeMap** . This tool allows users to interact with TradeMap's dropdown menus, select specific options, and export data as Excel files.

## **Installation**
**Step 1:** Clone the Repository

        git clone https://github.com/wissemmtiri/trademap-scraper.git
        cd trademap-scraper

**Step 2:** Set Up a Virtual Environment
1. Create a Virtual Environment

        python3 -m venv venv

2. Activate the Virtual Environment
    * On Windows:

            .\venv\Scripts\activate
    * On macOS/Linux:

            source venv/bin/activate
**Step 3:** Install Dependencies

Install the required packages using pip:

        pip install -r requirements.txt


## **Usage**
### Run the Scrapper
To run the script in normal mode (interactive user input):

        python main.py

The script will prompt you to enter values for various fields. After all selections are made, it will export and download the data as an Excel file.

### Explore available Options
To explore available options in TradeMap's dropdown fields:

        python main.py menu
This will open a headless browser, connect to TradeMap, and display a menu where you can view all available options for each field.