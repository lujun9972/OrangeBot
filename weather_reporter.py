import itchat
import requests
import sys
itchat.auto_login(hotReload=True,enableCmdQR=2)

def get_weather(location="",png=False):
    if png:
        url="http://wttr.in/"+location.replace(" ","+")+"?lang=zh"
        url=url.replace("?","_").replace("&","_")+".png"
        response=requests.get(url)
        weather_pic="/tmp/weather.png"
        open(weather_pic,'wb').write(response.content)
        return weather_pic
    else:
        url="http://wttr.in/"+location.replace(" ","+")+"?lang=zh&0qnT"
        response=requests.get(url)
        return response.text


def get_weather_text(location=""):
    return get_weather(location)

def get_weather_pic(location=""):
    return get_weather(location,True)

home=itchat.search_chatrooms(name='home')[0]

for city in sys.argv[1:]:
    weather=get_weather_pic(city)
    ret=itchat.send('@img@%s' % weather,home.UserName)
    print(ret)
