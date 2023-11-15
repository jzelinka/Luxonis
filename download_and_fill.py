from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import houses_db

driver = webdriver.Chrome()  # You can use other webdrivers like Firefox, Edge, etc.

url = "https://www.sreality.cz/hledani/prodej/byty/zahranici"
driver.get(url)

houses = houses_db.db_handler()
houses.delete_table()
houses.create_table()

try:
    element = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "span.name"))
    )

    dynamic_content = driver.page_source

    from bs4 import BeautifulSoup

    soup = BeautifulSoup(dynamic_content, 'html.parser')
    data = soup.find_all("div", {"class": "property"})

    for i in data:
        property_soup = BeautifulSoup(str(i), 'html.parser')

        imgs = property_soup.find_all("img")
        
        name = property_soup.find("span", {"class": "name"}).text
        location = property_soup.find("span", {"class": "locality"}).text
        if len(imgs) > 0:
            print(name, location, imgs[0]['src'])
            houses.insert(name, location, imgs[0]['src'])

        else:
            print("No image", name, location)


finally:
    # Close the browser window when done
    driver.quit()

print(houses.get_rows())