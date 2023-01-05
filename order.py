import os
import sys
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from helpers.SendText import SendText
from helpers.isAvailable import isAvailable
from helpers.Order import Order

# arguments
load_dotenv()
url = os.environ.get('URL')
available = isAvailable()
env = sys.argv[1]
isFood = sys.argv[2]
isDrink = sys.argv[3]
time = sys.argv[4]
order = sys.argv[5]

# web driver parameters 
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

# start order
if available:
    print("Ordering Available")
    Order(driver, By, WebDriverWait, EC, TimeoutException, env, isFood, isDrink, time, order)
else:
    SendText("Online ordering is currently unavailable")
    print("Ordering Unavailable")
    print("params: ", {
        "env": env,
        "isFood": isFood,
        "isDrink": isDrink,
        "time": time,
        "order": order
    })
    
# end process
driver.quit()