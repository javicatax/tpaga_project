# Generated by Django 3.1.6 on 2021-02-08 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tpaga_project_1', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PurchaseItems',
            new_name='PurchaseItem',
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='items',
            field=models.ManyToManyField(to='tpaga_project_1.PurchaseItem'),
        ),
    ]