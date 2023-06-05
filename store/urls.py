from django.urls import path
from store.views import (
    cart_view,
    sale_view,
    promo_view,
)

urlpatterns = [
    path('cart/', cart_view),
    path('sale/', sale_view),
    path('promo/', promo_view),
]
