from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options

@pytest.mark.selenium
def test_001_selenium():
    options = Options()
    options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    driver.get("https://enrichedacademy.com/")
    assert driver.title==("Enriched Academy – Canada’s #1 Financial Literacy Resource")
    driver.quit()





