import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import requests
# Setup WebDriver path and options
paths = r"D:\Automation study\Python Programming\Requirement\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
time.sleep(2)
# Navigate to the URL
driver.get("https://jqueryui.com/droppable/")
driver.maximize_window()
# Navigate to the Iframe
driver.switch_to.frame(0)
# Find the Dragglable and Droppable elements using find element
Dragglable =driver.find_element(By.ID,"draggable")
Droppable=driver.find_element(By.ID,"droppable")
time.sleep(3)
# Perform drag drop operations using Action chain
actions = ActionChains(driver)
time.sleep(5)
actions. drag_and_drop(Dragglable,Droppable)
actions. perform()
time. sleep(5)