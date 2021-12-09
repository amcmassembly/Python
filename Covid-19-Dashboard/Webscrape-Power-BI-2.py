from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
driver = webdriver.Chrome(options=options, executable_path="C:/Users/Aaron/chromedriver_win32/chromedriver.exe")

driver.get("https://app.powerbi.com/view?r=eyJrIjoiODJjOGE3ZDUtM2ViNy00YjBlLTllMjktOTNjZjlkODJhODU4IiwidCI6ImU3YTEzYWVhLTk0MzctNGRiNy1hMjJiLWNmYWE0Y2UzM2I2ZSJ9")

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='navigation-wrapper navigation-wrapper-big']//span[text()='30']"))).click()

time.sleep(10)
discharge_names_parent = driver.find_element(By.XPATH, "//*[@id='pvExplorationHost']//visual-container-repeat/visual-container[@class='visual-container-component']//*[name()='svg' and @class='card']//*[name()='g']//*[name()='text']")
discharge_names_children=discharge_names_parent.find_elements(By.XPATH, "//*")

listofoutput=[]
for value in discharge_names_children:
	listofoutput.append(value.text)

with open('C:/Users/Aaron/OneDrive/Documents/assembly/covid_dashboards/powerbioutput_icu.txt','w') as f:
	f.write('%s\n' %listofoutput[0])		

driver.quit()
