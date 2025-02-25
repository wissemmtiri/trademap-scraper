from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import selenium_stealth
from utils import get_user_input

def run_scraper():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--headless")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    selenium_stealth.stealth(
        driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
    )

    try:
        driver.get("https://www.trademap.org/Bilateral_TS.aspx")
        print("Opened TradeMap")

        fields = [
            ("Product", "ctl00_NavigationControl_DropDownList_Product", "TOTAL - All products"),
            ("Country", "ctl00_NavigationControl_DropDownList_Country", "Tunisia"),
            ("Partner", "ctl00_NavigationControl_DropDownList_Partner", "All"),
            ("Trade Type", "ctl00_NavigationControl_DropDownList_TradeType", "Exports"),
            ("Output Type", "ctl00_NavigationControl_DropDownList_OutputType", "Yearly time series"),
            ("Output Option", "ctl00_NavigationControl_DropDownList_OutputOption", "by product"),
            ("Product Cluster Level", "ctl00_NavigationControl_DropDownList_ProductClusterLevel", "At the same level (2 digits)"),
            ("Indicator", "ctl00_NavigationControl_DropDownList_TS_Indicator", "Values"),
            ("Currency", "ctl00_NavigationControl_DropDownList_TS_Currency", "Euro"),
        ]

        for field_name, dropdown_id, default_value in fields:
            # close_open_dropdown(driver)
            dropdown = driver.find_element(By.ID, dropdown_id)
            dropdown.click()
            value = get_user_input(f"Enter {field_name} (e.g., '{default_value}')", default_value)
            option = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//select[@id='{dropdown_id}']/option[text()='{value}']"))
            )
            option.click()
            print(f"Selected '{value}' for {field_name} successfully")

        # ========================== EXPORT DATA AS EXCEL
        export_excel_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "ctl00_PageContent_GridViewPanelControl_ImageButton_ExportExcel"))
        )
        export_excel_button.click()

        # ========================== TIME DELAY AS MARGIN
        time.sleep(10)

    finally:
        driver.quit()
        print("Browser closed")

def close_open_dropdown(driver):
    try:
        driver.find_element(By.TAG_NAME, "body").click()
    except Exception as e:
        print(f"Error closing dropdown: {e}")