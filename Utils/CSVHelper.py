
import csv

class CSVHelper:
	@staticmethod
	def writeCompaniesInfoToFile(companiesInfo,outputFile):
		with open(outputFile, 'a', newline='') as csvfile:
			spamwriter = csv.writer(csvfile, delimiter=',',
									quotechar='|', quoting=csv.QUOTE_MINIMAL)
			for company in companiesInfo:
				spamwriter.writerow([company.name, company.industry, company.location, company.employeeCount, company.website])

				print(company.industry)
				print(company.employeeCount)
				print(company.name)
				print(company.location)
				print(company.website)
