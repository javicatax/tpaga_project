from django.db import models

# Create your models here.

CREATED = "created"
PAID = "paid"
DELIVERED = "delivered"


class Item(models.Model):
    """
        Items to buy
    """
    name = models.CharField(max_length=180, blank=True, null=True)
    value = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.name)


class PurchaseOrder(models.Model):
    """
        Purchase order model to save payments information
    """
    STATUS_CHOICES = (
        (CREATED, "Created"),
        (PAID, "Paid"),
        (DELIVERED, "Delivered"),
    )

    start_time = models.DateTimeField(auto_now=True)
    purchase_description = models.CharField(max_length=180, blank=True, null=True)
    cost = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    status = models.CharField(max_length=80, blank=True, null=True, choices=STATUS_CHOICES)
    tpaga_payment_url = models.CharField(max_length=240, blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    items = models.ManyToManyField('PurchaseItem')

    def __str__(self):
        return '{}'.format(self.pk)


class PurchaseItem(models.Model):
    """
        Purchase order item model to save items for
    """
    order = models.ForeignKey('PurchaseOrder', on_delete=models.CASCADE)
    item = models.ForeignKey('Item', on_delete=models.CASCADE)

    def __str__(self):
        return '{}-{}'.format(self.order, self.item)