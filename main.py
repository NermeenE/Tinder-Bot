from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from time import sleep
from dotenv import load_dotenv
import os

load_dotenv('.env')
EMAIL = os.environ.get("TINDER_EMAIL")
PASSWORD = os.environ.get("TINDER_PASSWORD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)

tinder = driver.get("https://tinder.com/")

sleep(2)

cookies_popup = driver.find_element(By.XPATH, value="//div[contains(text(), 'I decline')]")
cookies_popup.click()

#sign in:
signin_btn = driver.find_element(By.XPATH, value='/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
signin_btn.click()
sleep(2)


#FB log in:
fb_login = driver.find_element(By.XPATH, value='//*[@id="s1746112904"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
fb_login.click()
sleep(2)

#change windows to fb-login:
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

fb_email = driver.find_element(By.XPATH, value='//*[@id="email"]')
fb_email.send_keys(EMAIL)
fb_password = driver.find_element(By.XPATH,value='//*[@id="pass"]')
fb_password.send_keys(PASSWORD, Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)

sleep(8)

##Notifcation pop-ups:
location_popup = driver.find_element(By.XPATH, value='//*[@id="s1746112904"]/main/div/div/div/div[3]/button[1]/div[2]/div[2]')
location_popup.click()

enable_notifications = driver.find_element(By.XPATH, value='//*[@id="s1746112904"]/main/div/div/div/div[3]/button[2]/div[2]/div[2]')
enable_notifications.click()

sleep(4)

try:
    terms_popup = driver.find_element(By.XPATH, '//*[@id="s1746112904"]/main/div/div[4]/button/div[2]/div[2]')
    terms_popup.click()
except NoSuchElementException:
    sleep(2)


sleep(5)


#Free Tinder acct only allows 100 "Likes" per day
for n in range(7):

  sleep(2)

  try:
    print("called")
    body = driver.find_element(By.CSS_SELECTOR, value="body")
    body.send_keys(Keys.LEFT) 
    print("disliked")

  #if a "Matched" appears:
  except ElementClickInterceptedException:
    try:
      matched_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
      matched_popup.click()
    #retry if "Like" isnt visable:
    except NoSuchElementException:
      sleep(2)

driver.quit()

