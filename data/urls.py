from django.urls import path, include
from data import views as data_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('getapi', data_views.UserApiView)

urlpatterns = [
    path('add-api/', data_views.add_api, name='add-api'),
    path('api/<str:name_url>/', data_views.api_details, name='api'),
    path('api/<str:name_url>/update', data_views.api_update, name='api-update'),
    path('rest/<str:pk>/', data_views.rest_api, name='rest-api'),
    path('my-credentials/', data_views.MyCredListView.as_view(), name='my-cred'),
    path('my-apis/', data_views.MyApisListView.as_view(), name='my-apis'),
    path('', include(router.urls)),
]
