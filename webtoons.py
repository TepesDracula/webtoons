"""This script will be used to download comics from webtoons.com"""
import time
import requests
import bs4
from bs4 import BeautifulSoup as bs
class Webtoons:


# list all comics released on that day
    def new_releases(self):
        day = time.strftime("%A")
        day_sched= requests.get("http://www.webtoons.com/en/dailySchedule")
        soup=bs(day_sched.content,'lxml')
        ls=soup.find("div",{'class':"daily_section  _list_"+day.upper()} )


        self.s=ls.find_all(class_="subj")
        count=1
        for e in self.s:
            print str(count) +' '+ e.get_text()
            count+=1

    def top10_of_day(self)
