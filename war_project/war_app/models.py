from django.db import models

class donate_table(models.Model):
    country=models.CharField(max_length=20)
    pincode=models.CharField(max_length=10)
    name=models.CharField(max_length=20)
    dob=models.DateField()
    phone_number=models.CharField(max_length=14)
    email=models.EmailField()

class cloth_table(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.FileField(upload_to="media")
 
    def __str__(self):
        return self.name
    
class bed_table(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.FileField(upload_to="media")
 
    def __str__(self):
        return self.name  

class med_table(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.FileField(upload_to="media")
 
    def __str__(self):
        return self.name    

class food_table(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.FileField(upload_to="media")
 
    def __str__(self):
        return self.name 

class kitchen_table(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.FileField(upload_to="media")
 
    def __str__(self):
        return self.name    

class communication_table(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.FileField(upload_to="media")
 
    def __str__(self):
        return self.name           

class cart_item(models.Model):
    product_type = models.CharField(max_length=50)
    product_id = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product_type} - {self.product_id}"    
# Create your models here.
