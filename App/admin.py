from django.contrib import admin
from .models import ProductCard, Notification
from django.template.defaultfilters import slugify

admin.site.register(ProductCard)
admin.site.register(Notification)

class ProductCardAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter =['title', 'price']
    prepopulated_fields = {'slag(title)'}

    def save(self, *args, **kwargs):
        if self.slug:
            self.slug=slugify(self.title) 
            super(ProductCard, self).save(*args, **kwargs)