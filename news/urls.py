from django.urls import path, include

from news.views import *

urlpatterns = [
    path('slug_test/<int:id>', id_view),
    path('slug_test/<str:name_of_news>', slug_view),
]
