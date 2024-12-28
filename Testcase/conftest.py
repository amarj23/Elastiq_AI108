import pytest
from selenium import webdriver


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')


@pytest.fixture
def setup():
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.lambdatest.com/selenium-playground/table-sort-search-demo')
    driver.implicitly_wait(5)
    return driver
