import time
from selenium import webdriver

# driver = webdriver.Chrome('/path/to/chromedriver')  # Optional argument, if not specified will search path.
driver = webdriver.Chrome()
driver.get('https://money.yodlee.com/pfm3/home');
 # Let the user actually see something!
login_id = driver.find_element_by_id('loginid')
login_id.send_keys('login')
login_password = driver.find_element_by_id('password')
login_password.send_keys('login_password')

#search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()
 