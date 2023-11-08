from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Feedback)
admin.site.register(Slider)
admin.site.register(Feature)
admin.site.register(Product)
admin.site.register(Service)
admin.site.register(ProductReviews)
admin.site.register(Cart)