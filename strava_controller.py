from dotenv import dotenv_values
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.firefox import GeckoDriverManager

class StravaController:
    def __init__(self) -> None:
        options=Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        executable = GeckoDriverManager().install()
        self.driver = webdriver.Firefox(
            service=Service(executable_path=executable), 
            options=options
        )
        self.secrets = dotenv_values(".env")
    
    def find_by_id_and_send_keys(self, id: str, keys: str) -> None:
        element = self.driver.find_element(By.ID, id)
        element.send_keys(keys)

    def find_textarea_and_send_keys(self, keys: str) -> None:
        element = self.driver.find_element(By.TAG_NAME, "textarea")
        element.send_keys(keys)

    def find_by_arbitrary_and_click(self, by: str, id: str) -> None:
        try:
            element = self.driver.find_element(by, id)
            element.click()
        except NoSuchElementException:
            print(f"Could not find {id} by {by}")

    def login(self):
        self.driver.get("https://www.strava.com/login")
        sleep(3)
        self.find_by_id_and_send_keys("email", self.secrets["STRAVA_EMAIL"])
        self.find_by_id_and_send_keys("password", self.secrets["STRAVA_PASSWORD"])
        self.find_by_arbitrary_and_click(By.ID, "login-button")
        sleep(3)

    def give_kudos(self, activity_id: int) -> None:
        self.driver.get(f"https://www.strava.com/activities/{activity_id}")
        sleep(3)
        self.find_by_arbitrary_and_click(By.XPATH, '//*[text()="Give kudos"]')
        sleep(1)

    def post_comment(self, activity_id: int, comment: str) -> None:
        self.driver.get(f"https://www.strava.com/activities/{activity_id}")
        sleep(3)
        self.find_by_arbitrary_and_click(By.XPATH, "//button[contains(@class, 'ADPKudosAndComments')]")
        sleep(1)
        self.find_by_arbitrary_and_click(By.XPATH, "//button[contains(text(), 'Comments')]")
        sleep(1)
        self.find_textarea_and_send_keys(comment)
        sleep(1)
        self.find_by_arbitrary_and_click(By.XPATH, "//button[contains(text(), 'Post')]")
        sleep(1)
