from django.db import models

class Category(models.Model):

    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category

class Items(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=35)
    brand = models.CharField(max_length=20)
    letter_size = models.CharField(max_length=16, blank=True)
    number_size = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    price = models.DecimalField(max_digits=20000 ,decimal_places=2)
    item_img = models.ImageField(default='no_image.png')

    def __str__(self):
        return self.name
