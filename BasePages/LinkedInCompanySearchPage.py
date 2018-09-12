import time

from Config import *
from Models.Company import *


class LinkedInCompanySearchPage:
	def __init__(self):
		""

	def searchForCompanyType(self,companyType,pageNumber):
		self.companyType = companyType
		self.driver.get("https://www.linkedin.com/search/results/companies/v2/?keywords={0}&origin=GLOBAL_SEARCH_HEADER&page={1}".format(companyType,pageNumber))

	def getPageCount(self):
		companyCountText = self.driver.find_element_by_xpath("//div[@class='display-flex']/div/div/div/h3").text

		companyCount = int(companyCountText.split(" ")[1].replace(",",""))
		pageCount = int((companyCount / 10))

		return pageCount

	def scrapePage(self,pageNumber):
		ITEM_COUNT = 10
		self.companyList = []

		for i in range(ITEM_COUNT):
			# Find the items industry type on the main scraping page
			itemIndustry = self.driver.find_elements_by_xpath(".//ul[contains(@class,'search-results__list') and contains(@class,'list-style-none')]/li[contains(@class,'search-result') and contains(@class,'ember-view')][{0}]//*[contains(@class,'subline-level-1')]".format(i+1))

			if (itemIndustry):
				if (itemIndustry[0].text == self.companyType):
					time.sleep(SLEEP_AMOUNT)
					# Find Item link and name on main scraping page
					itemNameLink = self.driver.find_elements_by_xpath(".//ul[contains(@class,'search-results__list') and contains(@class,'list-style-none')]/li[contains(@class,'search-result') and contains(@class,'ember-view')][{0}]//a[contains(@class,'ember-view')]/h3".format(i+1))

					# Add item company name and industry type to model
					self.addBasicInfoToModelAndNavigateToCompanySite(itemNameLink)

					# Open tabs for scraping
					self.openTabsForScrapingWebsiteInfo()

					# Scrape the remaining information
					self.scrapeCompanySiteRemainingInfo()

					# Add model to company list
					self.companyList.append(self.company)

					self.goBackToBasicCompanyListPage(self.companyType,pageNumber)

		return self.companyList

	def addBasicInfoToModelAndNavigateToCompanySite(self,itemNameLink):
		self.company = Company()
		self.company.industry = self.companyType
		if (itemNameLink):
			self.company.name = itemNameLink[0].text

			# Navigate to individual items page
			itemNameLink[0].click()

		time.sleep(SLEEP_AMOUNT)

	def openTabsForScrapingWebsiteInfo(self):
		seeMoreTab = self.driver.find_elements_by_id("org-about-company-module__show-details-btn")
		if (seeMoreTab):
			seeMoreTab[0].click()
			time.sleep(SLEEP_AMOUNT)

	def scrapeCompanySiteRemainingInfo(self):
		employeeCount = self.driver.find_elements_by_xpath(
			".//a[contains(@class,'org-company-employees-snackbar__details-highlight')]/strong")
		location = self.driver.find_elements_by_xpath(".//span[contains(@class,'org-top-card-module__location')]")
		website = self.driver.find_elements_by_xpath(".//a[contains(@class,'org-about-us-company-module__website')]")

		if (employeeCount):
			self.company.employeeCount = employeeCount[0].text.split(" ")[2]
		if (location):
			self.company.location = location[0].text
		if (website):
			self.company.website = website[0].text

	def goBackToBasicCompanyListPage(self,companyType,pageNumber):
		self.driver.get("https://www.linkedin.com/search/results/companies/v2/?keywords={0}&origin=GLOBAL_SEARCH_HEADER&page={1}".format(companyType,pageNumber))
		time.sleep(SLEEP_AMOUNT)


	def gotoNextPage(self,companyType,pageNumber):
		print("Page = {}".format(pageNumber))
		self.driver.get("https://www.linkedin.com/search/results/companies/v2/?keywords={0}&origin=GLOBAL_SEARCH_HEADER&page={1}".format(companyType,pageNumber+1))
