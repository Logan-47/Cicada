from bs4 import BeautifulSoup
import requests
# from selenium import webdriver
# import pandas as pd
import os
import random
import core.webshoot as webshoot 

# ink = str(random.randrange(1,20))
# if os.path.isfile("report.html"):
#     filename = 'report('+ink+').html'
#     file  = open('report('+ink+').html','a+')
# else:
#     filename = 'report.html'
#     file  = open('report.html','a+')


#-------------------------------------------------------------------------------------
        #one way of doing It.
# url = "https://stackoverflow.com/"
# user_input = input("What do you want to search: ")
# # name = user_input.split(" ")[0]
# # print("Do you want to take the screenshots also?\n")
# # c = input("1.yes  2.No : ")
# print("\n\t\tGot the Url\n")
# browser.get(url)
# input = browser.find_element_by_name('q')
# input.send_keys(user_input)
# input.send_keys( u'\ue007')
#
# # button1 = browser.find_element_by_name('btnK')
# # button1.click()
# # sleep(3)
# # # print(browser.current_url)
# web_url = browser.current_url
# print(web_url)

#----------------------------------------------------------------------------------------
def stackfunc(url):
    request  = requests.get(url)
    data = request.text
    soup = BeautifulSoup(data,'html.parser')
    # print(soup)
    answer = soup.find("div",attrs={"class":"accepted-answer"})
    try:
        answerdiv = answer.find_next("div", attrs={"class":"post-text"})
        return(answerdiv.text)
    except:
        return "Don't have an accepted-answer click on link ---> "
    # # answerText = answer.find_next("div",{"class":"post-text"}).get_text()
#------------------------------------------------------------------------------------

def stackflow(user_input,mainName):
#------------------------------------------------------------------------------------

    ink = str(random.randrange(1,20))
    if os.path.isfile("./"+mainName+"/stackreport.html"):
        filename = mainName+'/stackreport('+ink+').html'
        file  = open('./'+mainName+'/stackreport('+ink+').html','a+')
        s = mainName
    else:
        filename = mainName+'/stackreport.html'
        file  = open('./'+mainName+'/stackreport.html','a+')
        s = mainName
#------------------------------------------------------------------------------------

    user_input = user_input
    stackurl = "https://stackoverflow.com/search?q="+user_input+"+is:question"
    # name = stackurl.split('/')[2]
    print('\n[*] searching on stackoverflow.com..... :)')
    name = webshoot.fullscreensave(s,1,1,stackurl)
    print("\n[*] creating report...Please Wait :D")
    file.write("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="widtd=device-widtd, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Stackoverflow-Cicada</title>
      <style>
      #stackimg{
       height: 2000px;
       width: 35vw;
      }
      div{
          display:inline-flex;
      }
      body{
        background-color: blue;
        color: white;
      }
      table{
        height: 800px;
        width: 64vw;
        border-radius: 20px;
        color: black;
        font-size: 20px;
        border-collapse: collapse;
        /* padding: 5px; */
      }
      table th{
    background-color: black;
    color:white;
    }

    table td,th{
       border: 1px solid blue;
      text-align: center;
      /* border-radius : 20px; */
    }
      table th:nth-child(1){
      border-top-left-radius: 20px;
      }
      table th:last-child{
      border-top-right-radius: 20px;
      }
      table tr:nth-child(even){
        background-color: lightgrey ;
      }
      table tr:nth-child(odd){
        background-color: white ;
      }
      </style>
    </head>
    <body>
      <center><h1>Report Created By CICADA!</h1></center>
     <div> <table>
        <tr><th></th><th >Stackoverflow</th><th></th></tr>
      <tr><td style="font-weight:bold;">Question</td><td style="font-weight:bold;">Answer</td><td style="font-weight:bold;">link</td></tr>

    """)

    wrapper = """

    <tr><td width="200px">%s</td><td>%s</td><td width="100px"><a href="%s" target="_blank">click</a></td></tr>

    """
    request  = requests.get(stackurl)
    data = request.text
    soup = BeautifulSoup(data,'html.parser')
    # stack = {} # dicitionary to store data
    #
    #
    i = 0
    for link in soup.find_all("h3"):
        i = i + 1
        if i > 3:    # to strip the initial Crap......:D
            Heading = link.get_text()
            # print(Heading+"\n")
            sx = link.find_next("a")
            # print(sx)        # get <a> tag
            sy = sx.get('href').split('=')[0] # only link part
            sfull = "http://stackoverflow.com/"+sy
            # print(sfull)
            answer = stackfunc(sfull)
            # print(answer)
            whole = wrapper % (Heading, answer,sfull)
            file.write(whole)

    image = "<a href='http_"+name+".png' target='_blank'><img src='http_"+name+".png' alt='not found' id='stackimg'></a>"
    file.write(image)
    file.write("""


      </table>
      </div>
      </center>
    </body>
    </html>


    """)
    file.close()
    print("[*] Done ! check "+filename)

        # print(sfull)


        # Url = y.split("&")[0]
        # # print("heading:"+Heading+"\n" )
        # # print("Url:"+Url+"\n")
        # tab[Heading] = Url              #heading as key  and Url and value
#
#
# newdic = {'Heading':list(tab.keys()),'urls':list(tab.values())}
# df = pd.DataFrame(newdic)
# df.to_csv('./'+name+'/'+name+'.csv', index=False)
# # print(df)
# print("\nDone! Check '"+name+".csv' in the '"+name+"' folder\n")
