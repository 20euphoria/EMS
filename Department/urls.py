from unicodedata import name
from django.urls import path, include
from .views import *

urlpatterns = [
    # path("home/", home, name="home"),
    path("get_data/", get_data, name="get_data"),
    path("post_dept/", post_dept, name="post_dept"),
]
