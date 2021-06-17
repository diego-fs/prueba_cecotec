from django.urls import re_path
from .views import UserList

app_name = "users"

urlpatterns = [
    re_path(r"user/?$", UserList.as_view(), name="User_list"),
]