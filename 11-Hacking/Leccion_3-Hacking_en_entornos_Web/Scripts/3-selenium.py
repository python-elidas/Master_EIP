from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy, ProxyType

def getDriver(proxyserver=None, proxyport=None, proxyType="SSL"):
	proxyType = proxyType.lower()
	fp = webdriver.FirefoxProfile()
	if proxyType == "http":
		fp.set_preference("network.proxy.type", 1)
		fp.set_preference("network.proxy.http", proxyserver)
		fp.set_preference("network.proxy.http_port", int(proxyport))

		fp.set_preference("network.proxy.type", 1)
		fp.set_preference("network.proxy.ssl", proxyserver)
		fp.set_preference("network.proxy.ssl_port", int(proxyport))

	elif proxyType == "socks":
		fp.set_preference("network.proxy.socks_version", 5)
	fp.update_preferences()
	return webdriver.Firefox(firefox_profile=fp)

def check_exists_by_xpath(webDriver, xpath):
    try:
        webDriver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


webDriver = getDriver()
webDriver.get("https://www.youtube.com/watch?v=tVjcotgB-uQ")
webDriver.implicitly_wait(5)
genericAccept = check_exists_by_xpath(webDriver, '//*[@id="button"]')
if genericAccept:
	webDriver.implicitly_wait(15)
	webDriver.find_element_by_xpath('//*[@id="button"]').click()
webDriver.find_element_by_id("player-container").click()
print(webDriver.get_cookies())

