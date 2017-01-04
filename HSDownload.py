import pyautogui
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chromedriver_path = "/Users/Juan/Desktop/chromedriver"
chrome_options = webdriver.ChromeOptions()
local_state = {"protocol_handler.excluded_schemes.magnet" : False}
chrome_options.add_experimental_option("localState",local_state)
driver = webdriver.Chrome(executable_path = chromedriver_path,
                          chrome_options=chrome_options)

url = input("Paste url of show to download:\n")
driver.get(url)

WebDriverWait(driver, 5).until(EC.title_contains("HorribleSubs"))

links = driver.find_elements_by_xpath("//a[text()='1080p']")
print("Number of 1080p buttons found: " + str(len(links)))

magnets = driver.find_elements_by_xpath("//div[contains(@class, '1080p')] \
                                        //a[@title='Magnet Link']")
print("Number of 1080p magnets found: " + str(len(magnets)))

links = reversed(links)
magnets = reversed(magnets)

for link, magnet in zip(links, magnets):
    link.click()
    time.sleep(1)
    magnet.click()
    time.sleep(1)
    pyautogui.press("enter")

try:
    WebDriverWait(driver, 604800).until(EC.number_of_windows_to_be(0))

finally:
    driver.quit()
