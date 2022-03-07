from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Start the browser
chrome_options = Options()
chrome_options.add_argument("user-data-dir=selenium")
browser = webdriver.Chrome(options=chrome_options)
