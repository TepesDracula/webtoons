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

        released_list=[]
        for e in self.s:
            released_list.append(e.get_text())

        return released_list

    def new_releases_all(self):
        released_all= self.new_releases()
        count=1
        for i in released_all:
            print str(count)+ ' '+i
            count+=1

    def top10_of_day(self):
        released=self.new_releases()
        for i in range(0,10):
            print str(i+1) + ' '+released[i]


    def best_rated(self):
        page=requests.get('http://www.webtoons.com/en/top')
        soup=bs(page.content,'lxml')
        ls=soup.find(class_="ranking_lst top")
        subjall=ls.find_all(class_="subj")
        count = 1
        for i in subjall:
            print str(count)+' ' +i.get_text()
            count+=1

    def top_in_genre(self,g):
        page=requests.get('http://www.webtoons.com/en/genre')
        soup=bs(page.content,'lxml')
        gen=g.split(" ")
        genre=''
        for e in gen:
            genre+="_"+e

        ls=soup.find(class_="sub_title g"+genre)
        ul=ls.findNextSibling('ul')
        names=ul.find_all(class_="subj")
        count=1
        for i in names:
            print= str(count)+' '+ i.get_text()
            count+=1
