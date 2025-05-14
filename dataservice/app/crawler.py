from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManger
import time

def creawl_naver_flights():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://flight.naver.com/")
    time.sleep(5)

    sampel = {
        "airline": "대한항공",
        "departure": "ICN",
        "arrival": "NRT",
        "departure_time": "2025-0601T08:00",
        "price": "350000"
    }

    driver.quit()
    return [sample]