# Generated by Django 4.2.1 on 2023-07-31 14:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('waste', '0024_alter_products_status_alter_stock_his_qty'),
    ]

    operations = [
        migrations.AddField(
            model_name='collector_registration',
            name='collector_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='purchase',
            name='total',
            field=models.IntegerField(null=True),
        ),
    ]
