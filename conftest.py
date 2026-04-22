import pytest
from selenium import webdriver
from data import BASE_URL


@pytest.fixture
def driver():
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get(BASE_URL)
    yield browser
    browser.quit()