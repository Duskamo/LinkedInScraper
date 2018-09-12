
from BasePages.LinkedInCompanySearchPage import *

class LinkedInUserPage:
	def __init__(self):
		""

	def gotoLinkedInCompanySearchPage(self):
		self.driver.get('https://www.linkedin.com/search/results/companies/v2/')

		linkedInCompanySearchPage = LinkedInCompanySearchPage()
		linkedInCompanySearchPage.driver = self.driver

		return linkedInCompanySearchPage
