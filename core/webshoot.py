from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import os
import random
from PIL import Image
from io import StringIO
from io import BytesIO
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.firefox.options import Options


headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
#------------------------------------------------------------------------------------

# Selenium Web driver.

# firefox_options = Options()
# firefox_options.add_argument('--headless')
# browser2 = webdriver.Firefox(firefox_options=firefox_options)

#------------------------------------------------------------------------------------

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--hide-scrollbars')
chrome_options.add_argument('--mute-audio')
chrome_options.add_argument('--disable-notifications')
chrome_options.add_argument('--disable-crash-reporter')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36')
browser2 = webdriver.Chrome(chrome_options=chrome_options)


#------------------------------------------------------------------------------------

# WIl take Full page Screen shot.[thanks to stackoverflow (@Fabian Thommen):D]
def fullscreensave(user_input,i,j,url):
    browser2.get(url)
    name = url.split('/')[2]
    js = 'return Math.max( document.body.scrollHeight, document.body.offsetHeight,  document.documentElement.clientHeight,  document.documentElement.scrollHeight,  document.documentElement.offsetHeight);'
    quora = """var list, index,list2,list3;
    list = document.getElementsByClassName("SiteHeader");
    for (index = 0; index < list.length; ++index) {
        list[index].setAttribute('style', 'display: none; top: 0px;');
    }
    list2 = document.getElementsByClassName("input_prompt");
    for (index = 0; index < list2.length; ++index) {
        list2[index].setAttribute('style', 'display: none; top: 0px;');
    }

    list3 = document.getElementsByClassName("BelowQuestionAddPrompt");
    for (index = 0; index < list3.length; ++index) {
        list3[index].setAttribute('style', 'display: none; top: 0px;');
    }
    """

    stackf = """
    var list = document.getElementsByClassName('top-bar');
    var index;
    for(index=0;index<list.length;++index){

    list[index].setAttribute('style', 'display: none; top: 0px;')
    }
    document.getElementById('js-gdpr-consent-banner').setAttribute('style', 'display: none; top: 0px;');
    """
    #scroll through Page.
    scrollheight = browser2.execute_script(js)


    slices = []
    offset = 0
    # for quora
    # try:
    #     print("worked")
    #     browser2.execute_script(quora)
    # except:
    #     pass

    while offset < scrollheight:

        browser2.execute_script("window.scrollTo(0, %s);" % offset)
        try:
            # print("worked")
            browser2.execute_script(quora)
            browser2.execute_script(stackf)

        except:
            pass
        img = Image.open(BytesIO(browser2.get_screenshot_as_png()))
        offset += img.size[1]
        slices.append(img)


    screenshot = Image.new('RGB', (slices[0].size[0], scrollheight))
    offset = 0
    for img in slices:
        screenshot.paste(img, (0, offset))
        offset += img.size[1]
    if os.path.isfile('./'+user_input+'/http_'+name+'.png'):
        ink = str(random.randrange(1,100))
        screenshot.save('./'+user_input+'/http_'+name+'('+ink+').png')
        name = name+'('+ink+')'
    else:
        screenshot.save('./'+user_input+'/http_'+name+'.png')
    print('[%] screenshot http_'+name+'.png taken')
    return name
