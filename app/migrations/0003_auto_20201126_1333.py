# Generated by Django 3.1 on 2020-11-26 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20201126_1322'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productimage',
            old_name='image',
            new_name='file',
        ),
        migrations.AddField(
            model_name='productimage',
            name='name',
            field=models.CharField(default=True, max_length=20),
            preserve_default=False,
        ),
    ]