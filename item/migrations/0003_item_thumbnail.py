# Generated by Django 4.1.6 on 2023-03-03 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_category_options_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='item_images'),
        ),
    ]
