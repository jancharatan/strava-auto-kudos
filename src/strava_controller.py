from dotenv import dotenv_values
from time import sleep
from selenium_utils import handle_selenium_exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
    
    @handle_selenium_exceptions()
    def find_by_arbitrary_and_send_keys(self, by: str, value: str, keys: str) -> None:
        field_password = next(element for element in self.driver.find_elements(by=by, value=value) if element.is_displayed())
        field_password.send_keys(keys)
        field_password.send_keys(Keys.ENTER)

    @handle_selenium_exceptions()
    def find_textarea_and_send_keys(self, keys: str) -> None:
        element = self.driver.find_element(By.TAG_NAME, "textarea")
        element.send_keys(keys)

    @handle_selenium_exceptions()
    def find_by_arbitrary_and_click(self, by: str, id: str) -> None:
        element = self.driver.find_element(by, id)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def login(self):
        self.driver.get("https://www.strava.com/login")
        sleep(10)
        self.find_by_arbitrary_and_send_keys(By.XPATH, './/*[@data-cy="email"]', self.secrets["STRAVA_EMAIL"])
        sleep(2)
        self.find_by_arbitrary_and_send_keys(By.XPATH, './/*[@data-cy="password"]', self.secrets["STRAVA_PASSWORD"])
        sleep(1)

    def give_kudos(self, activity_id: int) -> None:
        self.driver.get(f"https://www.strava.com/activities/{activity_id}")
        sleep(3)
        self.find_by_arbitrary_and_click(By.XPATH, "//button[text()='Give kudos']")
        sleep(1)

    def post_comment(self, activity_id: int, comment: str) -> None:
        self.driver.get(f"https://www.strava.com/activities/{activity_id}")
        sleep(3)
        self.find_by_arbitrary_and_click(By.XPATH, "//button[contains(text(), 'ADPKudosAndComments')]")
        sleep(1)
        self.find_by_arbitrary_and_click(By.XPATH, "//button[contains(text(), 'Comments')]")
        sleep(1)
        self.find_textarea_and_send_keys(comment)
        sleep(1)
        self.find_by_arbitrary_and_click(By.XPATH, "//button[contains(text(), 'Post')]")
        sleep(1)
