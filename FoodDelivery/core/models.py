from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=13, blank=True, null=True)
    bonus_coin = models.IntegerField(default=0)


class NameIt(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Category(NameIt):
    pass


class Product(NameIt):
    price = models.IntegerField(null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    compound = models.TextField(null=True)
    description = models.TextField(null=True)


class ProductImage(models.Model):
    image = models.ImageField(upload_to='images', verbose_name='Изображение_товара')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.id


class Reviews(models.Model):
    body = models.TextField()
    publish_date = models.DateTimeField(blank=True, null=True)
    is_published = models.BooleanField(default=False)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.body


# Create your models here.
