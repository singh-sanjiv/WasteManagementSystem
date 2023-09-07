# Generated by Django 4.2.1 on 2023-07-17 19:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('waste', '0017_alter_purchase_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='stock',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='purchase',
            name='quantity',
            field=models.CharField(default=1, max_length=1, null=True),
        ),
        migrations.CreateModel(
            name='stock_his',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('qty', models.CharField(max_length=4, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waste.products')),
            ],
        ),
    ]
