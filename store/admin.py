from django.contrib import admin
from store.models import Category,Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # the order to display the fields
    list_display = ['name','slug']

    # preopulate the slug field with to name of the category
    prepopulated_fields = {'slug':('name',)}



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','author','slug','price','in_stock','created_at','updated_at']

    # to filter the page automatically
    list_filter = ['in_stock','is_active']

    # create an editable list
    list_editable = ['price', 'in_stock']

    #prepopulate slug field with product title
    prepopulated_fields = {'slug':('title',)}

