# Generated by Django 4.0.5 on 2022-07-06 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_product_compound_delete_compound'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='primary_image',
            field=models.ImageField(default=0, upload_to='gallery'),
            preserve_default=False,
        ),
    ]
