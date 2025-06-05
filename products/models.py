from django.db import models

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
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product_image")