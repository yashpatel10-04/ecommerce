from django.contrib import admin
from .models import Profile, Product, Cart, Watchlist, Order, Review

admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Watchlist)
admin.site.register(Order)
admin.site.register(Review)