# Generated by Django 2.2 on 2023-07-10 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='ytlink',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]