from django.contrib.auth.models import User
from .models import News, Category
from data.models import UserApi, ApiCredentials
import datetime


def get_top_5_news(request):
    data = News.objects.all().order_by('-date_posted')[:5]
    return {
        'get_top_5_news': data
    }


def get_all_categories(request):
    data = Category.objects.filter(is_active=True).order_by('title')
    context = {
        'get_all_categories': data,
        'today': datetime.date.today()
    }
    return context


def latest_apis(request):
    data = UserApi.objects.all().order_by('-date_added')[:5]
    context = {
        'latest_apis': data
    }
    return context


def number_of_cred(request):
    num = 0
    if request.user.is_authenticated:
        num = ApiCredentials.objects.filter(user=request.user).count()
    context = {
        'num_of_cred': num
    }
    return context


def number_of_apis(request):
    num = 0
    if request.user.is_authenticated:
        num = UserApi.objects.filter(user=request.user).count()
    context = {
        'num_of_apis': num
    }
    return context
