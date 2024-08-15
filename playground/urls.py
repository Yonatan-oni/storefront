from django.urls import path
from . import views


# building data model 5 create

urlpatterns = [
    path('hello/', views.say_hello)

]