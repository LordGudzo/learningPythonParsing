import time
from selenium import webdriver

# Install the driver for Firefox browsers
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

# Create a Firefox webdriver instance with automatic driver installation
browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Navigate to the specified URL
browser.get('https://github.com/mozilla/geckodriver/releases')

# Save a screenshot of the current page as '1.png'
browser.save_screenshot('1.png')

# Refresh the page
browser.refresh()

# Pause execution for 5 seconds (waiting for the page to load or for some other purpose)
time.sleep(5)

# Close the browser window and safely terminate the WebDriver session
browser.quit()