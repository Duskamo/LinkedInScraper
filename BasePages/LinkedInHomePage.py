
from selenium import webdriver

from BasePages.LinkedInUserPage import *


class LinkedInHomePage:
	def __init__(self):
		self.url = "https://www.linkedin.com"

	def open(self):
		self.driver = webdriver.Chrome(executable_path="C:\\Users\\dyano\\Google Drive\\Professional\\Projects\\AlexDublin\\ls\\linkedin_scraper\\chromedriver_win32\\chromedriver.exe")
		self.driver.maximize_window()
		self.driver.get(self.url)

	def enterCredentials(self,username,password):
		usernameField = self.driver.find_element_by_id('login-email')
		usernameField.send_keys(username)

		passwordField = self.driver.find_element_by_id('login-password')
		passwordField.send_keys(password)

	def gotoLinkedInUserPage(self):
		signInButton = self.driver.find_element_by_id('login-submit')
		signInButton.click()

		linkedInUserPage = LinkedInUserPage()
		linkedInUserPage.driver = self.driver

		return linkedInUserPage
