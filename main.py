import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from pprint import pprint
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

load_dotenv("G:\My Drive\Programming\Python\EnvironmentVariables\.env.txt")
GOOGLE_VOICE = os.getenv("GOOGLE_VOICE")
TINDER_URL = "https://tinder.com/"
chrome_driver_path = "C:\Programming\Web Driver\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get(TINDER_URL)
base_window = driver.window_handles[0]

# login with phone number. manually enter 2factor codes.
# login = driver.find_element(By.CLASS_NAME, 'button')
time.sleep(1)
login = driver.find_element(By.XPATH, '//*[@id="o-1556761323"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login.click()
time.sleep(1)
by_phone = driver.find_element(By.XPATH, '//*[@id="o-1335420887"]/div/div/div[1]/div/div[3]/span/div[3]/button')
by_phone.click()
time.sleep(5)
number = driver.find_element(By.NAME, "phone_number")
number.send_keys(GOOGLE_VOICE)
time.sleep(5)
# pprint(driver.page_source)
# continue_btn = driver.find_element(By.TAG_NAME, 'button')
# continue_btn.click()
# driver.find_element(By.CLASS_NAME, '#o-1335420887>div>div').click()
driver.switch_to.window(base_window)
# print(driver.title)
# print(driver.window_handles)
continue_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[1]/button')))
time.sleep(1)
continue_btn.click()
time.sleep(60)

# dismiss popups.
driver.find_element(By.XPATH, '//*[@id="o-1335420887"]/div/div/div/div/div[3]/button[1]').click()
driver.find_element(By.XPATH, '//*[@id="o-1335420887"]/div/div/div/div/div[3]/button[1]').click()
driver.find_element(By.XPATH, '//*[@id="o-1556761323"]/div/div[2]/div/div/div[1]/button').click()

# nope a bunch of people
for _ in range(99):
    try:
        driver.find_element(By.XPATH, '//*[@id="q-184954025"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[2]/button')
    except NoSuchElementException:
        time.sleep(2)
    finally:
        time.sleep(2)
