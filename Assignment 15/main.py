import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException 
import pandas as pd

myUrl = "https://www.scrapingcourse.com/button-click"

options = Options()
options.add_argument('--headless=new')
cService = webdriver.ChromeService(executable_path='/usr/lib/chromium-browser/chromedriver')
driver = webdriver.Chrome(service=cService,options=options)

print("Apriamo il Browser")

driver.get(myUrl)
driver.implicitly_wait(10)

print("Si comincia!")

try:
    while True:
        new_count = driver.find_element(By.ID, "load-more-btn").get_attribute("data-offset")
        print("OFFSET: " + new_count)
        button = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.ID, 'load-more-btn'))
        )
        button.click()
        time.sleep(1)

        WebDriverWait(driver,5).until(
            lambda d: d.find_element(By.ID, "load-more-btn").get_attribute("data-offset") > new_count
        )

        print("Si dorme")
        time.sleep(2)

except TimeoutException:
    print("fine scraping")

items = driver.find_elements(By.CLASS_NAME, "product-item")

scrapeData = []

for item in items:
    data = {
        "Name": item.find_element(By.CLASS_NAME, "product-name").text,
        "Price": item.find_element(By.CLASS_NAME, "product-price").text,
        "link": item.find_element(By.TAG_NAME, "a").get_attribute("href") 
    }
    scrapeData.append(data)
driver.quit()

print("Dati parsati!")

df = pd.DataFrame(scrapeData)
df.to_csv("products.csv")
print(df)