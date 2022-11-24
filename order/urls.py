from django.urls import path
from .views import CartView, CartDetailAPIView

urlpatterns = [
    path('cartview/', CartView.as_view(), name="장바구니"),
    path('cartview/<int:pk>/', CartDetailAPIView.as_view(), name="장바구니상세"),
]
