from django.contrib import admin
from tpaga_project_1 import models

admin.site.register(models.Item)
admin.site.register(models.PurchaseOrder)