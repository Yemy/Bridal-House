from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group

class CustomerAdmin(admin.ModelAdmin):
	list_display = ('user', 'name', 'email')
	search_fields = ('name', 'email', )


class ProductCategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'total', 'Available_colors', 'rating')
	search_fields = ('name', )
	list_filter = ['rating']


class DetailsInline(admin.TabularInline):
	model = productDetails


class ProductAdmin(admin.ModelAdmin):
	inlines = [
	    DetailsInline,
	]
	list_display = ('name', 'price', 'digital', 'product_url')
	search_fields = ('name', )
	prepopulated_fields = {'product_slug': ('name', )}
	list_filter = ['digital', 'price', ]


class RatingAdmin(admin.ModelAdmin):
	list_display = ('name', 'rating')
	list_filter = ['rating']
	search_fields = ('name', )


class OrderAdmin(admin.ModelAdmin):
	list_display = ('transaction_id', 'customer', 'date_ordered', 'complete')
	search_fields = ('transaction_id', )
	list_per_page = 10
	list_filter = ['date_ordered', 'customer', 'complete', 'transaction_id', ]


class OrderItemAdmin(admin.ModelAdmin):
	list_display = ('product', 'order', 'quantity', 'date_added')
	list_per_page = 10
	list_filter = ['date_added', 'product', 'order', 'quantity', ]


class ShippingAddressAdmin(admin.ModelAdmin):
	list_display = ('customer', 'order', 'address', 'city', 'state', 'zipcode', 'date_added')
	search_fields = ('zipcode', )
	list_per_page = 10
	list_filter = [ 'order', 'address', 'city', 'state', 'zipcode', 'customer', ]



admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(ShippingAddress, ShippingAddressAdmin)
admin.site.register(ProductRating, RatingAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)


admin.site.site_header = "Amore Bridal House Admin Dashboard"
admin.site.site_footer = "Amore Bridal Admin Dashboard"
admin.site.site_title = "Amore Bridal Admin Page"
admin.site.index_title = " Wellcome to Amore Bridal"
admin.site.site_url = " Amore Bridal "
