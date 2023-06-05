from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    sale = models.BooleanField(default=False, editable=False)
    sale_count = models.FloatField(default=1, editable=False)  # 0.8 = 20%

    @property
    def current_price(self):
        return round(float(self.price) * self.sale_count, 2)

    def __str__(self):
        return self.title


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    done = models.BooleanField(default=False)

    @property
    def price(self):
        result = 0
        for product in self.products.all():
            result += product.current_price
        return result

    def save(self, *a, **kw):
        if self.done:
            Order.objects.create(total_price=self.price, user=self.user)


class Order(models.Model):
    total_price = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class Frame(models.Model):
    title = models.CharField(max_length=200, )

    def __str__(self):
        return self.title


class Brands(models.TextChoices):
    BMW = 'bmw'
    GEELY = 'geely'
    TESLA = 'tesla'


class Car(models.Model):
    brand = models.CharField(max_length=200, choices=Brands.choices)
    seria = models.CharField(max_length=200)
    date_of_create = models.DateField()
    frames = models.ManyToManyField(Frame)
    owner = models.ForeignKey(User,
                              on_delete=models.SET_NULL,
                              null=True,
                              limit_choices_to={"is_staff": False},
                              related_name='cars'
                              )

    def __str__(self):
        return f"{self.brand}-{self.seria}"

#
# class Employee(models.Model):
#     name = models.CharField(max_length=200)
#     boss = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)
#
