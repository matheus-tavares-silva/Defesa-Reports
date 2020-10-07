import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

__LINK = 'http://www.saude.mt.gov.br/painelcovidmt2/'
__GECKO = 'app/controller/covid/geckodriver'

__XPATH_PANEL = {
    'panel': '/html/body/section/div/div/div/iframe',
    'confirmed': '.visualContainerHost > visual-container-repeat:nth-child(1) > visual-container-modern:nth-child(2) > transform:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > visual-modern:nth-child(2) > div:nth-child(1) > svg:nth-child(2) > g:nth-child(1) > text:nth-child(1)',
    'interned': 'visual-container-modern.visual-container-component:nth-child(32) > transform:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > visual-modern:nth-child(2) > div:nth-child(1) > svg:nth-child(2) > g:nth-child(1) > text:nth-child(1)',
    'recovered': 'visual-container-modern.visual-container-component:nth-child(5) > transform:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > visual-modern:nth-child(2) > div:nth-child(1) > svg:nth-child(2) > g:nth-child(1) > text:nth-child(1)',
    'isolated': 'visual-container-modern.visual-container-component:nth-child(6) > transform:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > visual-modern:nth-child(2) > div:nth-child(1) > svg:nth-child(2) > g:nth-child(1) > text:nth-child(1)',
    'dead': 'visual-container-modern.visual-container-component:nth-child(6) > transform:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > visual-modern:nth-child(2) > div:nth-child(1) > svg:nth-child(2) > g:nth-child(1) > text:nth-child(1)',
}

__XPATH_TABLE = {
    'cities': '.swipeable-blocked > div:nth-child(4) > div:nth-child(1) > visual-modern:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(%)',
    'cases': '.swipeable-blocked > div:nth-child(4) > div:nth-child(1) > visual-modern:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(%)'
}

__BTN_TABLE = '/html/body/div[1]/ui-view/div/div[1]/div/div/div/div/exploration-container/exploration-container-modern/div/div/div/exploration-host/div/div/exploration/div/explore-canvas-modern/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-modern[14]/transform/div/div[3]/div/visual-modern/div/div/div[2]/div[1]/div[2]/div/div[3]'


def panel():
    os.environ['MOZ_HEADLESS'] = '1' #-- Uncomment to show driver
    driver = webdriver.Firefox(executable_path=__GECKO)

    wait = WebDriverWait(driver, 40)

    size = 10

    data = {'confirmed': '', 'interned': '',
            'recovered': '', 'isolated': '', 'dead': '', 'cities': [], 'cases': []}

    try:
        driver.get(__LINK)

        driver.switch_to.frame(wait.until(
            EC.presence_of_element_located((By.XPATH, __XPATH_PANEL['panel']))))

        for key in __XPATH_PANEL:
            if(key in data.keys()):
                data[key] = wait.until(
                    EC.visibility_of_element_located(
                        (By.CSS_SELECTOR, __XPATH_PANEL[key])
                    )
                ).text.replace(',', '.')

        button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, __BTN_TABLE)
            )
        )

        ActionChains(driver).send_keys(Keys.PAGE_DOWN).click(button).pause(5).perform()

        for key in __XPATH_TABLE:
            buffer = []
            for i in range(size):
                element = wait.until(
                    EC.visibility_of_element_located(
                        (By.CSS_SELECTOR, __XPATH_TABLE[key].replace('%', str(i + 1)))
                    )
                )

                buffer.append(element.text.replace(',', '.'))

            data[key] = buffer

    finally:
        driver.quit()

    return data