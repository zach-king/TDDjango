from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

caps = DesiredCapabilities.FIREFOX
caps["marionette"] = True
caps["binary"] = "C:/Program Files (x86)/Mozilla Firefox/firefox.exe"

browser = webdriver.Firefox(capabilities=caps)
browser.get('http://localhost:8000')

assert 'Django' in browser.title
