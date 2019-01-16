from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserApi, ApiCredentials
from app.models import Category
from rest_framework import viewsets
from .serializers import UserApiSerializer
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
import csv
import io
import json


@login_required
def add_api(request):
    init = {
        'categories': Category.objects.filter(is_active=True).order_by('title')
    }
    if request.method == 'GET':
        return render(request, 'data/add_api.html', init)
    csv_file = request.FILES['file']
    name_input = request.POST.get('name')
    category_input = request.POST.get('category')
    description_input = request.POST.get('description')
    get_category = Category.objects.get(pk=category_input)
    check_api_name = UserApi.objects.filter(name=name_input).exists()

    if request.method == 'POST':
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'This file is not csv!')
            return redirect('add-api')
        elif check_api_name:
            messages.error(request, f'The api name "{name_input}" has already exists. Please use other.')
            return redirect('add-api')
        else:
            data_set = csv_file.read().decode('utf-8')
            io_string = io.StringIO(data_set)
            header = next(csv.DictReader(io_string))
            reader = csv.DictReader(io_string, fieldnames=header)
            out = json.dumps([row for row in reader])
            adduserapi = UserApi(user=request.user, name=name_input, name_url=name_input.replace(' ', '-'),
                                 category=get_category, description=description_input, data=out)
            adduserapi.save()
            messages.success(request, 'Your api has been created!')
            return redirect('add-api')


@login_required
def api_details(request, name_url):
    api_model = get_object_or_404(UserApi, name_url=name_url)
    check_cred = ApiCredentials.objects.filter(user=request.user, api=api_model).exists()
    if request.method == 'POST':
        if not check_cred:
            savecredentials = ApiCredentials(user=request.user, api=api_model)
            savecredentials.save()
            messages.success(request, 'Your credentials are ready. Check access link from "MY APIs".')
            return redirect('api', name_url)
    context = {
        'api_model': api_model,
        'check_cred': check_cred
    }
    return render(request, 'data/api.html', context)


class MyCredListView(LoginRequiredMixin, ListView):
    model = ApiCredentials
    template_name = 'data/my.html'
    context_object_name = 'my_apis'
    paginate_by = 10

    def get_queryset(self):
        return ApiCredentials.objects.filter(user=self.request.user)


@login_required
def api_update(request, name_url):
    api_model = get_object_or_404(UserApi, name_url=name_url)
    if request.user.pk is not api_model.user.pk:
        return redirect('app-home')
    else:
        init = {
            'categories': Category.objects.filter(is_active=True).order_by('title'),
            'api_model': api_model
        }
        if request.method == 'GET':
            return render(request, 'data/update_api.html', init)
        csv_file = request.FILES['file']
        name_input = request.POST.get('name')
        category_input = request.POST.get('category')
        description_input = request.POST.get('description')
        get_category = Category.objects.get(pk=category_input)
        check_api_name = UserApi.objects.filter(name=name_input).exists()

        if request.method == 'POST':
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'This file is not csv!')
                return redirect('api-update', name_url)
            elif name_input != api_model.name and check_api_name:
                messages.error(request, f'The api name "{name_input}" has already exists. Please use other.')
                return redirect('api-update', name_url)
            else:
                data_set = csv_file.read().decode('utf-8')
                io_string = io.StringIO(data_set)
                header = next(csv.DictReader(io_string))
                reader = csv.DictReader(io_string, fieldnames=header)
                out = json.dumps([row for row in reader])
                updateuserapi = UserApi.objects.get(pk=api_model.pk)
                updateuserapi.name = name_input
                updateuserapi.name_url = name_input.replace(' ', '-')
                updateuserapi.category = get_category
                updateuserapi.description = description_input
                updateuserapi.data = out
                updateuserapi.save()
                messages.success(request, 'Your api has been updated!')
                return redirect('api-update', name_input.replace(' ', '-'))


def rest_api(request, pk):
    credentials = get_object_or_404(ApiCredentials, pk=pk)
    api_model = get_object_or_404(UserApi, pk=credentials.api.id)

    context = {
        'name': api_model.name,
        'description': api_model.description,
        'data': str(api_model.data).replace('\\', '')
    }
    return JsonResponse(context)


class UserApiView(viewsets.ModelViewSet):
    serializer_class = UserApiSerializer
    queryset = UserApi.objects.all()


class MyApisListView(ListView):
    model = UserApi
    template_name = 'data/myapis.html'
    context_object_name = 'context'
    ordering = ['-date_added']
    paginate_by = 10

    def get_queryset(self):
        return UserApi.objects.filter(user=self.request.user)
