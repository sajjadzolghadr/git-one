from django.contrib import admin
from .models import Product , Profile
from .models import Category
from .models import Order
from .models import Customers
from .models import Offer
from django.contrib.auth.models import User





admin.site.register(Offer)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Customers)
admin.site.register(Order)
admin.site.register(Profile)





# mix profile info and user info
class ProfileInline(admin.StackedInline):
    model = Profile
    
# extend user model
class UserAdmin(admin.ModelAdmin):
    model = User
    field = ['username' , 'first_name' , 'last_name' , 'email' , ]
    inlines = [ProfileInline]
#vvvvv
admin.site.unregister(User)
#bbbbbbb
admin.site.register(User , UserAdmin)



