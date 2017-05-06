#!/usr/bin/python3
import selenium
from selenium import webdriver
import time
import os.path
from tqdm import tqdm
#TODO: придумать как получше этот скрипт сделать
url = 'https://www.fonts-online.ru/fonts/cyrillic'
page = '?page='
page_num = 1

profile = webdriver.FirefoxProfile()
wd = os.getcwd()

profile.set_preference('browser.download.folderList', 2)
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.download.dir', os.getcwd() + '/SampleFonts')
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/x-font-ttf')
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/vnd.ms-opentype')

time.sleep(3)
print("Browser startup")
browser = webdriver.Firefox(profile)
browser.maximize_window()
links = []
text = ""

for i in tqdm(range(0, 166, 1)):
    browser.get(url+page+str(i))
    for link in browser.find_elements_by_class_name("node-font-teaser-attr"):
        links.append([link.find_element_by_tag_name("a").get_attribute("href")])

msg = 'links saved, shall i download fonts?:'
shall = input("%s (y/N) " % msg).lower() == 'y'

if shall == True:
    time.sleep(10)
    files = len(os.listdir(os.getcwd() + "/SampleFonts"))
    print(files)
    print("getting fonts from website")
    for i in range(int(files), len(links), 1):
        try:
            browser.get(str(links[i][0]))
            time.sleep(3)
            button = browser.find_element_by_id("edit-submit--3")
            button.click()
            time.sleep(3)
        except selenium.common.exeptions.NoSuchElementExeption:
            print("might be some network issue on %s element of queue", i)
            time.sleep(1000)
            continue
browser.close()
profile.set_preference('browser.download.dir', "~/Downloads")