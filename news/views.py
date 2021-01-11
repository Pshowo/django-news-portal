from django.shortcuts import render
from django.views import View
from django.conf import settings
import json
import datetime


# Create your views here.
class MainPageView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'news/index.html')


class News(View):

    def get(self, request, *args, **kwargs):
        data, set_data = get_data()
        return render(request, 'news/news.html', {"all_articles": data, "set_":set_data})


def article(request, link):
    with open(settings.NEWS_JSON_PATH, 'r') as file:
        data = json.load(file)
    article = None
    for _ in data:
        if _['link'] == link:
            article = _
            break
    return render(request, 'news/articles.html', {'articles': article})


def get_data():
    with open(settings.NEWS_JSON_PATH, 'r') as file:
        data = json.load(file)

    for date in data:
        date_ = date['created'].split(' ')[0]
        time_ = date['created'].split(' ')[1]
        print(date_, time_)
        Y = int(date_.split("-")[0])
        M = int(date_.split("-")[1])
        d = int(date_.split("-")[2])
        H = int(time_.split(":")[0])
        m = int(time_.split(":")[1])
        s = int(time_.split(":")[2])
        date_time = datetime.datetime(Y, M, d, H, m ,s)
        date['created'] = date_time

    set_date=[]
    for a in data:
        DATE = datetime.date(a['created'].year, a['created'].month, a['created'].day)
        set_date.append(DATE)
    set_date = list(set(set_date))

    return data, set_date