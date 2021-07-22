from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

options = Options()
options.add_argument("--user-data-dir=/home/pi/.config/chromium")
driver = webdriver.Chrome(options=options)

### gmeet link + setup ###
meet_code="YOUR_MEET_CODE_HERE"
chat_messg="CHAT_MESSAGE_HERE"

delay=3

driver.get(f"https://meet.google.com/{meet_code}?authuser=1")
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'e')
join_button = WebDriverWait(driver, delay).until(
    EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Join now')]")))
driver.execute_script("arguments[0].click();", join_button)
sleep(4)
mesg_button = driver.find_element_by_xpath("//c-wiz[@id='ow3']/div/div/div[9]/div[3]/div[10]/div[3]/div[2]/div/div/div[3]/span/button/i").click()
sleep(1)
mesg_text_inp = driver.find_element_by_name("chatTextInput").send_keys(chat_messg)
mesg_text_inp = driver.find_element_by_name("chatTextInput").send_keys(Keys.ENTER)
