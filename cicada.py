from bs4 import BeautifulSoup
import requests
import sys
import random
from bs4 import NavigableString
import pandas as pd
import numpy as np
from selenium import webdriver
import selenium.webdriver.support.ui as ui
import os
from time import sleep
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.firefox.options import Options
import core.webshoot as webshoot
import core.stackoverflow as stackoverflow
import core.quora as quora

#------------------------------------------------------------------------------------
# Selenium web driver for firefox

# firefox_options = Options()
# firefox_options.add_argument("--headless")
# browser  = webdriver.Firefox(firefox_options=firefox_options)
# browser.maximize_window()

#------------------------------------------------------------------------------------

# selenium web driver for chrome

# chrome_options = Options()
# chrome_options.add_argument('--headless')
# # chrome_options.headless = True
# chrome_options.add_argument('--disable-gpu')
# browser = webdriver.Chrome(chrome_options=chrome_options)
# browser.maximize_window()


#------------------------------------------------------------------------------------
def googlefunc(user_input,name,ink):

        # folder exist or not!
        # if not os.path.exists(name):
        #     print("Folder '"+name+"' created.")
        #     os.mkdir(name)
        #     os.mkdir(name+"/google")
        #     gname = "google"
        # else:
        #     ink = str(random.randrange(1,100))
        #     print("Folder '"+name+"' exist..")
        #     o = input("\n[*] Want to use the same folder? (y | n):")
        #     if o == 'n':
        #         os.mkdir(name+"("+ink+")")
        #         name  = name+"("+ink+")"
        #         print("\n[*] Folder '"+name+"' created.")
        if not os.path.exists(name+"/google"):
            print("\n[*] Folder 'google' created inside '"+name+"' folder")
            os.mkdir(name+"/google")
            gname = "google"
        else:
            os.mkdir(name+"/google("+ink+")")
            gname = "google("+ink+")"
            print("\n[*] Folder 'google' exists inside '"+name+"' so creating '"+gname+"' folder")

        #
        # url = "http://google.com"
        print("\n[#] Do you want to take the screenshots also?")
        c = input("1.yes  2.No : ")
        # # print("\n[*] googling your term")
        # browser.get(url)
        # inputbr = browser.find_element_by_name('q')
        # inputbr.send_keys(user_input)
        # button1 = browser.find_element_by_name('btnK')
        # button1.click()
        # sleep(3)
        # print(browser.current_url)
        web_url = "https://www.google.com/search?&q="+user_input

        # browser.close()
        # print("\n[*] Done! , Please wait ,reteriving all urls")

        request  = requests.get(web_url)
        data = request.text
        soup = BeautifulSoup(data,'html.parser')
        tab = {} # dicitionary to store data


        for link in soup.find_all("h3"):
            Heading = link.get_text()
            x = link.find_next("a")         #find to get (Tag
            y = x.get('href').split('=')[1] #get to get the Attribute of the Tag
            Url = y.split("&")[0]
            # Url = Url.split(':')[0]
            # print(Url)
            # print("heading:"+Heading+"\n" )
            # print("Url:"+Url+"\n")
            if Url.split(':')[0] == 'https' or 'http':
                tab[Heading] = Url  #heading as key  and Url and value[CSV]
            else:
                pass



        newdic = {'Heading':list(tab.keys()),'urls':list(tab.values())}
        df = pd.DataFrame(newdic)
        df.to_csv('./'+name+'/'+gname+'/'+name+'.csv', index=False)
        # print(df)
        print("\n[*] Done! Check '"+name+".csv' in the '"+name+"/"+gname+"' directory\n")


        if c == '1':
            # firefox_options = Options()
            # firefox_options.add_argument('--headless')
            # browser2 = webdriver.Firefox(firefox_options=firefox_options)
            # print("[*] Time to take the screenshots.. :)")
            print("\n[*] please relax! this may take a while! ¯\_(ツ)_/¯\n")
            df2 = pd.read_csv('./'+name+'/'+gname+'/'+name+'.csv')
            # print("please wait! While the grabber is working this may take a while!")
            for i in range(len(df)):
                # print(df['urls'][i])
                url2 = df2['urls'][i]
                user_input2 = name+'/'+gname
                j = '1'
                try:
                    webshoot.fullscreensave(user_input2,i,j,url2)
                except:
                    print(str(i)+". link might be broken please check the it manually!")
                    continue
            print('\n[*] All Done! you can check images in the "'+name+'/'+gname+'" directory')
            # browser2.close()
            # test2.savescr(user_input)

def stackfunction(user_input,name,flag,ink):

        # folder exist or not!
        # if not os.path.exists(name):
        #     print("Folder '"+name+"' created.")
        #     os.mkdir(name)
        #     os.mkdir(name+"/stackoverflow")
        #     name = name+"/stackoverflow"
        # else:
        #     ink = str(random.randrange(1,20))
        #     if flag != '1':
        #         print("[*] Folder '"+name+"' exist..")
        #         o = input("\nWant to use the same folder? (y | n):")
        #         if o == 'n':
        #             os.mkdir(name+"("+ink+")")
        #             name  = name+"("+ink+")"
        #             print("\n[*] Folder '"+name+"' created.")
        if not os.path.exists(name+"/stackoverflow"):
            print("\n[*] Folder 'stackoverflow' created inside '"+name+"' folder")
            os.mkdir(name+"/stackoverflow")
            sname = "stackoverflow"
            name = name+'/'+sname
        else:
            os.mkdir(name+"/stackoverflow("+ink+")")
            sname = "stackoverflow("+ink+")"
            print("\n[*] Folder 'stackoverflow' exists inside '"+name+"' so creating '"+sname+"' folder")
            name = name+'/'+sname
        stackoverflow.stackflow(user_input,name)

def quorafunc(user_input,name,flag,ink):
        # folder exist or not!
        # if not os.path.exists(name):
        #     print("Folder '"+name+"' created.")
        #     os.mkdir(name)
        #     os.mkdir(name+"/quora")
        #     name = name+"/quora"
        # else:
        #     ink = str(random.randrange(1,20))
        #     if flag != '1':
        #         print("[*] Folder '"+name+"' exist..")
        #         o = input("\nWant to use the same folder? (y | n):")
        #         if o == 'n':
        #             os.mkdir(name+"("+ink+")")
        #             name  = name+"("+ink+")"
        #             print("\n[*] Folder '"+name+"' created.")
        if not os.path.exists(name+"/quora"):
            print("\n[*] Folder 'quora' created inside '"+name+"' folder")
            os.mkdir(name+"/quora")
            sname = "quora"
            name = name+'/'+sname
        else:
            os.mkdir(name+"/quora("+ink+")")
            sname = "quora("+ink+")"
            print("\n[*] Folder 'quora' exists inside '"+name+"' so creating '"+sname+"' folder")
            name = name+'/'+sname
        quora.quoraf(user_input,name)


if(len(sys.argv) != 2):
    print("Usage: "+sys.argv[0]+" <Searchterm> ")
    exit()

# user_input = sys.argv[1]
# name = user_input.split(" ")[0]
# if not os.path.exists(name):
#     print("Folder '"+name+"' created.")
#     os.mkdir(name)
#     # os.mkdir(name+"/google")
#     # gname = "google"
# else:
#     ink = str(random.randrange(1,100))
#     print("Folder '"+name+"' exist..")
#     o = input("\n[*] Want to use the same folder? (y | n):")
#     if o == 'n':
#         os.mkdir(name+"("+ink+")")
#         name  = name+"("+ink+")"
#         print("\n[*] Folder '"+name+"' created.")
# c = sys.argv[2]
pl = input("[+] On which Platform You want to search \n [1].Google\n [2].Stackoverflow \n [3].Quora \n [0]. All\n")
flag = '0'

user_input = sys.argv[1]
name = user_input.split(" ")[0]
ink = str(random.randrange(1,100))

if not os.path.exists(name):
    print("[^] Folder '"+name+"' created.")
    os.mkdir(name)
    # os.mkdir(name+"/google")
    # gname = "google"
else:
    # ink = str(random.randrange(1,100))
    print("[^] Folder '"+name+"' exist..")
    o = input("\n[*] Want to use the same folder? (y | n):")
    if o == 'n':
        os.mkdir(name+"("+ink+")")
        name  = name+"("+ink+")"
        print("\n[^] Folder '"+name+"' created.")
#------------------------------------------------------------------------------------
# user_input = input("What do you want to search: ")
#------------------------------------------------------------------------------------



print("\n")
print("""

        (  ____ \\\__   __/(  ____ \(  ___  )(  __  \ (  ___  )
        | (    \/   ) (   | (    \/| (   ) || (  \  )| (   ) |
        | |         | |   | |      | (___) || |   ) || (___) |
        | |         | |   | |      |  ___  || |   | ||  ___  |
        | |         | |   | |      | (   ) || |   ) || (   ) |
        | (____/\___) (___| (____/\| )   ( || (__/  )| )   ( |
        (_______/\_______/(_______/|/     \|(______/ |/     \|
                                                    @logan-47


""")
print("\n")
#------------------------------------------------------------------------------------

# # folder exist or not!
# if not os.path.exists(name):
#     print("Folder '"+name+"' created.")
#     os.mkdir(name)
#     os.mkdir(name+"/stackoverflow")
# else:
#     ink = str(random.randrange(1,20))
#     print("Folder '"+name+"' exist so creating '"+name+"("+ink+") ' Folder.....")
#     os.mkdir(name+"("+ink+")")
#     os.mkdir(name+"("+ink+")/stackoverflow")
#     name  = name+"("+ink+")"
#------------------------------------------------------------------------------------

if pl == '1':
    googlefunc(user_input,name,ink)
elif pl == '2':
    stackfunction(user_input,name,flag,ink)
elif pl == '3':
    quorafunc(user_input,name,flag,ink)
elif pl == '0':
    print('\n[*] Hmmmm..... Relax and wait for a while.... ¯\_(ツ)_/¯\n')
    flag = '1'
    googlefunc(user_input,name,ink)
    stackfunction(user_input,name,flag,ink)
    quorafunc(user_input,name,flag,ink)
else:
    print('Go Home....Kiddo.... :D')
