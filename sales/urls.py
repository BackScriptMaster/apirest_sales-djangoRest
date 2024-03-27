from django.urls import path, include
from rest_framework import routers

from sales import views

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"sales", views.SaleViewSet)
router.register(r"products", views.ProductViewSet)

urlpatterns = [
    path("", include(router.urls))
]
