from django.contrib import admin
from django.urls import path
from jenkins_ops import views
urlpatterns = [
    path('auth',views.auth_info),
    path('test',views.test),
    path('login',views.login),
    path('java_manage',views.java_manage),
    path('jenkins_manage',views.jenkins_manage),
    path('get_jobs',views.jenkins_get_jobs)
]