from selenium import webdriver

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
# driver.get("https://www.amazon.co.uk/Schwinn-Surge-Mountain-Bike-Aluminium/dp/B08PCQR21Y/ref=sr_1_1_sspa?dchild=1&keywords=bicycle&qid=1630521549&sr=8-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFNQjg4RzBVM1A5SzEmZW5jcnlwdGVkSWQ9QTA2NjU1NjdNVjhUMjdZNFNDMlcmZW5jcnlwdGVkQWRJZD1BMDcwNTUyNzJXWEFTOTA0NVBSNDAmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl&th=1")

# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)

# documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

# accept_cookies = driver.find_element_by_id('sp-cc-accept').click()

dict = {}

event_times = driver.find_elements_by_css_selector(".blog-widget li time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")
events = {}
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }
print(events)
# driver.close()
driver.quit()