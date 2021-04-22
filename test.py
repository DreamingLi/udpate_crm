import json

import pyotp
import time
import re

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

secret_key: str = "ODCAWFCTPO6TVSQUZBEK244GLZS6FHPO"
account: str = "will.zhang@onestoppak.com",
passwd: str = "Welcome#1",
location: str = "one stop pak limited"
chrome_options = webdriver.ChromeOptions()

settings = {
    "recentDestinations": [{
        "id": "Save as PDF",
        "origin": "local",
        "account": "",
    }],
    "selectedDestinationId": "Save as PDF",
    "version": 2,
    "isHeaderFooterEnabled": False,

    # "customMargins": {},
    # "marginsType": 2,
    # "scaling": 100,
    # "scalingType": 3,
    # "scalingTypePdf": 3,
    "isLandscapeEnabled": True,  # landscape横向，portrait 纵向，若不设置该参数，默认纵向
    "isCssBackgroundEnabled": True,
    "mediaSize": {
        "height_microns": 297000,
        "name": "ISO_A4",
        "width_microns": 210000,
        "custom_display_name": "A4 210 x 297 mm",
    },
    "pagesPerSheet": 4,
}
prefs = {
    'printing.print_preview_sticky_settings.appState': json.dumps(settings),
    'savefile.default_directory': 'C:\\Users\\Leo\\Desktop'  # 此处填写你希望文件保存的路径
}
chrome_options.add_argument('--kiosk-printing')  # 静默打印，无需用户点击打印页面的确定按钮
chrome_options.add_experimental_option('prefs', prefs)

with webdriver.Chrome(executable_path='./driver.exe', options=chrome_options) as browser:
    browser.get('https://www.google.com')
    wait = WebDriverWait(browser, 15)

    browser.execute_script('document.title="my_test_file1.pdf";window.print();')
    time.sleep(20)
    # # login
    # username = browser.find_element_by_id("EmailOrUsername")
    # username.send_keys(account)
    # password = browser.find_element_by_id('passwordInput')
    # password.send_keys(passwd)
    # login_button = browser.find_element(By.CSS_SELECTOR, ".btn")
    # login_button.click()
    #
    # # auth_code
    # auth_code = pyotp.TOTP(secret_key).now()
    # auth_box = wait.until(
    #     EC.presence_of_element_located(
    #         (By.XPATH, '//*[@id="Input_TwoFactorCode"]')
    #     )
    # )
    # auth_box.send_keys(auth_code)
    # browser.find_element(By.CSS_SELECTOR, ".btn").click()
