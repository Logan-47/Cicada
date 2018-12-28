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
import core.webshoot as webshoot
import core.stackoverflow as stackoverflow
import core.quora as quora
from colorama import init
from colorama import Fore
init()
#------------------------------------------------------------------------------------

def googlefunc(user_input,name,ink):

        if not os.path.exists(name+"/google"):
            print(Fore.YELLOW+"\n[^] Folder 'google' created inside '"+name+"' folder")
            os.mkdir(name+"/google")
            gname = "google"
        else:
            os.mkdir(name+"/google("+ink+")")
            gname = "google("+ink+")"
            print(Fore.YELLOW+"\n[^] Folder 'google' exists inside '"+name+"' so creating '"+gname+"' folder")

        print(Fore.RED+"[#] Do you want to take the screenshots also[Google result]?")
        c = input(Fore.RESET+"1.yes  2.No : ")

        web_url = "https://www.google.com/search?&q="+user_input

        request  = requests.get(web_url)
        data = request.text
        soup = BeautifulSoup(data,'html.parser')
        tab = {}                                                # dicitionary to store data


        for link in soup.find_all("h3"):
            Heading = link.get_text()
            x = link.find_next("a")                            #find to get (Tag
            y = x.get('href').split('=')[1]                  #get to get the Attribute of the Tag
            Url = y.split("&")[0]

            if Url.split(':')[0] == 'https' or 'http':
                tab[Heading] = Url                          #heading as key  and Url and value[CSV]
            else:
                pass

        newdic = {'Heading':list(tab.keys()),'urls':list(tab.values())}
        df = pd.DataFrame(newdic)
        df.to_csv('./'+name+'/'+gname+'/'+name+'.csv', index=False)
        print(Fore.RESET+"[*] Done! Check '"+name+".csv' in the '"+name+"/"+gname+"' directory\n")


        if c == '1':

            print(Fore.BLUE+"[*] Taking ScreenShots of GoogleSearch\n")
            df2 = pd.read_csv('./'+name+'/'+gname+'/'+name+'.csv')

            for i in range(len(df)):

                url2 = df2['urls'][i]
                user_input2 = name+'/'+gname
                j = '1'
                try:
                    webshoot.fullscreensave(user_input2,i,j,url2)
                except:
                    print(Fore.RED+str(i)+". link might be broken please check it manually!")
                    continue
            print(Fore.RESET+'[*] All Done! you can check images in the "'+name+'/'+gname+'" directory')

#-------------------------------------------------------------------------------------------------------

def stackfunction(user_input,name,flag,ink):

        if not os.path.exists(name+"/stackoverflow"):
            print(Fore.YELLOW+"\n[^] Folder 'stackoverflow' created inside '"+name+"' folder")
            os.mkdir(name+"/stackoverflow")
            sname = "stackoverflow"
            name = name+'/'+sname
        else:
            os.mkdir(name+"/stackoverflow("+ink+")")
            sname = "stackoverflow("+ink+")"
            print(Fore.YELLOW+"\n[^] Folder 'stackoverflow' exists inside '"+name+"' so creating '"+sname+"' folder")
            name = name+'/'+sname
        stackoverflow.stackflow(user_input,name)

#------------------------------------------------------------------------------------

def quorafunc(user_input,name,flag,ink):

        if not os.path.exists(name+"/quora"):
            print(Fore.YELLOW+"\n[^] Folder 'quora' created inside '"+name+"' folder")
            os.mkdir(name+"/quora")
            sname = "quora"
            name = name+'/'+sname
        else:
            os.mkdir(name+"/quora("+ink+")")
            sname = "quora("+ink+")"
            print(Fore.YELLOW+"\n[^] Folder 'quora' exists inside '"+name+"' so creating '"+sname+"' folder")
            name = name+'/'+sname
        quora.quoraf(user_input,name)


if(len(sys.argv) != 2):
    print(" Usage: "+sys.argv[0]+" 'Search term' ")
    exit()
#------------------------------------------------------------------------------------
pl = input("[+] On which Platform You want to search \n [1] Google \n [2] Stackoverflow \n [3] Quora \n [0] All\n")
flag = '0'

user_input = sys.argv[1]
name = user_input.split(" ")[0]
ink = str(random.randrange(1,100))

#------------------------------------------------------------------------------------
def b():
        print("""
     ▄████████  ▄█   ▄████████    ▄████████ ████████▄     ▄████████
    ███    ███ ███  ███    ███   ███    ███ ███   ▀███   ███    ███
    ███    █▀  ███▌ ███    █▀    ███    ███ ███    ███   ███    ███
    ███        ███▌ ███          ███    ███ ███    ███   ███    ███
    ███        ███▌ ███        ▀███████████ ███    ███ ▀███████████
    ███    █▄  ███  ███    █▄    ███    ███ ███    ███   ███    ███
    ███    ███ ███  ███    ███   ███    ███ ███   ▄███   ███    ███
    ████████▀  █▀   ████████▀    ███    █▀  ████████▀    ███    █▀
                                                        @logan-47
    """)

if __name__ == "__main__":

    if pl == '1' or pl == '2' or pl == '3' or pl == '0':
        b()
        if not os.path.exists(name):
            print("[^] Folder '"+name+"' created.")
            os.mkdir(name)

        else:

            print(Fore.RED+"[^] Folder '"+name+"' exist..")
            o = input(Fore.RESET+"[*] Want to use the same folder? (y|n):")
            if o == 'n':
                os.mkdir(name+"("+ink+")")
                name  = name+"("+ink+")"
                print(Fore.YELLOW+"[^] Folder '"+name+"' created.")

        print(Fore.BLUE+"[^] Chrome Headless Mode initialized.")

    if pl == '1':
        googlefunc(user_input,name,ink)
    elif pl == '2':
        stackfunction(user_input,name,flag,ink)
    elif pl == '3':
        quorafunc(user_input,name,flag,ink)
    elif pl == '0':
        flag = '1'
        googlefunc(user_input,name,ink)
        stackfunction(user_input,name,flag,ink)
        quorafunc(user_input,name,flag,ink)
    else:
        print(Fore.RED+" (-_(-_(-_(-_-)_-)_-)_-) ")
