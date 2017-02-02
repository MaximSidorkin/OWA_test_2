from selenium import webdriver
import unittest
import autoit
import time
import HTMLTestRunner
import sys
from selenium.webdriver.common.keys import Keys
#
url = 'https://owa.mos.ru/EWS/Exchange.asmx'
login = 'SolovievEV'
password = 'rOURDPTc'

class LetsGo(unittest.TestCase):
    def test_01_letMeIn(self):
        profile = webdriver.FirefoxProfile()
        profile.accept_untrusted_certs = True
        driver = webdriver.Firefox()
        driver.set_page_load_timeout(5)
        print('.')
        driver.maximize_window()
        handle = driver.current_window_handle
        driver.switch_to.window(handle)
        time.sleep(3)
        driver.find_element_by_tag_name('body').send_keys(Keys.F5)
        try:
            driver.get('https://owa.mos.ru/EWS/Exchange.asmx')
            print('..')
        except:
            print('..')
        try:
            time.sleep(5)
            alert = driver.switch_to.alert()
            alert.accept()
        except:
            print('No alert')
        autoit.mouse_click(button='left',x=755,y=453)   # 755, 453  # old x=573,y=233
        #autoit.win_wait_active('Требуется аутентификация')
        autoit.send('SolovievEV')
        autoit.send('{TAB}')
        autoit.send('rOURDPTc')
        autoit.send('{ENTER}')
        time.sleep(10)
        all_r = driver.find_element_by_css_selector('p.heading1')
        if all_r.is_displayed():
            driver.get_screenshot_as_file('ALL_RIGHT.jpg')
            print('All right')
        else:
            driver.get_screenshot_as_file('ERROR.jpg')
            self.fail(print('Service is not available!'))
        driver.close()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(LetsGo))
    # File
    buf = open("at_for_CHECK_OWA_EXCHANGE.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
    stream=buf,
    title='СЕРВИС OWA EXCHANGE НЕДОСТУПЕН',
    description='Отчет по тестированию'
    )
    ret = not runner.run(suite).wasSuccessful()
    sys.exit(ret)
