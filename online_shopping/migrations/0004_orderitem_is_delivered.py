# Generated by Django 4.2.5 on 2023-11-14 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_shopping', '0003_alter_category_options_product_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='is_delivered',
            field=models.BooleanField(default=False),
        ),
    ]