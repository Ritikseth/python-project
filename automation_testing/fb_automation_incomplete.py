from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')

chrome_browser.maximize_window()
chrome_browser.get('https://www.facebook.com/')

assert 'Facebook – log in or sign up' in chrome_browser.title

show_email_button= chrome_browser.find_element_by_class_name('inputtext login_form_input_box')
# # print(show_message_button.get_attribute('innerHTML'))

# assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id('email')
user_button2 = chrome_browser.find_element_by_css_selector('#get-input > .email')
# print(user_button2)
user_message.clear()
user_message.send_keys('seth@gmail.com')

# show_message_button.click()
# output_message = chrome_browser.find_element_by_id('display')

# assert 'I am a python developer' in output_message.text

# chrome_browser.quit()