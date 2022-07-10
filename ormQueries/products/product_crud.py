from django.db.models.functions import Length
from django.db.models import *
from .models import Product

class ProductCrud:
    @classmethod
    def get_all_products(cls):
        data = Product.objects.all()
        return data

    @classmethod
    def find_by_model(cls, model):
        data = Product.objects.get(model=model)
        return data
    
    @classmethod
    def last_record(cls):
        data = Product.objects.last()
        return data
    
    @classmethod
    def by_rating(cls, rating):
        data = Product.objects.filter(rating=rating)
        return data
    
    @classmethod
    def by_rating_range(cls, rating_low, rating_high):
        data = Product.objects.filter(rating__range=(rating_low,rating_high))
        return data
    
    @classmethod
    def by_rating_and_color(cls, rating, color):
        data = Product.objects.filter(Q(rating=rating) & Q(color=color))
        return data
    
    @classmethod
    def by_rating_or_color(cls, rating, color):
        data = Product.objects.filter(Q(rating=rating) | Q(color=color))
        return data
    
    @classmethod
    def no_color_count(cls):
        data = Product.objects.filter(color=None).count()
        return data
    
    @classmethod
    def below_price_or_above_rating(cls, price, rating):
        data = Product.objects.filter(Q(price_cents__lt=price) | Q(rating__gt=rating))
        return data
    
    @classmethod
    def ordered_by_category_alphabetical_order_and_then_price_decending(cls):
        data = Product.objects.order_by('category', F('price_cents').desc())
        return data
    
    @classmethod
    def products_by_manufacturer_with_name_like(cls, manufacturer):
        data = Product.objects.filter(manufacturer__contains=manufacturer)
        return data
    
    @classmethod
    def manufacturer_names_for_query(cls, manufacturer):
        data = Product.objects.filter(manufacturer__contains=manufacturer).values_list('manufacturer', flat=True)
        return data
    
    @classmethod
    def not_in_a_category(cls, category):
        data = Product.objects.exclude(category=category)
        return data
    
    @classmethod
    def limited_not_in_a_category(cls, category, limit):
        data = Product.objects.exclude(category=category)[:limit]
        return data
    
    @classmethod
    def category_manufacturers(cls, category):
        data = Product.objects.filter(category=category).values_list('manufacturer', flat=True)
        return data
    
    @classmethod
    def average_category_rating(cls, category):
        data = Product.objects.filter(category=category).aggregate(Avg('rating'))
        return data
    
    @classmethod
    def greatest_price(cls):
        data = Product.objects.all().aggregate(Max('price_cents'))
        return data
    
    @classmethod
    def longest_model_name(cls):
        data = Product.objects.annotate(length=Length('model')).order_by(F('length').desc())[0].pk
        return data
    
    @classmethod
    def ordered_by_model_length(cls):
        data = Product.objects.annotate(length=Length('model')).order_by('length').values_list('pk', flat=True)
        return data