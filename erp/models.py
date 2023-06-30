import datetime

from django.db import models

# Create your models here.

class Employee(models.Model):

    name = models.CharField(
        max_length=20,
        null=False,
        blank=False
    )

    last_name = models.CharField(
        max_length=400,
        null=False,
        blank=False
    )

    cpf = models.CharField(
        max_length=14,
        null=False,
        blank = False
    )

    email = models.EmailField(
        max_length=50,
        null=False,
        blank = False
    )

    remuneration = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=False,
        blank=False
    )


class Product(models.Model):

    name = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )

    description = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=False,
        blank=False
    )


class Sale(models.Model):

    employee = models.ForeignKey(
        'employee',
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        'product',
        on_delete=models.CASCADE
    )

    date_hour_sale = models.DateTimeField(
        auto_now_add=True
    )
