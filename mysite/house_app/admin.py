from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import (
    UserProfile,
    Region, City, District,
    Property, PropertyImg, Review,
)





@admin.register(Property)
class ProductAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }



class CityInline(admin.TabularInline):
    model = City
    fk_name = 'region'
    extra = 1


class DistrictInline(admin.TabularInline):
    model = District
    fk_name = 'city'
    extra = 1


class PropertyImgInline(admin.TabularInline):
    model = PropertyImg
    extra = 1


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0
    readonly_fields = ('created_date',)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'user_role', 'phone_number',)
    list_filter = ('user_role',)
    search_fields = ('username', 'phone_number')


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('region_name',)
    inlines = [CityInline]


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('city_name', 'region')
    inlines = [DistrictInline]




@admin.register(PropertyImg)
class PropertyImgAdmin(admin.ModelAdmin):
    list_display = ('property',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('property', 'buyer', 'rating', 'created_date')
    readonly_fields = ('created_date',)
