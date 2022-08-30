from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import json


url = os.getenv("LT_HUB_URL")
capabilities = {
    options = ChromeOptions()
    options.browser_version = "105.0"
    options.platform_name = "Windows 10"
    lt_options = {};
    lt_options["username"] = "iftikhar.ali";
    lt_options["accessKey"] = "lSat25gba2v3lGGYFSBXnm9ShHQUi2grrh2rNGG7IYSeLwCsQ0";
    lt_options["project"] = "Untitled";
    lt_options["w3c"] = True;
    lt_options["plugin"] = "python-python";
    options.set_capability('LT:Options', lt_options);
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
