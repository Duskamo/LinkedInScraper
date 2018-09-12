from BasePages.LinkedInHomePage import *
from Utils.CSVHelper import *


class LinkedInAutomator:
	def __init__(self,scrapingType):
		self.scrapingType = scrapingType
		self.companyTypeList = SEARCH_LIST
		self.outputFile = OUTPUT_FILE
		self.pageNumber = PAGE_NUMBER

	def performScrape(self):
		if (self.scrapingType == "Full"):
			print("Full scrape enabled...")

			self.performFullLinkedInScrape() # LinkedIn limits searches to 100 pages, will implement the specific/partial search instead

			print("Full scrape completed...")
		elif (self.scrapingType == "Partial"):
			print("Partial scrape enabled...")

			self.performPartialLinkedInScrape()

			print("Partial scrape completed...")

	def performFullLinkedInScrape(self):
		""


	def performPartialLinkedInScrape(self):
		linkedInHomePage = LinkedInHomePage()
		linkedInHomePage.open()
		linkedInHomePage.enterCredentials(USERNAME,PASSWORD)

		linkedInUserPage = linkedInHomePage.gotoLinkedInUserPage()
		
		linkedInCompanySearchPage = linkedInUserPage.gotoLinkedInCompanySearchPage()

		for companyType in self.companyTypeList:
			linkedInCompanySearchPage.searchForCompanyType(companyType,self.pageNumber)
			pageCount = linkedInCompanySearchPage.getPageCount()
			
			for pageNumber in range(self.pageNumber,pageCount):
				companiesInfo = linkedInCompanySearchPage.scrapePage(pageNumber)

				CSVHelper.writeCompaniesInfoToFile(companiesInfo,self.outputFile)

				time.sleep(SLEEP_AMOUNT)
				linkedInCompanySearchPage.gotoNextPage(companyType,pageNumber)

				
		
		
