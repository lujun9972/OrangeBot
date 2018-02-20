import itchat
import requests
import sys
import json

KEY='x5bmd5wcwt9h1mzi'

def request_seniverse(action,params):
    url='https://api.seniverse.com/v3/weather/{}.json'.format(action)
    response=requests.get(url,params)
    results=json.loads(response.text)
    status=results.get('status')
    if status:   # status means some error happended
        raise RuntimeError(status)
    return results['results'][0]

def get_weather_text(location=""):
    params={'key':KEY, 'location':location}
    result=request_seniverse('now',params)
    now=result['now']
    weather_now='当前天气:{} {}℃'.format(now['text'],now['temperature'])
    result=request_seniverse('daily',params)
    today=result['daily'][0]
    weather_today='今日天气:白天 {},晚上 {},{}℃--{}℃,降雨概率 {},风力等级 {}'.format(today['text_day'], today['text_night'],today['low'],today['high'],today['precip'],today['wind_scale'])
    weather="{}天气\n{}\n{}".format(location,weather_now,weather_today)
    return weather

def get_weather_pic(location=""):
    url="http://wttr.in/"+location.replace(" ","+")+"?lang=zh"
    url=url.replace("?","_").replace("&","_")+".png"
    response=requests.get(url)
    weather_pic="/tmp/weather.png"
    open(weather_pic,'wb').write(response.content)
    return weather_pic

itchat.auto_login(hotReload=True,enableCmdQR=2)
home=itchat.search_chatrooms(name='home')[0]

for city in sys.argv[1:]:
    weather=get_weather_text(city)
    ret=itchat.send(weather,home.UserName)
    print(ret)
