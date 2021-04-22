
import time

from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC


from login import loginWrapper


@loginWrapper('one stop pak limited')
def DownloadCrm(browser, wait):
    # click icon
    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '#top-bar > div.hamburger-menu')
    )).click()

    # click CRM
    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '#left-navigation > div.slimScrollDiv > div.sidebar-content > ul > li:nth-child(1) > a')
    )).click()

    # click action
    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '#ActionsLink')
    )).click()

    # click export
    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '#MenuPanelActions > div:nth-child(2) > p > a')
    )).click()

    # click the checkbox of the group selection
    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_M_Members_66')
    )).click()

    # click export button
    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_MemberExportNextButton')
    )).click()

    # click export button
    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_MemberExportSubmitButton')
    )).click()

    time.sleep(10)


if __name__ == "__main__":
    DownloadCrm()
