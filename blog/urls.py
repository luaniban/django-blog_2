from django.urls import path
from blog.views import index, ola

urlpatterns = [
    path('', index, name= "home"),
    path('index/', index, name= "index"),
    path('ola/', ola, name= "ola")
]
