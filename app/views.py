from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import News, Category
from data.models import UserApi
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from functools import reduce
import operator


def home(request):
    return render(request, 'app/home.html', {'title': 'Home page'})


class NewsListView(ListView):
    model = News
    template_name = 'app/news.html'
    context_object_name = 'all_news'
    ordering = ['-date_posted']
    paginate_by = 10


class CategoryListView(ListView):
    model = UserApi
    template_name = 'app/category.html'
    context_object_name = 'categories_list'
    ordering = ['-date_added']
    paginate_by = 10
    title = None

    def get_queryset(self):
        category = get_object_or_404(Category, title=self.kwargs.get('title'))
        return UserApi.objects.filter(category=category).order_by('-date_added')

    def get_object(self, queryset=None):
        return queryset.get(title=self.title)


class ApiSearchListView(ListView):
    model = UserApi
    template_name = 'app/search.html'
    context_object_name = 'context'
    ordering = ['-date_added']
    paginate_by = 10

    def get_queryset(self):
        result = super(ApiSearchListView, self).get_queryset()

        query = self.request.GET.get('searchtext')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(name__icontains=q) for q in query_list))
            )
        return result
