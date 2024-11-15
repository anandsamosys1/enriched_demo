from selenium import webdriver
import pytest

@pytest.mark.selenium
def test_001_selenium():
    driver = webdriver.Chrome()
    driver.get("https://enrichedacademy.com/")
    assert driver.title==("Enriched Academy – Canada’s #1 Financial Literacy Resource")
    driver.quit()





