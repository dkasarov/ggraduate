from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='app-home'),
    path('news/', views.NewsListView.as_view(), name='app-news'),
    path('category/<str:title>/', views.CategoryListView.as_view(), name='app-category'),
    path('search/', views.ApiSearchListView.as_view(), name='app-search'),
]
