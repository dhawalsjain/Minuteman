from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.clickjacking import xframe_options_sameorigin

import requests

from bs4 import BeautifulSoup
from django.contrib.auth.decorators import login_required

# define groups
lab1_hpc_rstudio_user = "lab1_hpc_rstudio_user"
lab1_Company_user = "lab1_Company_user"
lab1_external_user = "lab1_external_user"

@login_required
def index(request):
    return render(request, 'dashboard/dashboard.html')

@login_required
@xframe_options_sameorigin
def sciview(request):
    if request.user.groups.filter(name=lab1_Company_user).exists():
        return render(request, 'boston/sciview.html')
    if request.user.groups.filter(name=lab1_external_user).exists():
        return render(request, 'boston/sciview.html')
    return render(request, 'dashboard/permission.html')

@login_required
def indexlab1(request):
    if request.user.groups.filter(name=lab1_Company_user).exists():
        return render(request, 'boston/indexlab1.html')
    if request.user.groups.filter(name=lab1_external_user).exists():
        return render(request, 'boston/indexlab1.html')
    return render(request, 'dashboard/permission.html')

@login_required
@xframe_options_sameorigin
def sciview_contents(request):
    if not request.user.groups.filter(name=lab1_Company_user).exists():
        if not request.user.groups.filter(name=lab1_external_user).exists():
            return JsonResponse({'html_contents': ''})
    response = requests.get('http://sciview/SciView/')
    soup = BeautifulSoup(response.content, 'html.parser')
    return JsonResponse({'html_contents': str(soup)})

@login_required
def home(request):
    home_greeting = 'Welcome to the Minuteman Information Portal'
    template = 'dashboard/home.html'
    context = {'home_greeting': home_greeting}
    return render(request, template, context)

@login_required
@xframe_options_sameorigin
def cellxgene(request):
    if request.user.groups.filter(name=lab1_Company_user).exists():
        return render(request, 'boston/cellxgene.html')
    if request.user.groups.filter(name=lab1_external_user).exists():
        return render(request, 'boston/cellxgene.html')
    return render(request, 'dashboard/permission.html')

@login_required
@xframe_options_sameorigin
def cellxgene_contents(request):
    if not request.user.groups.filter(name=lab1_Company_user).exists():
        if not request.user.groups.filter(name=lab1_external_user).exists():
            return JsonResponse({'html_contents': ''})
    response = requests.get('http://cellxgene/')
    soup = BeautifulSoup(response.content, 'html.parser')
    return JsonResponse({'html_contents': str(soup)})

@login_required
@xframe_options_sameorigin
def lab1singlecellapp(request):
    if request.user.groups.filter(name=lab1_Company_user).exists():
        return render(request, 'boston/lab1singlecellapp.html')
    if request.user.groups.filter(name=lab1_external_user).exists():
        return render(request, 'boston/lab1singlecellapp.html')
    return render(request, 'dashboard/permission.html')

@login_required
@xframe_options_sameorigin
def lab1singlecellapp_contents(request):
    if not request.user.groups.filter(name=lab1_Company_user).exists():
        if not request.user.groups.filter(name=lab1_external_user).exists():
            return JsonResponse({'html_contents': ''})
    response = requests.get('http://singlecellapp/lab1SingleCellApp/')
    soup = BeautifulSoup(response.content, 'html.parser')
    return JsonResponse({'html_contents': str(soup)})

@login_required
@xframe_options_sameorigin
def lab1expressionapp(request):
    if request.user.groups.filter(name=lab1_Company_user).exists():
        return render(request, 'boston/lab1expressionapp.html')
    if request.user.groups.filter(name=lab1_external_user).exists():
        return render(request, 'boston/lab1expressionapp.html')
    return render(request, 'dashboard/permission.html')

@login_required
@xframe_options_sameorigin
def lab1expressionapp_contents(request):
    if not request.user.groups.filter(name=lab1_Company_user).exists():
        if not request.user.groups.filter(name=lab1_external_user).exists():
            return JsonResponse({'html_contents': ''})
    response = requests.get('http://expressionapp/lab1ExpressionApp/')
    soup = BeautifulSoup(response.content, 'html.parser')
    return JsonResponse({'html_contents': str(soup)})

@login_required
def jupyterhub(request):
    if request.user.groups.filter(name=lab1_hpc_rstudio_user).exists():
        if request.user.groups.filter(name=lab1_Company_user).exists():
            return render(request, 'dashboard/jupyterhub_lab1_internal.html')
        if request.user.groups.filter(name=lab1_external_user).exists():
            return render(request, 'dashboard/jupyterhub_lab1_external.html')
    return render(request, 'dashboard/permission.html')

@login_required
def rstudio(request):
    if request.user.groups.filter(name=lab1_hpc_rstudio_user).exists():
        if request.user.groups.filter(name=lab1_Company_user).exists():
            return render(request, 'dashboard/rstudio_lab1_internal.html')
        if request.user.groups.filter(name=lab1_external_user).exists():
            return render(request, 'dashboard/rstudio_lab1_external.html')
    return render(request, 'dashboard/permission.html')

def check(request):
    # Get an HttpRequest - the request parameter.
    # perform operations using information from the request.
    # Return HttpResponse.
    # Used for check website status.
    return HttpResponse(status=200)
