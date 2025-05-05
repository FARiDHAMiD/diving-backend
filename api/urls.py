from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CourseViewSet, ProductViewSet, CartItemViewSet, OrderViewSet,
    UserProfileViewSet, RatingViewSet
)

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'products', ProductViewSet)
router.register(r'cart', CartItemViewSet, basename='cart')
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'profiles', UserProfileViewSet)
router.register(r'ratings', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
