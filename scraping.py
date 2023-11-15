from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Scraping dynamic content using Selenium

# Set up the Selenium WebDriver (you need to have the appropriate webdriver installed)
driver = webdriver.Chrome()  # You can use other webdrivers like Firefox, Edge, etc.

# Navigate to the webpage with dynamically loaded content
url = "https://www.sreality.cz/hledani/prodej/byty/zahranici"
driver.get(url)

try:
    # Wait for the dynamic content to load (adjust the timeout as needed)
    element = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "span.name"))
    )

    # Extract data from the loaded page
    dynamic_content = driver.page_source

    # Now, you can parse and extract information from the dynamic content using a parsing library like BeautifulSoup
    # Example: Use BeautifulSoup to extract text from an element with class "example-class"
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
        else:
            print("No image", name, location)

    # data = soup.find(class_='name')

    print("-----------------------------")
    print(len(data))


finally:
    # Close the browser window when done
    driver.quit()

