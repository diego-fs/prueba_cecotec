##Third party imports
from django.urls import re_path
##Local application imports
from .views import ArticleList


app_name = "articles"

urlpatterns = [
    re_path(r"articles/?$", ArticleList.as_view(), name="article_list"),
]