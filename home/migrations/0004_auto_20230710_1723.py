# Generated by Django 2.2 on 2023-07-10 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20230710_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='ytlink',
            field=models.CharField(max_length=1000),
        ),
    ]