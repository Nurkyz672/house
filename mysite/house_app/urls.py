from django.urls import path,include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .views import (UserProfileViewSet,RegionViewSet,CityViewSet,
                    DistrictViewSet,PropertyViewSet,PropertyImgViewSet,ReviewViewSet)

router = routers.DefaultRouter()
router.register(r'user',UserProfileViewSet)
router.register(r'region',RegionViewSet)
router.register(r'city',CityViewSet)
router.register(r'district',DistrictViewSet)
router.register(r'property',PropertyViewSet)
router.register(r'propertyImg',PropertyImgViewSet)
router.register(r'review',ReviewViewSet)

urlpatterns = [
    path('',include(router.urls)),
]