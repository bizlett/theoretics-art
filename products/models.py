from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Art(models.Model):
    product = models.ForeignKey(
        'Product', null=True, blank=True, on_delete=models.CASCADE)
    dimensions = models.CharField(max_length=254, null=True, blank=True)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name


class Photography(models.Model):
    product = models.ForeignKey(
        'Product', null=True, blank=True, on_delete=models.CASCADE)
    sku = models.CharField(max_length=254, null=True, blank=True)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name


class Size(models.Model):
    product = models.ForeignKey(
        'Photography', null=True, blank=True, on_delete=models.CASCADE)
    size = models.CharField(max_length=254)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.size
