import os
from dotenv import load_dotenv
from helpers.SendText import SendText
from helpers.login import login
from helpers.menu import menu
from helpers.checkout import checkout

class Order():
    load_dotenv()

    def __init__(self, driver, By, WebDriverWait, EC, TimeoutException, env, isFood, isDrink, time, order): 
        url = os.environ.get('URL')
        phone = os.environ.get("PHONE")
        email = os.environ.get("EMAIL")
        password = os.environ.get("PASSWORD")

        # start order modal
        try:
            print('start order ready')
            if time == 'ASAP':
                WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// button[contains(text(), "Start Order")]'))).click()
            elif time == 'Future':
                driver.find_element(By.ID, 'fulfillment_time').click()
            else:
                None
        except TimeoutException:
            print('start order modal timeout')

        # login
        try:
            print('login ready')
            WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// span[contains(text(), "Log In")]'))).click()
            login(driver, By, WebDriverWait, EC, TimeoutException, email, password)
        except TimeoutException:
            print('login timeout')

        # menu
        menu(driver, order, isFood, isDrink, By, WebDriverWait, EC, TimeoutException, email, password)

        # checkout
        checkout(driver, By, WebDriverWait, EC, TimeoutException, phone, email, password, env)
    
        # confirmation text
        if env == 'dev':
            SendText("TEST Order Complete!" + "\nTime: " + time + "\nOrder: " + order)
        else:
            SendText("Online Order Placed!" + "\nTime: " + time + "\nOrder: " + order)
