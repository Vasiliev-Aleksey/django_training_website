# Generated by Django 4.2 on 2023-04-26 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_alter_order_order_name_alter_order_order_phone_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
    ]