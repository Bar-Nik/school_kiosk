# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

import mammoth as mth

from datetime import *

from kiosk.models import *

import requests
from bs4 import BeautifulSoup

days_week_list = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']

date_time = datetime.now()
date_today = date.today()
days_week = days_week_list[date_today.weekday()]


def index(request):
    return render(request, 'kiosk/index.html',
                  {'title': 'Главная', 'date_time': date_today})


def raspisanie_new(request):
    raspisanie = Raspisanie_New.objects.all()
    raspisanie_new = raspisanie[len(raspisanie) - 1].raspisanie_new
    rasp = mth.convert_to_html(raspisanie_new).value
    rasp_new = rasp[rasp.find('<table>'):]

    context = {
        'title': 'Расписание на сегодня',
        'content': rasp_new,
        'date_time': date_today,
        'days_week': days_week
    }
    return render(request, 'kiosk/raspisanie.html', context=context)


def raspisanie_post(request):
    context = {
        'title': 'Расписание 5-11 классы',
        'date_time': date_today
    }
    return render(request, 'kiosk/raspisanie_post.html', context=context)


def raspisanie_post_monday(request):
    raspisanie = Raspisanie_Post.objects.all()
    raspisanie_post = raspisanie[len(raspisanie) - 1].raspisanie_post_1monday
    post = mth.convert_to_html(raspisanie_post).value
    post_rasp = post[post.find('<table>'):]

    context = {
        'title': 'Понедельник',
        'content': post_rasp,
        'date_time': date_today
    }
    return render(request, 'kiosk/raspisanie.html', context=context)


def raspisanie_post_tuesday(request):
    raspisanie = Raspisanie_Post.objects.all()
    raspisanie_post = raspisanie[len(raspisanie) - 1].raspisanie_post_2tuesday
    post = mth.convert_to_html(raspisanie_post).value
    post_rasp = post[post.find('<table>'):]

    context = {
        'title': 'Вторник',
        'content': post_rasp,
        'date_time': date_today
    }
    return render(request, 'kiosk/raspisanie.html', context=context)


def raspisanie_post_wednesday(request):
    raspisanie = Raspisanie_Post.objects.all()
    raspisanie_post = raspisanie[len(raspisanie) - 1].raspisanie_post_3wednesday
    post = mth.convert_to_html(raspisanie_post).value
    post_rasp = post[post.find('<table>'):]

    context = {
        'title': 'Среда',
        'content': post_rasp,
        'date_time': date_today
    }
    return render(request, 'kiosk/raspisanie.html', context=context)


def raspisanie_post_thursday(request):
    raspisanie = Raspisanie_Post.objects.all()
    raspisanie_post = raspisanie[len(raspisanie) - 1].raspisanie_post_4thursday
    post = mth.convert_to_html(raspisanie_post).value
    post_rasp = post[post.find('<table>'):]

    context = {
        'title': 'Четверг',
        'content': post_rasp,
        'date_time': date_today
    }
    return render(request, 'kiosk/raspisanie.html', context=context)


def raspisanie_post_friday(request):
    raspisanie = Raspisanie_Post.objects.all()
    raspisanie_post = raspisanie[len(raspisanie) - 1].raspisanie_post_5friday
    post = mth.convert_to_html(raspisanie_post).value
    post_rasp = post[post.find('<table>'):]

    context = {
        'title': 'Пятница',
        'content': post_rasp,
        'date_time': date_today
    }
    return render(request, 'kiosk/raspisanie.html', context=context)

def raspisanie_post_saturday(request):
    raspisanie = Raspisanie_Post.objects.all()
    raspisanie_post = raspisanie[len(raspisanie) - 1].raspisanie_post_6saturday
    post = mth.convert_to_html(raspisanie_post).value
    post_rasp = post[post.find('<table>'):]

    context = {
        'title': 'Суббота',
        'content': post_rasp,
        'date_time': date_today
    }
    return render(request, 'kiosk/raspisanie.html', context=context)


def raspisanie_calls(request):
    raspisanie = Raspisanie_Calls.objects.all()
    raspisanie_call = raspisanie[len(raspisanie) - 1].raspisanie_calls
    calls = mth.convert_to_html(raspisanie_call).value
    calls_new = calls[calls.find('<table>'):]

    context = {
        'title': 'Расписание  звонков',
        'content': calls_new,
        'date_time': date_today
    }
    return render(request, 'kiosk/raspisanie_calls.html', context=context)


def newSchool(request):
    try:
        url = 'https://koltush.vsevobr.ru/'
        responce = requests.get(url=url)
        responce.encoding = 'utf-8'
        soup = BeautifulSoup(responce.text, 'lxml')
        news_title = soup.find('div', class_='items').find_all('h1')
        news_text = soup.find_all('div', class_='content clearfix')
        content = {news_title[i].text.strip(): news_text[i].text.strip() for i in range(len(news_title))}
        context = {
            'title': 'Новости школы',
            'content': content,
            'date_time': date_today
        }
        return render(request, 'kiosk/news.html', context=context)
    except:
         content = 'Нет соединения с интернетом'
         context = {
             'title': 'Ошибка',
             'content': content,
             'date_time': date_today
         }
         return render(request, 'kiosk/error.html', context=context)

def aboutSchool(request):
    # url = 'https://koltush.vsevobr.ru/index.php/svedeniya-ob-obrazovatelnoj-organizatsii/osnovnye-svedeniya'
    # responce = requests.get(url=url)

    # responce.encoding = 'utf-8'

    # soup = BeautifulSoup(responce.text, 'lxml')

    # news_title = soup.find('div', class_='items').find_all('h1')
    # news_text = soup.find('div', class_='content clearfix').find_all('table')
    # print(1, news_text[0])
    # print(2, type(news_text[1]), news_text[1])

    # content = news_text


    context = {
        'title': 'О школе',
        'content': '#',
        'date_time': date_today
    }
    return render(request, 'kiosk/about.html', context=context)


def navigation1(request):
    context = {
        'title': 'Первый этаж',
        'content': '#',
        'date_time': date_today,
        'cabs': [118, 122, 123, 124, 125, 126, 127, 128, 129, 130,
                 131, 133, 135, '148-149', 'мед. кабинет', 'спортзал', 'столовая']
    }
    return render(request, 'kiosk/floor_first.html', context=context)

def navigation2(request):
    context = {
        'title': 'Второй этаж',
        'content': '#',
        'date_time': date_today,
        'cabs': [207, 208, 209, 210, 211, 212, 213, 214, 215, 217,
                 218, 219, 220, 229, 232, 233, 237, 239,'актовый зал',
                 'приемная', 'шахматы']
    }
    return render(request, 'kiosk/floor_second.html', context=context)

def navigation3(request):
    context = {
        'title': 'Третий этаж',
        'content': '#',
        'date_time': date_today,
        'cabs': [304, 305, 306, 307, 308, 309, 310, 311, 313, 314,
                 317, 319, 320, 322, 330, 332, 333, 335, 344, 346,
                 360, 'библио-тека', 'музей', 'психолог']
    }
    return render(request, 'kiosk/floor_third.html', context=context)

def raspisanie_bus(request):
    raspisanie = Raspisanie_Bus.objects.all()
    raspisanie_bus_temp = raspisanie[len(raspisanie) - 1].raspisanie_bus
    bus = mth.convert_to_html(raspisanie_bus_temp).value
    calls_bus_new = bus[bus.find('<table>'):]

    context = {
        'title': 'Расписание автобуса',
        'content': calls_bus_new,
        'date_time': date_today
    }
    return render(request, 'kiosk/bus.html', context=context)