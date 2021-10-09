from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', blank=True, null=True)
    email = models.EmailField()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    one = "1"
    two = "2"
    three = "3"
    four = "4"
    five = "5"
    Rating = [
        (one, 1),
        (two, 2),
        (three, 3),
        (four, 4),
        (five, 5),
    ]
    name = models.CharField(max_length=50)
    total = models.IntegerField()
    Available_colors = models.CharField(max_length=50)
    rating = models.CharField(max_length=1, choices=Rating, default="",)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, default="", on_delete=models.CASCADE, blank=True, null=True, )
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(upload_to='products' ,null=True, blank=True)
    # product_slug = models.SlugField(max_length=50, default=1, blank=True, null=True) # new
    product_slug = models.SlugField(max_length=50, null=True, blank=True, help_text="Product Slug is a url for that Specific Product, Please Don't Edit this if you don't have to")
    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    @property
    def product_url(self):
        prod_url = self.name + str(self.id)
        return str(prod_url)


class productDetails(models.Model):
    name = models.ForeignKey(Product, default="", on_delete=models.CASCADE)
    brand = models.CharField(max_length=50)
    size = models.CharField(max_length=30)
    # color = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Product Details"


class ProductRating(models.Model):
    one = "1"
    two = "2"
    three = "3"
    four = "4"
    five = "5"
    Rating = [
        (one, 1),
        (two, 2),
        (three, 3),
        (four, 4),
        (five, 5),
    ]
    rating = models.CharField(max_length=1, choices=Rating, default="",)
    name = models.ForeignKey(Product, default="", on_delete=models.CASCADE)
    # rating = models.IntegerField(blank=True, null=True, )

    class Meta:
        verbose_name_plural = "Product Rating"

    def __str__(self):
        return self.rating


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
    	shipping = False
    	orderitems = self.orderitem_set.all()
    	for i in orderitems:
    		if i.product.digital == False:
    			shipping = True
    	return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
