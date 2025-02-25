from trademap_scraper import run_scraper
from menu import show_menu
import sys

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "menu":
        show_menu()
    else:
        run_scraper()

if __name__ == "__main__":
    main()