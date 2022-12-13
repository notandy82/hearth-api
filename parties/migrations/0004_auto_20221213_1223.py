# Generated by Django 3.2.16 on 2022-12-13 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parties', '0003_remove_party_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='image',
            field=models.ImageField(blank=True, default='../default_post_q98lks', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='party',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
