from django.urls import path
from . import views


# start with mapping url -9

urlpatterns = [
    path('hello/', views.say_hello)

]