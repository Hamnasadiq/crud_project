"""
URL configuration for accounting_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from accounts.views import (
    GroupListCreateView, LevelListCreateView, AccountMasterListCreateView,
    dashboard
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # API endpoints
    path('api/groups/', GroupListCreateView.as_view(), name='group-list'),
    path('api/levels/', LevelListCreateView.as_view(), name='level-list'),
    path('api/accounts/', AccountMasterListCreateView.as_view(), name='account-list'),

    # HTML dashboard
    path('', dashboard, name='dashboard'),
]
