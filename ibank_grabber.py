import getpass
from contextlib import contextmanager
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of

@contextmanager
def wait_for_page_load(driver, timeout=30):
    old_page = driver.find_element_by_tag_name('html')
    yield
    WebDriverWait(driver, timeout).until(
        staleness_of(old_page)
    )

def login():
    user = input("login: ")
    pswd = getpass.getpass('password:')

    return user, pswd

user, pwd = login()

chromedriver = "E:/dddd/chromedriver_win32/chromedriver.exe"
#chromeOptions = webdriver.ChromeOptions()
#prefs = {"download.default_directory" : "/some/path"}
#chromeOptions.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=None)
driver.implicitly_wait(10) # seconds
driver.get("https://online.binbank.ru")

login = driver.find_element_by_id("login")
login.send_keys(user)

password = driver.find_element_by_id("password")
password.send_keys(pwd)

with wait_for_page_load(driver):
    password.submit()

balance = driver.find_element_by_xpath("//div[@id='topmenu']//span[@class='current']")
print(balance.text)

accounts_link = driver.find_element_by_link_text('Карты и счета')
with wait_for_page_load(driver):
    accounts_link.click()

account_history_link = driver.find_element_by_xpath("//div[@class='accounts-list']/div[@class='account-history']//a")
with wait_for_page_load(driver):
    account_history_link.click()

period_start_field = driver.find_element_by_name("periodStartField")
period_start_field.click() # !!!
WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//div[@id='ui-datepicker-div']"))
period_start_field.clear()
period_start_field.send_keys("01.03.2016")

period_end_field = driver.find_element_by_name("periodEndField")
period_end_field.click() # !!!
WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//div[@id='ui-datepicker-div']"))
period_end_field.clear()
period_end_field.send_keys("31.03.2016")
with wait_for_page_load(driver):
    period_end_field.submit()

rows = driver.find_elements_by_xpath("//div/div/div[@class='table-wrap']/table/tbody")
for r in rows:
    tr = r.find_elements_by_tag_name('tr')
    tds = tr[0].find_elements_by_tag_name('td')
    if tds:
        #Дата операции
        tds[0].text

        #Сумма
        tds[1].text

        #Детали операции
        tds[2].text

# история операций
payments_history = driver.find_element_by_link_text('История операций')
with wait_for_page_load(driver):
    payments_history.click()

extended_search = driver.find_element_by_xpath("//div[@id='wrapper']/div[@class='inner']/a")
extended_search.click()

from_date = driver.find_element_by_name("fromDate")
from_date.click() # !!!
WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//div[@id='ui-datepicker-div']"))
from_date.clear()
from_date.send_keys("01.03.2016")

to_date = driver.find_element_by_name("toDate")
to_date.click() # !!!
WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//div[@id='ui-datepicker-div']"))
to_date.clear()
to_date.send_keys("31.03.2016")

with wait_for_page_load(driver):
    to_date.submit()

rows = driver.find_elements_by_xpath("//div[@class='table-wrap']/table/tbody/tr")
for r in rows:
    tds = r.find_elements_by_tag_name('td')
    if tds:        
        # Операция
        tds[0]

        # Состояние
        tds[1].find_element_by_tag_name('a').get_attribute("title")

        #Сумма
        tds[2]

        #Детали операции
        tds[3]

driver.quit()