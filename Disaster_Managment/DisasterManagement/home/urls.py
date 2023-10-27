from django.contrib import admin
from django.urls import path
from home import views
from django.urls import path
#from .views import index, ChatbotViewSet


urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('contactus', views.contact, name='contactus'),
    path('about', views.about, name='about'),
    path('signup', views.signup, name='signup'),
    path('login', views.Login, name='login'),
    path('next', views.next, name='next'),
    path('blog', views.blog, name='blog'),
#    path('chatbot', ChatbotViewSet.as_view()),

]