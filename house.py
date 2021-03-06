from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from math import sin, log
import time

try:
    def calc(x):
        return log(abs(12 * sin(x)))

    browser = webdriver.Chrome()
    #browser.implicitly_wait(15)

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '100'))
    button = browser.find_element_by_id('book')
    button.click()

    x = browser.find_element_by_id('input_value').text
    y = calc(int(x))
    browser.find_element_by_id('answer').send_keys(str(y))
    browser.find_element_by_css_selector('[type="submit"]').click()
    alert = browser.switch_to.alert
    time.sleep(3)
    alert.accept()

finally:
    time.sleep(15)
    browser.quit()