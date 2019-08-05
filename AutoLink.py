##It may fail sometimes. Feel free to adapt to your own need
## @author {DARWISH Marwan, https://github.com/DMarwan, https://www.linkedin.com/in/dmarwan/}

import os

CHROMEDRIVER_PATH = os.environ.get('CHROMEDRIVER_PATH', '/usr/local/bin/chromedriver')
GOOGLE_CHROME_BIN = os.environ.get('GOOGLE_CHROME_BIN', '/usr/bin/google-chrome')

from calltracker import calltracker

@calltracker
def auto_applyer(mail, password, job, location):
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    import time
    print('starting auto_applyer')

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
    time.sleep(1.5)
    jobs = browser.find_element_by_xpath('//*[@id="jobs-nav-item"]/a').click()
    print('logged in successfully')
    time.sleep(1.5)
    position = browser.find_element_by_xpath("//*[@placeholder='Search jobs']").send_keys(job)
    location = browser.find_element_by_xpath("//*[@placeholder='Search location']").send_keys(location)
    validation_2 = browser.find_element_by_xpath("//*[@placeholder='Search location']").send_keys(Keys.ENTER)
    time.sleep(2)
    distance_options = browser.find_element_by_xpath('//*[@aria-controls="distance-facet-values"]').click()
    set_distance_to_10_miles = browser.find_element_by_xpath("//*[@for='distance-10']").click()
    apply_distance = browser.find_element_by_xpath("//*[@data-control-name='filter_pill_apply']").click()
    time.sleep(1.5)
    linkedin_features = browser.find_element_by_xpath("//*[@aria-label='LinkedIn Features filter. Clicking this button displays all LinkedIn Features filter options.']").click()
    easy_apply_only = browser.find_element_by_xpath("//*[@for='f_LF-f_AL']").click()
    validation_3 = browser.find_element_by_xpath("//*[@class='search-s-facet__values search-s-facet__values--is-floating search-s-facet__values--f_LF container-with-shadow']//*[@class='display-flex justify-flex-end mt4']/button[@data-control-name='filter_pill_apply']").click()
    time.sleep(1.5)
    pages = [browser.find_element_by_xpath(f'//*[@aria-label="Page {i}"]') for i in range (2,6)]

    ################### Here we go ! ##############################
    i = -1
    nb_offers = 0
    while i < 5:
        i += 1 
        offers = browser.find_elements_by_xpath('//*[@class="occludable-update artdeco-list__item--offset-4 artdeco-list__item p0 ember-view"]')
        for offer in offers:
            offer.click()
            time.sleep(1)
            easy_apply = browser.find_element_by_xpath("//*[@class='jobs-apply-button--top-card artdeco-button--3 artdeco-button--primary jobs-apply-button artdeco-button ember-view']").click()
            try:
                submit = browser.find_element_by_xpath('//button[@type="submit"]').click()
                time.sleep(1)
                close = browser.find_element_by_xpath('//*[@class="artdeco-modal__dismiss artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--2 artdeco-button--tertiary ember-view"]').click()
                nb_offers += 1
                
                time.sleep(1)
            except: 
                continue
        pages[i].click()
        time.sleep(2)
    print(f'Applyed to {nb_offers} offers !')
    browser.quit()
    return j
    
@calltracker
def auto_connector(mail, password, job):
    
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    import time
    from random import uniform
    
    print('starting auto_connector')
    
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
    time.sleep(1.5)
    search = browser.find_element_by_class_name("search-global-typeahead__input")
    print('logged in successfully')
    search.send_keys(job)
    search.send_keys(Keys.ENTER)
    time.sleep(2)
    people = browser.find_element_by_xpath('//button[@aria-label="View only People results"]').click()
    time.sleep(2)
    connections = browser.find_element_by_xpath('//button[@aria-label="Connections filter. Clicking this button displays all Connections filter options."]').click()
    second = browser.find_element_by_xpath('//label[@for="network-S"]').click()
    time.sleep(1)
    third = browser.find_element_by_xpath('//label[@for="network-O"]').click()
    time.sleep(1)
    apply = browser.find_element_by_xpath('//button[@data-control-name="filter_pill_apply"]').click()
    
    time.sleep(2)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
   
    next_page = browser.find_element_by_xpath('//button[@class="artdeco-pagination__button artdeco-pagination__button--next artdeco-button artdeco-button--muted artdeco-button--icon-right artdeco-button--1 artdeco-button--tertiary ember-view"]')
    time.sleep(1)
    i = 0
    
    #let's go 
    page = 1
    while True:  
        try:
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")   
            time.sleep(1)
    
            to_connect = browser.find_elements_by_xpath("//button[starts-with(@aria-label, 'Connect with')]")

            
            for connect in to_connect:
                
                time.sleep(uniform(1.5,2.5))
                browser.execute_script("arguments[0].scrollIntoView();", connect)
                time.sleep(1.5)
                if connect.get_attribute("disabled") == 'true':
                    continue
                browser.execute_script("arguments[0].click();", connect)             
                time.sleep(uniform(1.5, 2))
                
                if browser.find_element_by_xpath('//button[@class="artdeco-button artdeco-button--3 ml1"]').get_attribute("disabled") == 'true':
                    browser.find_element_by_xpath('//button[@class="send-invite__cancel-btn"]').click()
                    continue
                browser.find_element_by_xpath('//button[@class="artdeco-button artdeco-button--3 ml1"]').click()
                time.sleep(1)
                try:
                    
                    browser.find_element_by_xpath('//button[@data-control-name="fuse_limit_got_it"]').click()
                    browser.quit()
                    print(f'\nJob finished without error. {i} invitations sent.')
                    return i
                except:
                    pass    
                i += 1
                           
            browser.execute_script("arguments[0].scrollIntoView();", next_page)
            time.sleep(uniform(1,1.5))
            next_page.click()
            page += 1
            print(f'\nPage {page}\n')
            time.sleep(1)
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            next_page = browser.find_element_by_xpath('//button[@class="artdeco-pagination__button artdeco-pagination__button--next artdeco-button artdeco-button--muted artdeco-button--icon-right artdeco-button--1 artdeco-button--tertiary ember-view"]')
        except Exception as e:
            print("type error: " + str(e))
            print(f'\nJob finished with an error. {i} invitations sent.')
            break
    browser.quit()
    return 'error'
            
