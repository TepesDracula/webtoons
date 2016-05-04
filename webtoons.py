"""This script will be used to download comics from webtoons.com"""
import requests
from bs4 import BeautifulSoup as bs
class Webtoons:
    def __init__(self):
        pass

#This function will list the comics based on the age/sex specified
    def popularity_age(self,age,sex):
        age=int(round(age/10)*10)
        if age>30:
            age=30
        else:
            pass
        sex=sex.upper()
        if sex=="MALE" or sex == "FEMALE":
            pass
        else:
            print "Invalid sex..!"
            return
        url = "http://www.webtoons.com/en/top?rankingGenre=ALL&target="+sex+str(age)
        page_data=requests.get(url)
        if page_data.status_code==200:
            soup=bs(page_data.content,"lxml")
        else:
            print page_data.status_code," :  error"
        data=soup.find_all("h3",class_="blind")
        list_data=data[1].findNextSibling('ul')
        list_of_names=list_data.find_all(class_="subj")
        for i in list_of_names:
            print i.get_text()

#This will fetch the work done by a given author

    def author_comics(self,author):
        search_url="http://www.webtoons.com/search?keyword="+author
        search_data=requests.get(search_url)
        if search_data.status_code==200:
            soup=bs(search_data.content,'lxml')
        else:
            print search_data.status_code, ": error"
        search_result=soup.find("ul",class_="card_lst")
        all_result=search_result.find_all(class_="subj")
        for i in all_result:
            print i.get_text()

    def download_comic(self,comic):
        search_url="http://www.webtoons.com/search?keyword="+comic
        search_data=requests.get(search_url)
        if search_data.status_code==200:
            soup=bs(search_data.content,'lxml')
        else:
            print search_data.status_code, ": error"
        search_result=soup.find("ul",class_="card_lst")
        genre_data=str(search_result.find_all("span")[1].get_text())
        genre=""
        for i in genre_data:
            if i==" ":
                genre=genre+"-"
            else:
                genre=genre+i
        title_data=search_result.find("a")
        title=title_data.get("href")
        title_number=int(title.split("=")[1])
        comic_url="http://www.webtoons.com/en/"+genre+"/"+comic+"/list?title_no="+str(title_number)
        
