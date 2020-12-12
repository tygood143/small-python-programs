''' Bot that opens a chrome browser, goes to 
typeracer.com, enters a practice match 
and types in the passage autoomatically'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
#navigates to typeracer.com and clicks on practice button
driver = webdriver.Chrome('/Users/tylergood/Downloads/chromedriver')
driver.get('https://typeracer.com')
#makes sure button loads, quits if it doesn't
timeout = 3
time.sleep(4)
try:
    button = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@id="gwt-uid-2"]/a')))
except TimeoutException:
    driver.quit()
    print('button did not load')
#clicks button
ActionChains(driver).click(button).perform()
time.sleep(5)
typee = driver.find_element_by_xpath('//*[@id="gwt-uid-17"]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/input')
#adds passsage to list
a = True
b = []
while a:
    try:
        for i in range(1,10):
            text = driver.find_element_by_xpath(f'//*[@id="gwt-uid-17"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[{i}]').text
            b.append(text)
    except:
        a = False
#first letter is always stored in a different html element
# makes sure that if first word is longer than 1 letter, 
# it won't be sepperated from the rest of the word 
if len(b) == 3:
    d = []
    q = ''.join(b[0:2])
    d.append(q)
    d.append(b[2])
    text = ' '.join(d)
else:
    text = ' '.join(b)
#types in passage
actions = ActionChains(driver)
actions.move_to_element(typee)
actions.send_keys(text)
actions.perform()
time.sleep(3)
driver.quit()