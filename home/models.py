from django.db import models

# Create your models here.


class Create_user(models.Model):

    name = models.CharField(max_length=25, null=False)
    password = models.CharField(max_length=12, null=False)
    email= models.EmailField(max_length=254)
    phone_number = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name