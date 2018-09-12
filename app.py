
import sys

from Utils.LinkedInAutomator import *

# Receieve arguments from terminal
# Valid Arguements: Full | Partial
scrapingType = sys.argv[1] 

# Scrape LinkedIn base off of scraping type
# Full - Compete scraping of all companies in LinkedIn
# Partial - Scraping of compaines belonging to ['Computer Software','Information Technology and Services','Internet','Wireless'] industries. 
linkedInAutomator = LinkedInAutomator(scrapingType)
linkedInAutomator.performScrape()