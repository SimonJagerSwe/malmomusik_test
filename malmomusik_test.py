import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from helper_tests_malmomusik import simple_assert, boolean_assert

MAIN_SITE = "https://www.malmomusikaffar.com/"

@pytest.fixture
def load_driver():

    driver = webdriver.Chrome()

    yield driver

    driver.quit()