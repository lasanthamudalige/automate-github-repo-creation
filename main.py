from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import sys
import os
from dotenv import load_dotenv


# load username and password from env file
load_dotenv()
USERNAME = os.getenv("GITHUB_USERNAME")
PASSWORD = os.getenv("GITHUB_PASSWORD")


def main():
    # If user didn't enter a repo name
    try:
        repo_name = sys.argv[1]

        # Load chrome driver
        driver = webdriver.Chrome()

        # go to github new repo page
        driver.get("https://github.com/new")

        username = driver.find_element(By.NAME, "login")
        username.send_keys(USERNAME)
        sleep(2)
        password = driver.find_element(By.NAME, "password")

        # press enter after entering password
        password.send_keys(PASSWORD + Keys.ENTER)
        sleep(2)

        repo_name_input_box = driver.find_element(By.ID, "repository_name")
        repo_name_input_box.send_keys(repo_name)
        sleep(2)

        create_repo_btn = driver.find_element(
            By.XPATH, '//*[@id="new_repository"]/div[5]/button')
        create_repo_btn.click()

        # wait for an 10 seconds before closing the window
        sleep(10)
        print("Repo created.")

    except IndexError:
        print("Repo name not found")


main()
