import time
import random
import threading
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# ------- CONFIGURATION -------
NUM_THREADS = 30
NUM_ACTIONS_PER_THREAD = 10  
WEBSITE_URL = "https://pykale.streamlit.app/"
ASSISTANT_QUESTIONS = [
    "Who created PyKale?",
    "What is PyKale?",
]


def create_browser():
    """
    Create a headless Chrome browser instance.
    """

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--log-level=3")


    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    return driver

def action_visit_homepage(driver):
    """
    Action: visit the homepage.
    """
    driver.get(WEBSITE_URL)

    try:
        WebDriverWait(driver, 25).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="80500b10"]'))
        )
        print("[action_visit_homepage] Page loaded successfully!")
    except TimeoutException:
        print("[action_visit_homepage] ERROR: Timed out waiting for element")

    time.sleep(random.uniform(3, 7))
    
def action_ask_assistant(driver):
    """
    Action: go to the assistant page, input a question, and simulate asking a question.
    """


def action_video_demo(driver):
    """
    Action: go to the video demo page and run the basic loading video demo
    """


def simulate_user(thread_id):
    """
    Each thread runs a sequence of random actions.
    """
    print(f"[Thread {thread_id}] Starting browser...")
    driver = create_browser()


    action_visit_homepage(driver)


    driver.quit()
    print(f"[Thread {thread_id}] Done.")

def main():
    threads = []
    for i in range(NUM_THREADS):
        t = threading.Thread(target=simulate_user, args=(i,))
        threads.append(t)

    print("[Main] Starting all threads...")
    for t in threads:
        t.start()

    print("[Main] Waiting for all threads to finish...")
    for t in threads:
        t.join()

    print("[Main] All done!")

if __name__ == "__main__":
    main()
