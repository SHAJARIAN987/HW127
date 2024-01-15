from bs4 import BeautifulSoup as bs  
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd 

url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars'

service = webdriver.EdgeService(executable_path="C:/Users/jalal/VSCodePrgms/python_files/HW_127/msedgedriver.exe")
browser = webdriver.Edge(service=service)

browser.get(url)

time.sleep(10)

star_data = []

def scrape_stars():
    soup = bs(browser.page_source, "html.parser")
    for table in soup.find_all("table", attrs = {"class", "wikitable sortable jquery-tablesorter"}):
        for tbody in table.find_all("tbody"):
            for tr_tag in tbody.find_all("tr"):
                td_tags = tr_tag.find_all("td")
                star_list = []
                for index, td_tag in enumerate(td_tags):
                    star_list.append(td_tag.contents[0])
                star_data.append(star_list)

scrape_stars()

headers = ["Rank", "Visual Magnitutde", "Name", "Bayer Designation", "Distance", "Spectral Type"]

star_sheet = pd.DataFrame(star_data, columns = headers)

star_sheet.to_csv("StarData.csv", index = True, index_label = "id")



