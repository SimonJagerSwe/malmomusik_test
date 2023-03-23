import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from helper_tests_malmomusik import simple_assert, boolean_assert

MAIN_SITE = "https://www.malmomusikaffar.com/"
ELEC_GUIT = "https://www.malmomusikaffar.com/stranginstrument/gitarr/elgitarrer"
T484 = "https://www.malmomusikaffar.com/eastman-t484-classic-t484"

@pytest.fixture
def load_driver():

    driver = webdriver.Chrome()

    yield driver

    driver.quit()
    

def assert_open_time(load_driver):

    driver = load_driver

    driver.get(MAIN_SITE)

    heading = driver.find_element(By.XPATH, "/html/body/div[3]/footer/section/ul/li[1]/header/span")

    simple_assert(heading.text, "M-F: 10-18 L: 10-14")


def find_T484(load_driver):

    driver = load_driver

    driver.get(ELEC_GUIT)

    T484_link = driver.find_element(By.LINK_TEXT, "T484 Classic")

    T484_link.click()

    heading = driver.find_element(By.XPATH, "/html/body/div[3]/main/div/div/section/div/div[3]/div[2]/h1/span")

    simple_assert(heading.text, "T484 Classic")


def add_to_cart(load_driver):

    driver = load_driver

    driver.get(T484)

    buy_button = driver.find_element(By.XPATH, "/html/body/div[3]/main/div/div/section/div/div[3]/div[4]/div[2]/form/div/div/div[2]/button/span")

    buy_button.click()


def find_on_fb(load_driver):

    driver = load_driver

    driver.get(MAIN_SITE)

    fb_link = driver.find_element(By.XPATH, "/html/body/div[3]/footer/div[1]/div[2]/ul/li[1]/a/svg/use")

    fb_link.click()