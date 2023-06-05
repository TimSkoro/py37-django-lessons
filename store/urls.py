from django.urls import path
from store.views import *


urlpatterns = [
    path('cart/', cart_view),
    path('sale/', sale_view),
    path('promo/', promo_view),
]
