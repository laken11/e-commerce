# Generated by Django 3.1 on 2020-12-13 12:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20201130_1054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='Product',
            new_name='product',
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='date_crated',
            field=models.DateField(default=datetime.date(2020, 12, 13)),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.order'),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product'),
        ),
    ]
