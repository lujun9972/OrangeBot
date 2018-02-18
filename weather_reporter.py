import itchat
import requests
itchat.auto_login(hotReload=True,enableCmdQR=2)

def get_weather(location="",png=False):
    if png:
        url="http://wttr.in/"+location.replace(" ","+")+"?lang=zh"
        url=url.replace("?","_").replace("&","_")+".png"
        response=requests.get(url)
        open('weather.png','wb').write(response.content)
        return 'weather.png'
    else:
        url="http://wttr.in/"+location.replace(" ","+")+"?lang=zh&0qnT"
        response=requests.get(url)
        return response.text


def get_weather_text(location=""):
    return get_weather(location)

def get_weather_pic(location=""):
    return get_weather(location,True)

home=itchat.search_chatrooms(name='home')[0]

for city in ('zhuhai','dongguan'):
    weather=get_weather_pic(city)
    ret=itchat.send('@img@%s' % weather,home.UserName)
    print(ret)
