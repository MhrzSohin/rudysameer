from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Feedback)
admin.site.register(Slider)
admin.site.register(Feature)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'labels', 'slug')
    list_filter = ('name', 'price', 'category', 'labels','slug')
    search_fields = ('name', 'description')

    class Meta:
        ordering = ('id', 'name', 'price')


admin.site.register(Service)
admin.site.register(ProductReviews)
admin.site.register(Cart)
admin.site.register(Checkout)
