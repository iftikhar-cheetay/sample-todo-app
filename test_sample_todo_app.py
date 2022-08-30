from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import json


url = os.getenv("LT_HUB_URL")
capabilities = {
    browser_version = "105.0"
    platform_name = "Windows 10"
    et_capability('LT:Options', lt_options);
}
driver = webdriver.Remote(
    desired_capabilities= capabilities,
    command_executor= url
)
driver.get("http://localhost:8081/")
driver.find_element_by_name("li3").click()

textbox = driver.find_element_by_id("sampletodotext")
textbox.send_keys("Testing")
driver.find_element_by_id("addbutton").click()
assert "No results found." not in driver.page_source
driver.execute_script("lambda-status=passed")
driver.quit()
