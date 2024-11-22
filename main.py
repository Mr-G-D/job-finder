from time import sleep

from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests
import mailtrap as mt



load_dotenv()

options = Options()
options.add_argument('--headless')
# options.add_experimental_option("detach", True)

print(os.getenv("chrome_path"))

sender = os.getenv("sender_mail")
receiver = os.getenv("receiver_mail")
token = os.getenv("token")

c_path = os.getenv("chrome_path")

driver = webdriver.Chrome(options=options)

driver.get("https://hiring.amazon.ca/app#/jobSearch?query=montreal&postal=&locale=en-CA")

job_not_found_text = "Sorry, there are no jobs available that match your search."

job_not_found_xpath = "//h1[@class='hvh-careers-emotion-15srwnt']"
search_bar_xpath = "//input[@placeholder='Search jobs']"
search_button_xpath = "//button[@class='e4s17lp0 hvh-careers-emotion-cf0kvy']"
i_consent_button_xpath = "//button[@class='e4s17lp0 hvh-careers-emotion-1ipr55l']"


def send_mail():
    mail = mt.Mail(
        sender=mt.Address(email=sender, name="Amazon Warehouse Jobs"),
        to=[mt.Address(email=receiver)],
        subject="Amazon Warehouse Jobs",
        text="There is an opening at Amazon warehouse",
    )

    client = mt.MailtrapClient(token=token)
    return client.send(mail)


def job_finder():

    while (True):
        try:
            sleep(1)
            try:
                i_consent_button = driver.find_element(By.XPATH, i_consent_button_xpath)
                i_consent_button.click()
            except NoSuchElementException:
                pass

            target = driver.find_element(By.XPATH, job_not_found_xpath).find_element(By.XPATH, './b')
            if target.text == job_not_found_text:
                print("Job Not found")
            else:
                send_mail()
            # search_bar = driver.find_element(By.XPATH, search_bar_xpath)
            # search_bar.click()
            # search_bar.send_keys("Montreal")
            #
            # search_button = driver.find_element(By.XPATH, search_button_xpath)
            # search_button.click()
            sleep(1000)



        except NoSuchElementException as e:
            print("no such element")
            # print(e)
        except Exception as e:
            print(e)



if __name__ == '__main__':
    job_finder()
