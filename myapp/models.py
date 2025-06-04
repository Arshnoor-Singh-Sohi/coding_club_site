from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField()
    city = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    CATEGORY_CHOICES = [
        ('S', 'Science & Tech'),
        ('F', 'Fiction'),
        ('B', 'Biography'),
        ('T', 'Travel'),
        ('O', 'Other'),
    ]
    title = models.CharField(max_length=200)
    category = models.CharField(
        max_length=1,
        choices=CATEGORY_CHOICES,
        default='S'
    )
    num_pages = models.PositiveIntegerField(default=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    publisher = models.ForeignKey(
        Publisher,
        related_name='books',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"

