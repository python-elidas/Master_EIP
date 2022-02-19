import requests
proxies = {'http': 'socks5h://127.0.0.1:9150',
			'https':'socks5h://127.0.0.1:9150'}
def searcherUnderDir(address):
		#http://underdj5ziov3ic7.onion/search/passport/pg/1
		#http://underdj5ziov3ic7.onion/search/cards/pg/4
		for page in range(1, 4):
			for searchItem in ['guns', 'passports', 'drugs']:
				addressWithCriteria = address.replace("CRITERIA_WILDCARD", searchItem)
				addressToSearch=addressWithCriteria+str(page)
				print(addressToSearch)
				response = requests.get(addressToSearch, proxies=proxies)
				print(response)
				#crawl(addressToSearch, searchCriteriaId=searchItem.id)
#http://underdj5ziov3ic7.onion/search/CRITERIA_WILDCARD/pg/
searcherUnderDir('http://underdiriled6lvdfgiw4e5urfofuslnz7ewictzf76h4qb73fxbsxad.onion/search/CRITERIA_WILDCARD/pg/')
