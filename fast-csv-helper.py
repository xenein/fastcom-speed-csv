#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from time import sleep
from os import path

import datetime

driver_path = "/opt/homebrew/Cellar/geckodriver/0.28.0/bin/geckodriver"
data_path = "~/fast/"
csv_file = "fast.csv"

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options, executable_path=driver_path)

start = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
driver.get("https://fast.com/")

# wait for and collect download speed
download_speed = ""
while download_speed == "":
    sleep(10)
    elem = driver.find_element_by_id("speed-value")
    print(elem.text)
    if "succeeded" in elem.get_attribute("class"):
        units = driver.find_element_by_id("speed-units").text
        download_speed = f"{elem.text} {units}"

# click magic button to make upload 
driver.find_element_by_id("show-more-details-link").click()

# wait for and collect upload speed
upload_speed = ""
while upload_speed == "":
    sleep(10)
    elem = driver.find_element_by_id("upload-value")
    if "succeeded" in elem.get_attribute("class"):
        units = driver.find_element_by_id("upload-units").text
        upload_speed = f"{elem.text} {units}"

# collect latency and bufferbloat information
latency = f"{driver.find_element_by_id('latency-value').text} {driver.find_element_by_id('latency-units').text}"
bufferbloat = f"{driver.find_element_by_id('bufferbloat-value').text} {driver.find_element_by_id('bufferbloat-units').text}"
        
# collect static information (Server location, Client info)
client_location = f"{driver.find_element_by_id('user-location').text}"
client_ip = f"{driver.find_element_by_id('user-ip').text}"
client_isp = f"{driver.find_element_by_id('user-isp').text}"
server_info = f"{driver.find_element_by_id('server-locations').text}"

if path.isdir(data_path):
    if not path.isfile(path.join(data_path, csv_file)):
        with open(path.join(data_path, csv_file), mode="x") as fp:
            fp.write(
               "start\tclient_location\tclient_ip\tclient_isp\tserver_info\tlatency\tbufferbloat\tdownload_speed\tupload_speed\tscreenshot\n"
            )
    screenshot_name = f"fast_{start.replace(':','.').replace(' ','_')}.png"
    driver.get_screenshot_as_file(path.join(data_path, screenshot_name))
    with open(path.join(data_path, csv_file), mode="a") as fp:
        fp.write(
            f"{start}\t{client_location}\t{client_ip}\t{client_isp}\t{server_info}\t{latency}\t{bufferbloat}\t{download_speed}\t{upload_speed}\t{screenshot_name}\n"
        )
else:
    print(f"Download Speed: {download_speed}\nUpload Speed: {upload_speed}")

driver.close()
