from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

browser = webdriver.Chrome("./chromedriver")
url = "https://www.youtube.com/feed/explore"
browser.get(url)

html = browser.page_source
soup = BeautifulSoup(html, "html.parser")
clips = soup.select('ytd-video-renderer')

results = []
for clip in clips:
    title = clip.select("#video-title > yt-formatted-string")[0].text
    link = "https://www.youtube.com/"+ clip.select('#video-title')[0]['href']
    
    data = [title,link]
    results.append(data)

df = pd.DataFrame(results)
df.columns=['영상제목','링크']
df.to_excel('./populrar.xlsx',index=False)