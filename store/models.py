from django.db import models

class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class Collection(models.Model):
    title = models.CharField(max_length=255)
    fetaured_product = models.ForeignKey('Products', on_delete=models.SET_NULL, null=True, related_name="+")


class Products(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(default='-')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    # one to many relation between collections and products
    # single collection can have multiple products
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)

    # many to many relation
    products = models.ManyToManyField(Promotion)


class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, "Bronze"),
        (MEMBERSHIP_SILVER, "Silver"),
        (MEMBERSHIP_GOLD, "Gold")
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1,choices=MEMBERSHIP_CHOICES,default=MEMBERSHIP_BRONZE)

    class Meta:
        indexes = [models.Index(fields=['last_name', 'first_name'])]


class Order(models.Model):
    ORDER_PENDING = 'P'
    ORDER_COMPLETE = 'C'
    ORDER_FAILED = 'F'
    ORDER_STATUS = [
        (ORDER_PENDING, "Pending"),
        (ORDER_COMPLETE, "Complete"),
        (ORDER_FAILED, "Failed")
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1,choices=ORDER_STATUS,default=ORDER_PENDING)
   
    # one to many relation between Customer and Order
    # Customer can have multiple orders 
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


class OrderItem(models.Model):
    title = models.CharField(max_length=255)
    
    # one to many relations
    order = models.ForeignKey(Order, on_delete=models.CASCADE)    
    product = models.ForeignKey(Products, on_delete=models.PROTECT)
    
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6,decimal_places=2)



class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    # primary_key is neccesary to make it one to one relation
    # customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)
    
    # one to many relation between customer and addresses
    # single customer can have multiple addresses
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()

