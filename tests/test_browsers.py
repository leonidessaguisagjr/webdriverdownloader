from webdriverdownloader.webdriverdownloader import GeckoDriverDownloader, ChromeDriverDownloader, OperaChromiumDriverDownloader
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions


def test_firefox():
    _, geckodriver_path = GeckoDriverDownloader().download_and_install()
    options = FirefoxOptions()
    options.headless = True
    driver = webdriver.Firefox(executable_path=geckodriver_path, options=options)
    assert driver
    driver.close()

def test_chrome():
    _, chromedriver_path = ChromeDriverDownloader().download_and_install()
    options = ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)
    assert driver
    driver.close()


