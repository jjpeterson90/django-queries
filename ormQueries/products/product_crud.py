from .models import Product
import pprint

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
    def by_rating_and_color(cls):
        
        pass
    
    @classmethod
    def by_rating_or_color(cls):
        pass
    
    @classmethod
    def no_color_count(cls):
        pass
    
    @classmethod
    def below_price_or_above_rating(cls):
        pass
    
    @classmethod
    def ordered_by_category_alphabetical_order_and_then_price_descending(cls):
        pass
    
    @classmethod
    def products_by_manufacturer_with_name_like(cls):
        pass
    
    @classmethod
    def manufacturer_names_for_query(cls):
        pass
    
    @classmethod
    def not_in_a_category(cls):
        pass
    
    @classmethod
    def limited_not_in_a_category(cls):
        pass
    
    @classmethod
    def category_manufacturers(cls):
        pass
    
    @classmethod
    def average_category_rating(cls):
        pass
    
    @classmethod
    def greatest_price(cls):
        pass
    
    @classmethod
    def longest_model_name(cls):
        pass
    
    @classmethod
    def ordered_by_model_length(cls):
        pass