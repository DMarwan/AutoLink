def test_login(mail,password):
	import os

	CHROMEDRIVER_PATH = os.environ.get('CHROMEDRIVER_PATH', '/usr/local/bin/chromedriver')
	GOOGLE_CHROME_BIN = os.environ.get('GOOGLE_CHROME_BIN', '/usr/bin/google-chrome')

	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys
	import time

	try: 
		chrome_options = webdriver.ChromeOptions()
		chrome_options.binary_location = GOOGLE_CHROME_BIN
		chrome_options.add_argument("--window-size=1920,1080");
		chrome_options.add_argument("--start-maximized");
		chrome_options.add_argument('--headless')
		chrome_options.add_argument('--disable-gpu')
		chrome_options.add_argument('--no-sandbox')
		chrome_options.add_argument('--disable-setuid-sandbox')
		browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
		browser.get('https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin')
		login = browser.find_element_by_xpath('//*[@id="username"]').send_keys(mail)
		pwd = browser.find_element_by_xpath('//*[@id="password"]').send_keys(password)
		validation_1 = browser.find_element_by_xpath('//*[@id="app__container"]/main/div/form/div[3]/button').send_keys(Keys.ENTER)
		time.sleep(1.2)
		search = browser.find_element_by_class_name("search-global-typeahead__input")
		
		return True
	
	except:
		return False	
