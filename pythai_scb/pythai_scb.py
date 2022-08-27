from bs4 import BeautifulSoup
import pandas as pd
import datetime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from pythai_scb.exceptions import LoginError, ElementNotFound

SCBEASY_LOGIN_URL = 'https://www.scbeasy.com/v1.4/site/presignon/index.asp'
ACC_COLUMN_MAPPING = [
    'type',
    'acc_no',
    'nickname',
    'balance',
    'date'
]

class ScbCrawler:

    def __init__(self, username: str, password: str):
        phantomjs_path = self._get_phantomjs_path()
        self._browser = webdriver.PhantomJS(executable_path=phantomjs_path)
        self._browser.get(SCBEASY_LOGIN_URL)

        if username is None or password is None:
            raise ValueError('Username and password must be specified')

        self._log_in(username, password)

        # Keep landing page for future features
        # self.landing_page = self.browser.copy()
    def _get_phantomjs_path(self):
        user_os = platform.system()

        if user_os == "Darwin":
            phantomjs_filepath = "phantomjs/phantomjs_mac"
        elif user_os == 'Windows':
            phantomjs_filepath = "phantomjs/phantomjs_windows.exe"
        elif user_os == "Linux":
            user_machine = platform.machine()
            if user_machine == "x86_64":
                phantomjs_filepath = "phantomjs/phantomjs_linux_64" 
            else:       
                phantomjs_filepath = "phantomjs/phantomjs_linux_32" 
        else:
            raise Exception('Unable to determine platform system')

        phantomjs_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), phantomjs_filepath )
        return phantomjs_path

    def _log_in(self, username: str, password: str):
        # Find elements required for logging in
        try:
            username_field = self.browser.find_element_by_xpath("//input[@name='LOGIN']")
            password_field = self.browser.find_element_by_xpath("//input[@name='PASSWD']")
            login_button = self.browser.find_element_by_xpath("//input[@name='lgin']")
        except NoSuchElementException as err:
            raise ElementNotFound(err)

        # Enter username and password
        username_field.send_keys(username)
        password_field.send_keys(password)

        # Click login button
        login_button.click()

        # Check if logging-in is successful
        try:
            logout_button = self.browser.find_element_by_xpath("//img[@name='Image2']")
        except NoSuchElementException as err:
            # The absence of logout button means login failure
            raise LoginError('Unable to login with the provided username and password')
    
    def get_account_bal(self):
        # Find my account button
        my_account_button = self.browser.find_element_by_xpath("//img[@name='Image3']")
        my_account_button.click()

        # Look up for My accont table
        soup = BeautifulSoup(self.browser.page_source, features='html.parser')
        try:
            table_view = soup.find(id="DataProcess_SaCaGridView")
            tr_list = table_view.find_all('tr', {'class': "bd_th_blk11_rtlt10_tpbt5"})
            acc_list = []

            # Iterate over the table and extract account balacne information
            for tr in tr_list:
                table = tr.findChild('table')
                td_list = table.findChildren('td')
                list = []
                for td in td_list:
                    text = td.text.replace('\n','').strip(' ')
                    list.append(text)
                acc_list.append(list)
        except AttributeError as err:
            raise ElementNotFound(err)

        # Format data to dict
        acc_dict = {}
        for acc in acc_list:
            acc_no = acc[1]
            acc_dict[acc_no] = {}
            for idx in range(len(ACC_COLUMN_MAPPING)):
                acc_dict[acc_no][ACC_COLUMN_MAPPING[idx]] = acc[idx]
            acc_dict[acc_no]['balance'] = acc_dict[acc_no]['balance'].replace(',', '')
            acc_dict[acc_no]['date'] = datetime.date.today()

        return acc_dict

    def get_account_bal_df(self):
        acc_idct = self.get_account_bal()

        bank_df = pd.DataFrame.from_dict(acc_idct, orient='index')

        return bank_df