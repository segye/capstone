from django.urls import path
from .views import ProductListAPI, ProductDetailAPI, ProductTopAPI, ProductPantsAPI

urlpatterns = [
    path('list/', ProductListAPI.as_view(), name="list"),
    path('top/', ProductTopAPI.as_view(), name="상의"),
    path('pants/', ProductPantsAPI.as_view(), name="하의"),
    path('list/<int:pk>/', ProductDetailAPI.as_view(), name="detail"),

]