import json

import time

from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC


from login import loginWrapper

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
    "scaling": 104,
    "scalingType": 3,
    "scalingTypePdf": 3,
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


@loginWrapper(prefs, location="one stop pak limited", )
def print_wp(browser, wait):
    page = 0
    flag = True

    # customer_reference_number = ['C','M','W','E','S','N','SS','S+','E+']

    # burger
    wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#top-bar > div.hamburger-menu.active')
        )
    ).click()

    # sales
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR,
             '#left-navigation > div.slimScrollDiv > div.sidebar-content > ul > li:nth-child(6) > div')
        )
    ).click()

    # sales order
    wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR,
             '#left-navigation > div.slimScrollDiv > div.sidebar-content > ul > li.nav-item.has-child.active > ul > li:nth-child(1) > a')
        )
    ).click()

    time.sleep(1)
    # ========================================================
    # click To Print
    wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_GroupCheckBoxList > tbody > tr > td:nth-child(3) > label')
        )
    ).click()
    # input the district (which will be printed)
    customer_number = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR,
             '#SearchSubPanel1 > table > tbody > tr:nth-child(1) > td:nth-child(1) > table > tbody > '
             'tr:nth-child(7) > td.CustomSearchInput > input[type=text]')
        )
    )
    customer_number.clear()
    customer_number.send_keys("C")

    # search
    wait.until((
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_SearchButton')
        )
    )).click()

    time.sleep(5)

    # click all selected
    browser.find_element(By.CSS_SELECTOR,
                         '#ctl00_ContentPlaceHolder1_OrdersListGridView_ctl01_SelectAllCheckBox').click()

    actions = ActionChains(browser)

    action_btn = browser.find_element(By.CSS_SELECTOR, '#ActionsLink')
    actions.move_to_element(action_btn).click(action_btn).perform()

    # click print invoices
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#MenuPanelActions > div:nth-child(17) > p > a')
        )
    ).click()

    time.sleep(30)
    browser.execute_script('document.title="my_test_file1.pdf";window.print();')


if __name__ == "__main__":
    print_wp()
