from .models import UserProfile,Region,City, District,Property,PropertyImg,Review
from .serializers import (UserProfileSerializer,RegionSerializer,CitySerializer,
                          DistrictSerializer,PropertySerializer,
                          PropertyImgSerializer,ReviewSerializer)
from rest_framework import viewsets



class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class PropertyImgViewSet(viewsets.ModelViewSet):
    queryset = PropertyImg.objects.all()
    serializer_class = PropertyImgSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

