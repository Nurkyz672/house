from .models import Region,City,District,Property
from modeltranslation.translator import TranslationOptions,register

@register(Region)
class ProductTranslationOptions(TranslationOptions):
    fields = ('region_name',)


@register(City)
class ProductTranslationOptions(TranslationOptions):
    fields = ('region','city_name')


@register(District)
class ProductTranslationOptions(TranslationOptions):
    fields = ('city','district_name')


@register(Property)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title','descriptions',
              'address','area','rooms','floor',
              'total_floors','condition','documents','seller')
