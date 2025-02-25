from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def show_menu():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    try:
        driver.get("https://www.trademap.org/Bilateral_TS.aspx")
        print("Connected to TradeMap")

        fields = {
            1: "Product",
            2: "Country",
            3: "Partner",
            4: "Trade Type",
            5: "Output Type",
            6: "Output Option",
            7: "Product Cluster Level",
            8: "Indicator",
            9: "Currency",
            0: "Exit"
        }

        dropdown_ids = {
            1: "ctl00_NavigationControl_DropDownList_Product",
            2: "ctl00_NavigationControl_DropDownList_Country",
            3: "ctl00_NavigationControl_DropDownList_Partner",
            4: "ctl00_NavigationControl_DropDownList_TradeType",
            5: "ctl00_NavigationControl_DropDownList_OutputType",
            6: "ctl00_NavigationControl_DropDownList_OutputOption",
            7: "ctl00_NavigationControl_DropDownList_ProductClusterLevel",
            8: "ctl00_NavigationControl_DropDownList_TS_Indicator",
            9: "ctl00_NavigationControl_DropDownList_TS_Currency"
        }

        while True:
            print("\n=== TradeMap Field Options Menu ===")
            print("Select a field to view its options:")
            for key, value in fields.items():
                print(f"[{key}]. {value}")

            choice = input("Enter the number of the field you want to explore (or 0 to exit): ")
            if not choice.isdigit():
                print("Invalid input. Please enter a number.")
                continue

            choice = int(choice)
            if choice == 0:
                print("Exiting menu...")
                break

            if choice not in fields:
                print("Invalid choice. Please try again.")
                continue

            dropdown_id = dropdown_ids.get(choice)
            if not dropdown_id:
                print("Dropdown not found. Returning to menu.")
                continue

            dropdown = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, dropdown_id))
            )
            options = dropdown.find_elements(By.TAG_NAME, "option")

            print(f"\nOptions for '{fields[choice]}':")
            for idx, option in enumerate(options, start=1):
                print(f"{idx}. {option.text}")
            input("\nPress Enter to return to the menu...")

    finally:
        driver.quit()
        print("Connection closed.")