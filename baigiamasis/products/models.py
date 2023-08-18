from django.db import models

class ScrapedProduct(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    image = models.ImageField()


    def __init__(self, name, price, image):

        self.name = name
        self.price = price
        self.image = image





class ScrapedRecipes(models.Model):
    title = models.CharField(max_length=200)


    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name