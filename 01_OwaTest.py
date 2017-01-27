from selenium import webdriver
import unittest
import autoit
import time
import HTMLTestRunner
import sys

url = 'https://owa.mos.ru/EWS/Exchange.asmx'
login = 'SolovievEV'
password = 'rOURDPTc'

class LetsGo(unittest.TestCase):
    def test_01_letMeIn(self):
        profile = webdriver.FirefoxProfile()
        profile.accept_untrusted_certs = True
        # final ver.
        driver = webdriver.Firefox()
        driver.set_page_load_timeout(5)
        print('.')
        try:
            driver.get('https://owa.mos.ru/EWS/Exchange.asmx')
            print('..')
        except:
            print('..')
        autoit.win_wait_active('Требуется аутентификация')
        autoit.send('SolovievEV')
        autoit.send('{TAB}')
        autoit.send('rOURDPTc')
        autoit.send('{ENTER}')
        time.sleep(10)
        all_r = driver.find_element_by_css_selector('p.heading1')
        if all_r.is_displayed():
            print('All right')
        else:
            self.fail(print('Service is not available!'))

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
