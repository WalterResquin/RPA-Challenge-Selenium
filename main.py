from selenium import webdriver
from  selenium.webdriver.common.by import By
import pyautogui
import pandas as pd
import time

#abre url
browser = webdriver.Chrome()
browser.get("https://rpachallenge.com/")
browser.maximize_window()

#baixa arquivo excel
browser.execute_script("window.scrollBy(0, 500);")
time.sleep(1)
botao_download = pyautogui.locateCenterOnScreen("download.png");
pyautogui.click(botao_download);
#time.sleep(3)

#lê planilha
planilha = r"C:\Users\walter\Downloads\arquivos\challenge.xlsx"
df = pd.read_excel(planilha)

#Clica em Start
browser.find_element(By.XPATH, "//button[contains(text(), 'Start')]").click()

#preenche campos
for index, row in df.iterrows():
    campo_name = browser.find_element(By.XPATH, "//input[@ ng-reflect-name='labelFirstName']")
    campo_name.send_keys(row['First Name'])

    campo_last_name = browser.find_element(By.XPATH, "//input[@ ng-reflect-name='labelLastName']")
    campo_last_name.send_keys(row['Last Name'])

    campo_company = browser.find_element(By.XPATH, "//input[@ ng-reflect-name='labelCompanyName']")
    campo_company.send_keys(row['Company Name'])

    campo_role = browser.find_element(By.XPATH, "//input[@ ng-reflect-name='labelRole']")
    campo_role.send_keys(row['Role in Company'])

    campo_address = browser.find_element(By.XPATH, "//input[@ ng-reflect-name='labelAddress']")
    campo_address.send_keys(row['Address'])

    campo_email = browser.find_element(By.XPATH, "//input[@ ng-reflect-name='labelEmail']")
    campo_email.send_keys(row['Email'])

    campo_phone = browser.find_element(By.XPATH, "//input[@ ng-reflect-name='labelPhone']")
    campo_phone.send_keys(row['Phone Number'])

    #clica em submit
    browser.find_element(By.XPATH, "//input[@type='submit']").click()

time.sleep(5)