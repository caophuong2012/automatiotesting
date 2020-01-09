# Import variables
import common

# Import modules
import time
from selenium import webdriver

print(common.driver_path)

# from selenium import webdriver
base_url=common.site_url
# declare and initialize driver variable
driver=webdriver.Chrome(executable_path=common.driver_path)
# browser should be loaded in maximized window
driver.maximize_window()
# driver should wait implicitly for a given duration, for the element under consideration to load.
# to enforce this setting we will use builtin implicitly_wait() function of our 'driver' object.
driver.implicitly_wait(10) #10 is in seconds
# to load a given URL in browser window
driver.get(base_url)
# test whether correct URL/ Web Site has been loaded or not
assert "Beowulf" in driver.title
# to close the browser
driver.close()