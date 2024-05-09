from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

'''
For ubuntu (linux) you need to have  Chrome installed. 

You can see how to do it here: https://github.com/password123456/setup-selenium-with-chrome-driver-on-ubuntu_debian

or, quicker (what worked for me, but may not work directly):  
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    dpkg -i google-chrome-stable_current_amd64.deb
    pip3 install webdriver-manager
'''


url = "https://ai4netmon.csd.auth.gr"

options = Options()
options.headless = True # does not apper as window


### in case of Windows:
# driver = webdriver.Chrome(options=options)
### in case of Ubuntu without Chrome driver, the following can be used:
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


driver.get(url) # goes to the specified url
section = driver.find_element(By.ID, "people") # take a specific section of the webpage
elements = section.find_elements(By.TAG_NAME, "a") # take all elements of tag "a" in this section
for element in elements:
	print(element.text)