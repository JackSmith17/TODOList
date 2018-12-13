"""todoList URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from todoListApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # When the request url is http://localhost:8000/hello_world/ which application context path is hello_world, 
    # then Django server will use request url path and process view function mappings defined in hello_world/urls.py.    
    path('', include(('todoListApp.urls')))
]
