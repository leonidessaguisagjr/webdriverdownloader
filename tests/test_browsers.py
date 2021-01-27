from selenium import webdriver
from webdriverdownloader import ChromeDriverDownloader


def test_chromedriver():
    src_file, dest_file = ChromeDriverDownloader().download_and_install()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(service_args=["--verbose", "--log-path=/tmp/qc1.log"],
                                      executable_path=src_file,
                                      chrome_options=chrome_options)
    driver.get('http://google.com')
    assert driver.title == 'Google'
