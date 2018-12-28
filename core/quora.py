import requests
from bs4 import BeautifulSoup
import core.webshoot as webshoot
import random
import random
import os
from colorama import init
from colorama import Fore
init()

# user_input = "pubg"
def quoraf(user_input,mainName):
    ink = str(random.randrange(1,20))
    if os.path.isfile("./"+mainName+"/quorareport.html"):
        filename = mainName+'/quorareport('+ink+').html'
        file  = open('./'+mainName+'/quorareport('+ink+').html','a+')
        s = mainName
    else:
        filename = mainName+'/quorareport.html'
        file  = open('./'+mainName+'/quorareport.html','a+')
        s = mainName
    i = 0
    file.write("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="widtd=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Quora-Cicada</title>
      <style>

      </style>
    </head>
    <body>
      <center><h3>Report Created By CICADA!</h3></center>
    <div style="display:flex">
    """)

    wrapper = """
      <div width="500px" height="500px" style="border:1px solid black">
        <center><h3>%s <a href="%s" target="_blank"> link </a></h3><center><hr>
          <a href="http_%s.png" target="_blank">
         <img src="http_%s.png"  style="height:70vh;width:33vw" >
         </a>
      </div>

    """

    request = requests.get(r'https://www.google.com/search?q=site:%20"quora.com"%20text='+user_input)
    print(Fore.RESET+"[*] creating 'Quora' report please wait!")
    data = request.text
    soup = BeautifulSoup(data,'html.parser')
    for link in soup.find_all("h3"):
        Heading = link.get_text()
        x = link.find_next("a")
        y = x.get('href').split('=')[1]
        Url = y.split("&")[0]
        try:
            if (Url.split(':')[0] == 'https' or 'http') and (Url.split('/')[2] == 'www.quora.com') :
                Heading = Url.split('/')[3].replace('-',' ')
                name = webshoot.fullscreensave(s,1,1,Url)
                whole = wrapper %(Heading,Url,name,name)
                if (i%3) == 0:
                    file.write("""
                      </div>
                      <div style="display:flex">
                    """)
                file.write(whole)

            else:
                pass
        except:
            print(Fore.RED+"[#] Something Went Wrong")

        i = i+1
    file.write("""
    </div>
    </body>
    </html>
    """)
    file.close()
    print(Fore.RESET+"[*] Done! check "+filename)
