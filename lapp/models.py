from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=300)
    password = models.CharField(max_length=300)
    objects = models.Manager()

    def __str__(self):
        return f'{str(self.pk)}: Name: {self.name}, Password: {self.password}'
    
class Order(models.Model):
    placed_by = models.CharField(max_length=300, default='Buyer')
    unit_price = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)
    supplier = models.CharField(max_length=300)
    item = models.CharField(max_length=300)
    quantity = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=300)
    status = models.CharField(max_length=300, default='Pending Payment')
    objects = models.Manager()

    def __str__(self):
        return f'{str(self.pk)}: Order Placed By {self.placed_by}, Supplier: {self.supplier}, Item: {self.item}, Quantity: {self.quantity}, Unit Price: {self.unit_price}, Total Price: {self.total_price}, Created on: {self.created_on}, Location: {self.location}, Status: {self.status}'
    
class SupplierStock(models.Model):
    name = models.CharField(max_length=300)
    item = models.CharField(max_length=300)
    quantity = models.IntegerField()
    stock_added_on = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return f'{str(self.pk)}: Supplier {self.name}, Stock: {self.item}, Quantity: {self.quantity}, Stock Added On: {self.stock_added_on}'
    
class BuyerStock(models.Model):
    supplier = models.CharField(max_length=300)
    item = models.CharField(max_length=300)
    quantity = models.IntegerField()
    stock_added_on = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return f'{str(self.pk)}: Supplier: {self.supplier}, Stock: {self.item}, Quantity: {self.quantity}, Stock Added On: {self.stock_added_on}'
    
class OrderHistory(models.Model):
    supplier = models.CharField(max_length=300)
    buyer = models.CharField(max_length=300, default='Buyer')
    item = models.CharField(max_length=300)
    quantity = models.IntegerField()
    total_price = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=300, default='Pending')
    objects = models.Manager()

    def __str__(self):
        return f'{str(self.pk)}: Supplier: {self.supplier}, Stock: {self.item}, Quantity: {self.quantity}, Total Price: {self.total_price}, Completed On: {self.date}'