from django.urls import path

from news.views import id_view, slug_view

urlpatterns = [
    path('slug_test/<int:id>', id_view),
    path('slug_test/<str:name_of_news>', slug_view),
]
