from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://agile.endo.strykercorp.com/')

search = browser.find_element_by_name('j_username')
search.send_keys("grussell")

raw_input()