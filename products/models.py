from django.db import models
from django.db.models import Q
from django.utils import timezone

# Create your models here.


class AuditData(models.Model):
    createdAt=models.DateTimeField(default=timezone.now, editable=False)
    modifiedAt=models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True


class Category(AuditData):
    name = models.CharField(max_length=255, primary_key=True)

    class Meta:
        ordering = ("name",)
        indexes = [
            models.Index(fields=["name"]),
        ]


class Product(AuditData):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.IntegerField()


    class Meta:
        constraints = [
            models.CheckConstraint(
                check=Q(stock__gte=0), name="stock_preie_greater_than0"
            )
        ]


class ProductDescription(AuditData):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="description")
    description = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)


class Order(AuditData):
    product = models.ManyToManyField(Product, related_name="products")
    amount = models.DecimalField(max_digits=10, decimal_places=2)

