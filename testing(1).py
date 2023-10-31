from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random
import time

driver = webdriver.Chrome()

pages = []
   

def generateRandomString():
    randomString = []
    textFile = open(r"C:\Users\raikk\Desktop\wordlist.txt")
    textLines = textFile.readlines()
    while len(randomString) <= 2:
        random_number = random.randint(1, len(textLines))
        randomString.append(textLines[random_number])
    finalString = ' '.join(randomString)
    return finalString

def connectToYoutube():
    driver.get("https://www.youtube.com/")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    cookie_accept_button = driver.find_element(By.XPATH, '//button[@aria-label="Accept the use of cookies and other data for the purposes described"]')
    cookie_accept_button.click()
    
def searchOnYoutube(query):
    searchBar = driver.find_element(By.NAME, 'search_query')
    searchBar.clear()
    for word in query.split():
        searchBar.send_keys(word)
        time.sleep(1) 
        searchBar.send_keys(Keys.SPACE)
    searchBar.send_keys(Keys.RETURN)

def clickVideo(x):
        video = WebDriverWait(driver, 4).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".style-scope:nth-child(1) > #dismissible #video-title > .style-scope:nth-child(2)"))
        )
        time.sleep(2)
        video.click()
        time.sleep(2)
        pages.append(driver.current_url)
try:
    connectToYoutube()
    while len(pages) < 5:
        searchQuery = generateRandomString()
        time.sleep(2)
        searchOnYoutube(searchQuery)
        time.sleep(2)
        clickVideo(searchQuery)
    print(pages)
except Exception as e:
    print(f"Caught exception: {e}")

driver.close()