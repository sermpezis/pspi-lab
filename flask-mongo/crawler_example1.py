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


url = "https://www.csd.auth.gr/staff/faculty/"

options = Options()
options.headless = True # does not apper as window


### in case of Windows:
# driver = webdriver.Chrome(options=options)
### in case of Ubuntu without Chrome driver, the following can be used:
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get(url) # goes to the specified url
elements = driver.find_elements(By.CLASS_NAME, "uk-grid") # takes all html elements inside paragraph tag
res = []
for element in elements:
   try:
       rank = element.find_element(By.CLASS_NAME, "rank")
       name = element.find_element(By.TAG_NAME, "a")
       if rank.text and name.text:
          full_name = rank.text+' '+name.text
          print(full_name)
       res.append(full_name) #takes the text from the paragraph tags
       # break
   except:
      continue

# Print the results
for i,r in enumerate(res):
    print(f'#### element {i} ####')
    print(r)
    print('')
