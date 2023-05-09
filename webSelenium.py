from selenium import webdriver
from selenium.webdriver.chrome.service import Service

path = 'C:\\webdrivers\\chromedriver.exe'
chrome_path = '/mnt/c/Program Files/Google/Chrome/Application/chrome.exe'

options = webdriver.ChromeOptions()
options.binary_location = chrome_path
options.add_argument('--remote-debugging-port=9222')

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)

web = 'https://en.wikipedia.org/wiki/1982_FIFA_World_Cup'
driver.get(web)


#C:\Program Files\Google\Chrome\Application