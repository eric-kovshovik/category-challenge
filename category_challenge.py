import time
import os
import settings
import pdb
from selenium import webdriver
from dotenv import load_dotenv

driver = webdriver.Chrome()
driver.get('https://accounts.intuit.com/index.html?offering_id=Intuit.ifs.mint&namespace_id=50000026&redirect_url=https%3A%2F%2Fmint.intuit.com%2Foverview.event%3Futm_medium%3Ddirect%26cta%3Dnav_login_dropdown%26adobe_mc%3DMCMID%253D68207418306127383673797277059766651502%257CMCAID%253D2EBACD6785033310-600011932000123E%257CMCORGID%253D969430F0543F253D0A4C98C6%252540AdobeOrg%257CTS%253D1567989798%26ivid%3Ddce1b692-c1ae-49c9-b178-bb6117a7cc2d')

login_id = driver.find_element_by_id('ius-userid')
login_id.send_keys(os.environ.get('MINT_LOGIN'))

login_password = driver.find_element_by_id('ius-password')
login_password.send_keys('MINT_PASSWORD')

sign_in_button = driver.find_element_by_id('ius-sign-in-submit-btn')
sign_in_button.click()

time.sleep(5) # Let the user actually see something!
driver.quit()
 