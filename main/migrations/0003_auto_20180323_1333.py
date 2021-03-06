# Generated by Django 2.0.2 on 2018-03-23 13:33

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20180322_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 3, 23, 13, 33, 46, 520727, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='traded',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trade_product', to='main.Product'),
        ),
        migrations.AlterField(
            model_name='traderequest',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trade_request_product', to='main.Product'),
        ),
    ]
