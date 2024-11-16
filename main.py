
from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By



load_dotenv()

print(os.getenv("chrome_path"))

c_path = os.getenv("chrome_path")

driver = webdriver.Chrome()

driver.get("https://hiring.amazon.com/search/warehouse-jobs#/")


job_not_found = "jobNotFoundContainer"

try:
    ele = driver.find_element(By.CLASS_NAME, job_not_found)
    if(ele.size != 0):
        print("Jobs not found")
except NoSuchElementException:
    print("Jobs found")
except Exception as e:
    print(e)