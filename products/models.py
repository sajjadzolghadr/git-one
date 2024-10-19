from tabnanny import verbose
from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save

#create customer profile
class Profile(models.Model):
   user = models.OneToOneField(User , on_delete = models.CASCADE)
   date_modified = models.DateTimeField(user , auto_now = True)
   phone = models.CharField(max_length=20 , blank=True)
   address1 = models.CharField(max_length=200 , blank=True)
   address2 = models.CharField(max_length=200 , blank=True)
   city =  models.CharField(max_length=200 , blank=True)
   state =  models.CharField(max_length=200 , blank=True)
   zipcode =  models.CharField(max_length=200 , blank=True)
   country =  models.CharField(max_length=200 , blank=True)
   old_cart = models.CharField(max_length=200 , blank=True , null = True)

   def __str__(self):
      return self.user.username
   
# create a user profile by defualt when user signs up
def create_profile(sender , instance , created , **kwargs):
   if created : 
      user_profile = Profile(user = instance)
      user_profile.save()
#automate the profile thing
post_save.connect(create_profile , sender = User)




# Categgories of Products
class Category (models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category/product/', null=True, blank=True)
    
    def __str__ (self): 
        return self.name
    class Meta:
        verbose_name_plural = 'categories'


    
    

    





# Customers
class Customers (models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 10)
    email = models.EmailField(max_length = 100)
    passworde = models.CharField(max_length = 100)
    def __srt__(self):
     return '{self.first_name}  {self.last_name}'




# All of our Products
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0 , decimal_places= 2 , max_digits=6)
    category = models.ForeignKey(Category ,on_delete=models.CASCADE  ,default= 1)
    image = models.ImageField(upload_to='uploads/product/')
    description = models.CharField(max_length=250 , default='' , blank=True , null=True)
    #add Sale Stuff
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0 , decimal_places= 2 , max_digits=6)

    def __str__ (self):
     return self.name

 

# Customers Orders
class Order(models.Model):
    product = models.ForeignKey(Product , on_delete=models.CASCADE )
    costumers = models.ForeignKey(Customers , on_delete=models.CASCADE )
    quantity = models.IntegerField(default= 1)
    address = models.CharField(max_length=100 , default ='' , blank = True )
    phone = models.CharField(max_length= 20 , default ='' , blank = True )
    date = models.DateField(datetime.datetime.today)
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.product


    


class Offer(models.Model):
    code = models.CharField(max_length=10)
    descriptions = models.CharField(max_length = 253)
    discount = models.FloatField()

    