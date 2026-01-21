from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(AbstractUser):
    ROLE_CHOICES = (
        ('seller', 'seller'),
        ('buyer', 'buyer'),
    )

    user_role = models.CharField(
        max_length=30,
        choices=ROLE_CHOICES,
        default='buyer'
    )
    phone_number = PhoneNumberField(null=True, blank=True)
    avatar = models.ImageField(upload_to='user_photo', null=True, blank=True)
    def __str__(self):
        return f'{self.username} - {self.user_role}'



class Region(models.Model):
    region_name = models.CharField(max_length=30)

    def __str__(self):
        return self.region_name


class City(models.Model):
    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        related_name='cities'
    )
    city_name = models.CharField(max_length=30)

    def __str__(self):
        return self.city_name


class District(models.Model):
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name='districts'
    )
    district_name = models.CharField(max_length=30)

    def __str__(self):
        return self.district_name



class Property(models.Model):
    title = models.CharField(max_length=50)
    descriptions = models.TextField()

    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE
    )
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE
    )
    district = models.ForeignKey(
        District,
        on_delete=models.CASCADE
    )

    address = models.CharField(max_length=100)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    rooms = models.PositiveSmallIntegerField()
    floor = models.PositiveSmallIntegerField()
    total_floors = models.PositiveSmallIntegerField()
    condition = models.CharField(max_length=100)
    documents = models.BooleanField(default=False)

    video = models.ImageField(
        upload_to='video_photo',
        null=True,
        blank=True
    )

    seller = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='properties'
    )

    def __str__(self):
        return f'{self.title} - {self.city}'


class PropertyImg(models.Model):
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name='images'
    )
    property_img = models.ImageField(upload_to='property_photo')

    def __str__(self):
        return f'Image for {self.property.title}'


class Review(models.Model):
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    buyer = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    rating = models.PositiveSmallIntegerField(
        choices=[(i, str(i)) for i in range(1, 6)]
    )
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.buyer.username} - {self.rating}'
