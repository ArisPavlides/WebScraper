import pandas as pd
import time
import re
import datetime
import collections

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(r"C:\Users\arisp\Documents\WebScraper\New_folder\chromedriver.exe")
actionchains = ActionChains(driver)

#### GRABBER ####
week_list = [1, 3, 11, 12, 31]
search_terms = "Bitcoin"
grabber = []
stories = []

for x in week_list:

    week = x
    dat = "2018-W" + str(week)
    r = datetime.datetime.strptime(dat + '-1', "%Y-W%W-%w")

    date = "{}/{}/{}".format(r.month, r.day, r.year)
    date2 = "{}/{}/{}".format(r.month, r.day + 7,r.year)

    driver.get("https://www.google.gr/search?q="+search_terms+"&biw=1920&bih=921&source=lnt&tbs=cdr%3A1%2C:" + date + ",cd_max:" + date2 + "&tbm=nws")
    links = driver.find_elements_by_xpath("//div[@class='gG0TJc']//a[@href]")

    links_grabbed = []

    for x in links:

        if x.text == "" or x.text == "Μετάφραση αυτής της σελίδας":
            continue

        else:
            links_grabbed.append(x.text.upper())

    grabber.append(links_grabbed)
    story = driver.find_elements_by_xpath("//div[@class='st']")

    for x in story:

        stories.append(x.text.upper())

    time.sleep(2)

week_rez = pd.DataFrame({"WEEK": week_list,"PRESS": grabber})

#### COUNTER (NOT BEST PRACTICE USED) ####
mone = grabber
zzzz = str(mone).split()
words = zzzz
wordsx = re.findall(r'\w{4,10}', str(words))
counter = collections.Counter(wordsx)
print(counter.most_common(10))

mone1 = stories
zzzz1 = str(mone1).split()
words1 = zzzz1
wordsxx = re.findall(r'\w{4,10}', str(words1))
counter1 = collections.Counter(wordsxx)
print(counter1.most_common(10))