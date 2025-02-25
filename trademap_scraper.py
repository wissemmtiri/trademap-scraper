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

        # ========================== PRODUCT
        product_value = get_user_input("Enter Product (e.g., '01 - Live animals')", "All")
        product_dropdown = driver.find_element(By.ID, "ctl00_NavigationControl_DropDownList_Product")
        product_dropdown.click()
        product_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//option[text()='{product_value}']"))
        )
        product_option.click()
        print(f"Selected '{product_value}' successfully")

        # ========================== COUNTRY
        country_value = get_user_input("Enter Country (e.g., 'Tunisia')", "Tunisia")
        country_dropdown = driver.find_element(By.ID, "ctl00_NavigationControl_DropDownList_Country")
        country_dropdown.click()
        country_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//select[@id='ctl00_NavigationControl_DropDownList_Country']/option[text()='{country_value}']"))
        )
        country_option.click()
        print(f"Selected '{country_value}' successfully")

        # ========================== PARTNER
        partner_value = get_user_input("Enter Partner (e.g., 'Germany' or 'All')", "All")
        partner_dropdown = driver.find_element(By.ID, "ctl00_NavigationControl_DropDownList_Partner")
        partner_dropdown.click()
        partner_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//select[@id='ctl00_NavigationControl_DropDownList_Partner']/option[text()='{partner_value}']"))
        )
        partner_option.click()
        print(f"Selected '{partner_value}' as partner successfully")

        # ========================== TRADE_TYPE
        trade_type_value = get_user_input("Enter Trade Type (e.g., 'Exports', 'Imports')", "Exports")
        trade_type_dropdown = driver.find_element(By.ID, "ctl00_NavigationControl_DropDownList_TradeType")
        trade_type_dropdown.click()
        trade_type_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//select[@id='ctl00_NavigationControl_DropDownList_TradeType']/option[text()='{trade_type_value}']"))
        )
        trade_type_option.click()

        # ========================== OUTPUT_TYPE
        output_type_value = get_user_input("Enter Output Type (e.g., 'Yearly time series')", "Yearly time series")
        output_type_dropdown = driver.find_element(By.ID, "ctl00_NavigationControl_DropDownList_OutputType")
        output_type_dropdown.click()
        output_type_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//select[@id='ctl00_NavigationControl_DropDownList_OutputType']/option[text()='{output_type_value}']"))
        )
        output_type_option.click()

        # ========================== OUTPUT_OPTION
        output_option_value = get_user_input("Enter Output Option (e.g., 'by product')", "by product")
        output_option_dropdown = driver.find_element(By.ID, "ctl00_NavigationControl_DropDownList_OutputOption")
        output_option_dropdown.click()
        output_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//select[@id='ctl00_NavigationControl_DropDownList_OutputOption']/option[text()='{output_option_value}']"))
        )
        output_option.click()

        # ========================== PRODUCT_CLUSTER_LEVEL
        cluster_level_value = get_user_input("Enter Product Cluster Level (e.g., 'At the same level (2 digits)')", "At the same level (2 digits)")
        cluster_level_dropdown = driver.find_element(By.ID, "ctl00_NavigationControl_DropDownList_ProductClusterLevel")
        cluster_level_dropdown.click()
        cluster_level_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//select[@id='ctl00_NavigationControl_DropDownList_ProductClusterLevel']/option[text()='{cluster_level_value}']"))
        )
        cluster_level_option.click()

        # ========================== TS_INDICATOR
        indicator_value = get_user_input("Enter Indicator (e.g., 'Values')", "Values")
        indicator_dropdown = driver.find_element(By.ID, "ctl00_NavigationControl_DropDownList_TS_Indicator")
        indicator_dropdown.click()
        indicator_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//select[@id='ctl00_NavigationControl_DropDownList_TS_Indicator']/option[text()='{indicator_value}']"))
        )
        indicator_option.click()

        # ========================== CURRENCY
        currency_value = get_user_input("Enter Currency (e.g., 'Euro')", "Euro")
        currency_dropdown = driver.find_element(By.ID, "ctl00_NavigationControl_DropDownList_TS_Currency")
        currency_dropdown.click()
        currency_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//select[@id='ctl00_NavigationControl_DropDownList_TS_Currency']/option[text()='{currency_value}']"))
        )
        currency_option.click()
        print(f"Selected '{currency_value}' as currency successfully")

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