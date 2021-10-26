import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pyautogui
from PIL import ImageGrab, Image

GAME_OVER_PICTURE_PIL = Image.open("game_over.png")
REGION = (650, 270, 600, 160)

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(chrome_options=chrome_options, service=s)
driver.maximize_window()
driver.get('https://elgoog.im/t-rex/')
time.sleep(1)
htmlElem = driver.find_element(By.CSS_SELECTOR, "html")
htmlElem.send_keys(Keys.SPACE)
pyautogui.moveTo(820, 398)
game = True
while game:
    image = pyautogui.screenshot()
    if pyautogui.pixelMatchesColor(820, 398, (83, 83, 83), tolerance=100):
        pyautogui.press('space')
    elif pyautogui.locateOnScreen(GAME_OVER_PICTURE_PIL, grayscale=True, region=REGION):
        driver.close()
        game = False
