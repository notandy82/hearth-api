# Generated by Django 3.2.16 on 2022-12-15 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20221213_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]