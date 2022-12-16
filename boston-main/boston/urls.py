"""boston URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('dashboard_home/', views.index, name='dashboardHome'),
    path('', views.home, name='minutemanHome'),
    path('admin/', admin.site.urls),
    path('sciview/', views.sciview, name='sciview'),
    path('sciview_contents/', views.sciview_contents, name='sciview_contents'),
    path('accounts/login/', auth_views.LoginView.as_view()),
    path('lab1/', views.indexlab1, name='indexlab1'),
    path('cellxgene/', views.cellxgene, name='cellxgene'),
    path('cellxgene_contents/', views.cellxgene_contents, name='cellxgene_contents'),
    path('lab1singlecellapp/', views.lab1singlecellapp, name='lab1singlecellapp'),
    path('lab1singlecellapp_contents/', views.lab1singlecellapp_contents, name='lab1singlecellapp_contents'),
    path('lab1expressionapp/', views.lab1expressionapp, name='lab1expressionapp'),
    path('lab1expressionapp_contents/', views.lab1expressionapp_contents, name='lab1expressionapp_contents'),
    path('jupyterhub/', views.jupyterhub, name='jupyterhub'),
    path('rstudio/', views.rstudio, name='rstudio'),
    path('check/', views.check, name='check'),
]

# Change admin site title
admin.site.site_header = "Minuteman Administration"
admin.site.site_title = "Minuteman Admin Portal"
