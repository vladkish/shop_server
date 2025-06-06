from django.db import models
from users.models import User

class Category(models.Model):
    title = models.CharField(max_length=60)
    
    def __str__(self):
        return f"{self.title}"
    

# Class Product
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title} | {self.price}"
    
# Create class for photo.
class ProductImage(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to="product_image/")

# Manager model Basket.
class Manager(models.QuerySet):
    # total quantity.
    # self == QuerySet
    def total_quantity(self):
        total = 0
        for basket in self:
            total += basket.quantity
        return total
    
    def total_sum(self):
        total = 0
        for basket in self:
            total += basket.sum()
        return total
    
# Basket
class Basket(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    date_add = models.DateTimeField(auto_now_add=True)
    objects = Manager.as_manager()
    
    def __str__(self):
        return f"{self.product} for {self.user}"
    
    # Fnc sum for basket.
    def sum(self):
        return self.product.price * self.quantity