import pyotp
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def loginWrapper(prefs, location="one stop pak limited",):
    secret_key: str = "ODCAWFCTPO6TVSQUZBEK244GLZS6FHPO"
    account: str = "will.zhang@onestoppak.com",
    passwd: str = "Welcome#1",
    browser_options: Options = webdriver.ChromeOptions()
    browser_options.add_argument('--kiosk-printing')  # 静默打印，无需用户点击打印页面的确定按钮
    browser_options.add_experimental_option('prefs', prefs)

    def loginInner(func):

        def login():

            with webdriver.Chrome(executable_path='./driver.exe', options=browser_options) as browser:
                browser.get('https://go.cin7.com/Cloud/Dashboard/HomePageDashboard.aspx')
                wait = WebDriverWait(browser, 15)

                # login
                username = browser.find_element_by_id("EmailOrUsername")
                username.send_keys(account)
                password = browser.find_element_by_id('passwordInput')
                password.send_keys(passwd)
                login_button = browser.find_element(By.CSS_SELECTOR, ".btn")
                login_button.click()

                # auth_code
                auth_code = pyotp.TOTP(secret_key).now()
                auth_box = wait.until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="Input_TwoFactorCode"]')
                    )
                )
                auth_box.send_keys(auth_code)
                browser.find_element(By.CSS_SELECTOR, ".btn").click()

                # select region
                current_location = wait.until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="quick-links"]/div[2]/div[1]/div[2]/span[2]')
                    )
                )

                if location.lower().strip() not in current_location.text.lower().strip():
                    wait.until(EC.element_to_be_clickable(
                        (By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[2]/div[1]/div[2]')
                    )).click()

                    time.sleep(1)
                    wait.until(EC.presence_of_element_located(
                        (By.CSS_SELECTOR,
                         "#quick-links > div.user-container > div.user-panel.active > ul.user-settings > "
                         "li:nth-child(1) > a"))
                    ).click()

                    # select the region, if the current region is the location where we want to be, then back to homepage
                    org = wait.until(
                        EC.presence_of_element_located(
                            (By.CSS_SELECTOR, '#PageContentContainer > div > div > div > table > tbody')
                        )
                    ).find_elements_by_tag_name('tr')

                    for i in org:
                        if location in i.find_element(By.CSS_SELECTOR,
                                                      'td:nth-child(3)  > strong').text.lower().strip():
                            # either (signed in) or select
                            if i.find_element(By.CSS_SELECTOR, 'td:nth-child(1)').text.lower().strip() == "select":
                                i.find_element(By.CSS_SELECTOR, 'td:nth-child(1) > a').click()
                                break
                            else:
                                # left-navigation > div.slimScrollDiv > div.sidebar-content > ul > li:nth-child(8) > a
                                browser.find_element(By.CSS_SELECTOR,
                                                     "#left-navigation > div.logo-section > a").click()
                                break
                    time.sleep(2)

                return func(browser, wait)

        return login

    return loginInner
