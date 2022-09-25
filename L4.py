import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options



# 1.
# a. Chrome Driver:
chromedriver = webdriver.Chrome(service=Service("C:/Users/mulik/Downloads/chromedriver.exe"))
# chromedriver.get(r'http://www.walla.co.il')

# # Initialize firefox driver
# firefox_options = FirefoxOptions()
# firefox_options.binary_location = 'C:/Program Files/Mozilla Firefox/firefox.exe'
#
# # b. Firefox driver:
# firefoxdriver = webdriver.Firefox(options=firefox_options)
# firefoxdriver.get("https://www.ynet.co.il")
#
# # 2. In chrome browser using the driver:
# # a. Create a variable with the website’s title
# get_title = chromedriver.title
# print(get_title)
# # b. Refresh website
# chromedriver.refresh()
# # c. Get website name and compare it to the variable you created in clause 1
# if get_title == chromedriver.title:
#     print("equal")

# 4.
# a.
chromedriver.get(r'https://translate.google.com/')
# b.
text = "Hello World - Testing one two three"
chromedriver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz['
                                   '1]/span/span/div/textarea').send_keys(text)

# # 5.
# chromedriver.get(r'https://www.youtube.com/')
# time.sleep(3)
# # a.
# song_name = "Igorrr - Brutal Swing"
# chromedriver.find_element(By.NAME, 'search_query').send_keys(song_name)
# # b.
# chromedriver.find_element(By.ID, 'search-icon-legacy').click()
#
# # 6.
# chromedriver.get(r'https://translate.google.com/')
# a = chromedriver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz['
#                                     '1]/span/span/div/textarea')
# print(a)
# b = chromedriver.find_element(By.TAG_NAME, 'textarea')
# print(b)
# c = chromedriver.find_element(By.CLASS_NAME, 'er8xn')
# print(c)
#
# # 7.
# chromedriver.get(r'https://www.facebook.com/')
# # a.
# chromedriver.find_element(By.XPATH,'//*[@id="email"]').send_keys('myemail@gmail.com')
# chromedriver.find_element(By.XPATH,'//*[@id="pass"]').send_keys('MYPASSWORD', Keys.ENTER)
#
# # 8.
# chromedriver.get('https://en.wiktionary.org/wiki/naughty')
# # a+b. Deleting cookies + Printing
# print(chromedriver.get_cookies())
# chromedriver.delete_all_cookies()
# print(chromedriver.get_cookies())
#
# # 9.
# chromedriver.get(r'https://github.com/')
# # a+b.
# chromedriver.fullscreen_window() # thus in order to show the search bar - there is a hidden menu while the screen
#                                  # size is small
# chromedriver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[2]/div/'
#                                    'div/div[1]/div/div/form/label/input[1]').send_keys('Selenium', Keys.ENTER)
#
# # 10.
# # a.
# chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")
# no_extensions_chromedriver = webdriver.Chrome(service=Service("C:/Users/mulik/Downloads/chromedriver.exe"))
#
# # b.
# # I tried and gave up :)
# # firefox_profile = webdriver.FirefoxProfile()
# # firefox_profile.
# #
# # firefox_options = FirefoxOptions()
# # firefox_options.binary_location = 'C:/Program Files/Mozilla Firefox/firefox.exe'
# # firefox_options.add_argument("--disable-extensions")
# # no_extensions_firefox_driver = webdriver.Firefox(options=firefox_options)
#
# # c.
# # I was too tired to go into it :P
#
# # 11.
# # chrome_options = Options()
# # chrome_options.add_argument("--disable-extensions")
# # no_extensions_chromedriver = webdriver.Chrome(service=Service("C:/Users/mulik/Downloads/chromedriver.exe"))


chromedriver.close()
# firefoxdriver.close()
