from .models import Product 

class ProductCrud:
    @classmethod
    def get_all_products(cls):
        return Product.objects.all()

    @classmethod
    def find_by_model(cls, model):
        return Product.objects.get(model='Heavy Duty Steel Clock')
    
    @classmethod
    def last_record():
        return 
