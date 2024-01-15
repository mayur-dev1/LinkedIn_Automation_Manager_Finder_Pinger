from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from utils.Functions import *

FirefoxService= Service(executable_path="./drivers/geckodriver.exe")
driver=webdriver.Firefox(service=FirefoxService)
driver.implicitly_wait(8)