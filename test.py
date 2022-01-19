from os import sep
from selenium import webdriver
from bs4 import BeautifulSoup
import time

browser = webdriver.Chrome("./chromedriver")
url = "https://www.youtube.com/feed/explore"
browser.get(url)

html = browser.page_source
soup = BeautifulSoup(html, "html.parser")
clips = soup.select('ytd-video-renderer')

clip = clips[0]
title = clip.select("#video-title > yt-formatted-string")[0].text
link = "https://www.youtube.com/"+ clip.select('#video-title')[0]['href']
print(title,link,sep='\n')

browser.close()