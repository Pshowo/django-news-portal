from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings
import json
import datetime


def write_data_JSON(data):
    """ Write data to the file"""
    with open(settings.NEWS_JSON_PATH, "w") as file:
        json.dump(data, file, indent=0)


def get_unit_link(data):
    """ Return uniqe id for the new articles """
    links = []
    for i in data:
        links.append(int(i['link']))

    links = list(set(links))
    links.sort()
    return links.pop()+1


def search(string, data):
    new_data = []
    for i in data:
        if string.lower() in (i['title'].lower()):
            new_data.append(i)
    set_date = []
    for a in data:
        DATE = datetime.date(a['created'].year, a['created'].month, a['created'].day)
        set_date.append(DATE)
    set_date = list(set(set_date))
    return new_data, set_date


# Create your views here.
class MainPageView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'news/index.html')


class News(View):

    def get(self, request, *args, **kwargs):
        data, set_data = get_data()
        q = request.GET.get('q')
        if q:
            data = search(q, data)[0]
            set_data = search(q, data)[1]
        return render(request, 'news/news.html', {"all_articles": data, "set_": set_data, 'query': q})


class Create(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'news/form.html', )

    def post(self, request, *args, **kwargs):
        with open(settings.NEWS_JSON_PATH, 'r') as file:
            data = json.load(file)
        link = get_unit_link(data)
        title = request.POST.get('title')
        text = request.POST.get('text')
        created = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        new_article = {
            "created": created,
            "text": text,
            "title": title,
            "link": link
        }
        print(new_article)
        data.append(new_article)
        print(data)
        write_data_JSON(data)

        print(new_article)
        return redirect("/news/")


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
