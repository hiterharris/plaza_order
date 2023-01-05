def checkout(driver, By, WebDriverWait, EC, TimeoutException, phone, email, password, env):
    print("env: ", env)
    try:
        print("checkout ready")
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// span[contains(text(), "Continue to checkout")]'))).click()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "customer_first_name"))).send_keys("Henry")
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "customer_last_name"))).send_keys("Harris")
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "customer_tel"))).send_keys(phone)
        print("ready to submit")
        if env == 'prod':
            WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// button[@data-testid="submit-button"]'))).click()
            WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// h2[contains(text(), "Order Sent")]')))
            WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// button[contains(text(), "Back To Menu")]'))).click()
            print("order submit complete")
        else:
            WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// button[@data-testid="submit-button"]')))
            print("order not submitted")
    except TimeoutException:
        print("checkout timeout")