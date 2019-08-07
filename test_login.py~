def test_login(mail,password):
	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys
	import time

	try: 
		chrome_options = webdriver.ChromeOptions()
		chrome_options.add_argument('--headless')
		chrome_options.add_argument('--no-sandbox')
		chrome_options.add_argument('--disable-setuid-sandbox')
		browser = webdriver.Chrome('/usr/bin/chromedriver', options=chrome_options)
		browser.get('https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin')
		login = browser.find_element_by_xpath('//*[@id="username"]').send_keys(mail)
		pwd = browser.find_element_by_xpath('//*[@id="password"]').send_keys(password)
		validation_1 = browser.find_element_by_xpath('//*[@id="app__container"]/main/div/form/div[3]/button').send_keys(Keys.ENTER)
		time.sleep(1.2)
		search = browser.find_element_by_class_name("search-global-typeahead__input")
		
		return True
	
	except:
		return False	
