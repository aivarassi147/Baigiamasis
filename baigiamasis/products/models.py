from django.db import models


class ScrapedProduct(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    image = models.ImageField(null=True)


    def __init__(self, name, price, image, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.price = price
        self.image = image



class ScrapedRecipes(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True)
    link = models.URLField(max_length=200)

    def __init__(self, title, image, link, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = title
        self.image = image
        self.link = link

