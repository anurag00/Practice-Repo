from selenium import webdriver
browser = webdriver.Firefox()
browser.get("https://www.amazon.in/")
searchElem = browser.find_element_by_css_selector('#twotabsearchtextbox')
searchElem.send_keys('laptop')
searchElem.submit()
priceElem = browser.find_elements_by_class_name('a-size-base a-color-price s-price a-text-bold')
for x in priceElem:
    print(x.text)
#browser.quit()
#elem = browser.find_element_by_css_selector('body > div.main > div:nth-child(1) > ul:nth-child(18) > li:nth-child(1) > a')
#elem.click()
#elems = browser.find_element_by_css_selector('p')
