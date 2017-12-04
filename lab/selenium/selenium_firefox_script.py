"""Example: Selenium"""
# Pre-Condition: Install selenium bindings
# - pip install selenium
import os
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

# Set browser driver path
binary_path = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'driver', 'geckodriver.exe')
print('# Binary path: ' + binary_path)
driver = webdriver.Firefox(executable_path=binary_path)
# Goto page
driver.get("https://henriquebreda.github.io/")
# Validate title
assert "or not" in driver.title

# Close driver
driver.close()
