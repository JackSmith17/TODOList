from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # When request url is http://localhost:8000/hello_world/hello, it will invoke hello_world function defined in hello_world/views.py.
    # The first argument is the path relative to django application context path.
    path('hello', views.hello_world, name='helo_world'),
    path('',views.home, name="home"),
    path('delete/<list_id>', views.delete, name ='delete'),
    path('cross_off/<list_id>', views.cross_off, name ='cross_off'),
    path('uncross/<list_id>',   views.uncross, name ='uncross'),
    path('register',views.RegisterFormView.as_view(), name ='register'),
    path('login',views.LoginFormView.as_view(), name ='login'),
    path('logout',views.logOut, name ='logout'),
    path('filter',views.filter, name ='filter'),
]