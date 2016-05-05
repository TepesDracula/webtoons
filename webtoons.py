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
#This function will download the given comic
    def download_comic(self,comic):
        search_url="http://www.webtoons.com/search?keyword="+comic
        search_data=requests.get(search_url)
        if search_data.status_code==200:
            soup=bs(search_data.content,'lxml')
        else:
            print search_data.status_code, ": error"
        search_result=soup.find("ul",class_="card_lst")
        genre_data=str(search_result.find_all("span")[1].get_text())
#for getting the title page we need genre of the comic and the title number
        genre=""
        for i in genre_data:
            if i==" ":
                genre=genre+"-"
            else:
                genre=genre+i
        title_data=search_result.find("a")
        title=title_data.get("href")
        title_number=int(title.split("=")[1])
#after getiing the comics we need the name of each comic and total page number of pages of comics in the series
        comic_url="http://www.webtoons.com/en/"+genre+"/"+comic+"/list?title_no="+str(title_number)
        end_page_url=comic_url+"&page=50"
        end_page_data=requests.get(end_page_url)
        end_page_soup=bs(end_page_data.content,"lxml")
        end_page_soup_data=end_page_soup.find("div",class_="paginate")
    #    print end_page_soup_data
        end_page=int(str(end_page_soup_data.get_text()).split("\n")[len(end_page_soup_data.get_text().split("\n"))-2])
    #    print end_page,"end _page"
#Getting the names of the comics in a page
        last_page_episode=0
        for page in range(end_page,1,-1):
            chapter_names=[]
            current_page_url=comic_url+"&page="+str(page)
        #    print current_page_url,"current page url"
            current_page_get=requests.get(current_page_url)
            current_page_soup=bs(current_page_get.content,"lxml")
#get number of episodes in a page here
            episode_number_data=current_page_soup.find("li",id=True)
            episode_number_text=str(episode_number_data.get_text())
            total_episodes=int(episode_number_text.split(" ")[1])
#start the loop of episdoes here
            for episode_number in range(last_page_episode+1,total_episodes+1):
                episode="episode_"+str(episode_number)
                current_name_soup=current_page_soup.find("li",id=episode)
                chapter_name=str(current_name_soup.find(class_="subj").get_text().split("- ")[1])
                if chapter_name[len(chapter_name)-1]==" ":
                    chapter_name=chapter_name[0:len(chapter_name)-1]
                episode_url="http://www.webtoons.com/en/"+genre+"/"+comic+"/ep-"+str(episode_number)+"-"+chapter_name+"/viewer?title_no="+str(title_number)+"&episode_no="+str(episode_number)
                last_page_episode=episode_number
                comic_get=requests.get(episode_url)
                comic_soup=bs(comic_get.content."lxml")
                print "couldn't find any way to fetch images from webtoons.. "
#There seems to no way to fetch images from webtoons, will append this if any way is found in future:
#ps: Till here all the links are being generated peoperly, the only thing left is image scrapping
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

        new=soup.find(class_="lst_type1")
        for e in new.find_all('a',href=True):
            requests.get(e['href'])

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
