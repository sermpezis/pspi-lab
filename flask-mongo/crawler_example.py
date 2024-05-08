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


url = "https://www.york.ac.uk/teaching/cws/wws/webpage1.html"

options = Options()
options.headless = True # does not apper as window


### in case of Windows:
# driver = webdriver.Chrome(options=options)
### in case of Ubuntu without Chrome driver, the following can be used:
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


driver.get(url) # goes to the specified url
elements = driver.find_elements(By.TAG_NAME, "p") # takes all html elements inside paragraph tag
res = []
for element in elements:
    res.append(element.text) #takes the text from the paragraph tags


# Print the results
for i,r in enumerate(res):
    print(f'#### paragraph {i} ####')
    print(r)
    print('')
