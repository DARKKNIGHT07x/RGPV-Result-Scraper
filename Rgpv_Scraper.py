import csv
import time
import traceback
from PIL import Image
import pytesseract
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Specify the path to the EdgeDriver executable
edge_driver_path = r"C:\Web Driver\msedgedriver.exe"  # Update with the actual path to EdgeDriver

# Specify the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Update with the actual path to Tesseract executable

# Specify the path to the CSV file containing roll numbers
csv_file_path = r"D:\Web Scraper\Students_Record_Cyber_2ndyear.csv"  # Absolute path to the CSV file

# Specify the path to the output CSV file
output_csv_file_path = r"D:\Web Scraper\results.csv"  # Absolute path to the output CSV file

# Create options and service
edge_options = Options()
service = EdgeService(edge_driver_path)

# Create the Edge WebDriver instance
try:
    driver = webdriver.Edge(service=service, options=edge_options)
    # Open the URL
    url = "http://result.rgpv.ac.in/result/ProgramSelect.aspx"
    driver.get(url)
    # Locate and click the radio button
    radio_button = driver.find_element(By.ID, 'radlstProgram_1')
    radio_button.click()

    # Wait for the page to redirect and load completely
    WebDriverWait(driver, 10).until(EC.url_changes(url))
except Exception as e:
    print(f"An error occurred: {e}")
    traceback.print_exc()
finally:
    driver.quit()
