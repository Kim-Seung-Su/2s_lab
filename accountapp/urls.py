from django.urls import path, include

from accountapp.views import hello_world

app_name = 'accountapp'

urlpatterns = [
    path('Hello_world/', hello_world, name="Hello World"),
    ]