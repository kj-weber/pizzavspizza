from django.core.validators import RegexValidator
from django.db import models

class Pizzeria(models.Model):
    pizzera_name = models.CharField(max_length=100, blank=False)
    street = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zip_code = models.IntegerField(blank=True, default=0)
    website = models.URLField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=200, validators=[RegexValidator(regex=r'^\1?\d{9,10}$')])
    description = models.TextField(blank=True)
    # logo_image = models.ImageField(
    #     upload_to='pizzariaImages',
    #     blank=True,
    #     default='pizzariaImages/pizzalogo.png'
    # )
    email = models.EmailField(max_length=245, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "{}, {}".format(self.pizzera_name, self.city)