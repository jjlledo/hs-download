import os
import pyautogui
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chromedriver_path = os.getcwd() + "/chromedriver"
chrome_options = webdriver.ChromeOptions()
local_state = {"protocol_handler.excluded_schemes.magnet" : False}
chrome_options.add_experimental_option("localState",local_state)
driver = webdriver.Chrome(executable_path=chromedriver_path,
                          chrome_options=chrome_options)

try:
    driver.get("http://horriblesubs.info")
    continue_dl = input("Navigate to the desired show URL and press ENTER")

    buttons = driver.find_elements_by_xpath("//a[text()='1080p']")

    magnets = driver.find_elements_by_xpath("//div[contains(@class, '1080p')] \
                                            //a[@title='Magnet Link']")

    releases = driver.find_elements_by_class_name("rls-label")

    print("Number of 1080p magnets found: " + str(len(magnets)))
    for release in releases:
        print(release.text)

    continue_dl = input("Press ENTER to continue with download")

    for button, magnet in zip(reversed(buttons), reversed(magnets)):
        button.click()
        time.sleep(1)
        magnet.click()
        time.sleep(1)
        pyautogui.press("enter")

    WebDriverWait(driver, 86400).until(EC.number_of_windows_to_be(0))

finally:
    driver.quit()
