import os
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

try:
    os.mkdir("steamban-checker")
except:
    pass
if not os.path.exists("steamban-checker/urls.txt"):
    open("steamban-checker/urls.txt", "w").close()
    input('Please enter the profile url in the file "urls.txt" to check profile on VAC/game ban, press enter and run the script again')
    raise "Please restart this script"
if not os.path.exists("steamban-checker/chromedriver.exe"):
    input('Please download chromedriver.exe from the site "https://chromedriver.chromium.org/downloads" to the steamban-checker folder, press enter and run the script again')
    raise "Please restart this script"

with open("steamban-checker/urls.txt", "r") as f:
    urls = f.read().split("\n")
    if urls == [""]:
        input('Please enter the profile url in the file "urls.txt" to check profile on VAC/game ban, press enter and run the script again')
        raise "Please restart this script"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(executable_path="steamban-checker/chromedriver.exe", chrome_options=chrome_options)
os.system("cls")
for url in urls:
    print(url)
    driver.get(url)
    try:
        if WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, '//*[@class="profile_private_info"]'))):
            print("Profile is hidden")
    except:
        try:
            print(WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, '//*[@class="profile_ban"]'))).text)
        except:
            print("VAC/game ban not detected")
    print("\n\n")

driver.quit()
input("Press ENTER for exit")
