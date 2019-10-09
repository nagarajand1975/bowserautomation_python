from selenium import webdriver
browser=webdriver.Chrome('.\\chromedriver_win32\\chromedriver.exe')
browser.get('http://www.google.com')
input=browser.find_element_by_name('q')
input.send_keys('python tutorial')
input.click()
button=browser.find_element_by_name('btnK')
button.click()