import time
from selenium import webdriver
driver = webdriver.Chrome('C:/Users/phuongcao12691/Downloads/chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('https://google.com/')
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(1) # Let the user actually see something!
driver.quit()
