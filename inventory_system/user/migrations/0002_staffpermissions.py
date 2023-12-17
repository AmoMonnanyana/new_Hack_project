# Generated by Django 5.0 on 2023-12-16 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffPermissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': (('view_dashboard', 'Can view dashboard'), ('manage_orders', 'Can manage orders'), ('manage_products', 'Can manage products'), ('view_products', 'Manage products'), ('view_inventory', 'Manage inventory')),
            },
        ),
    ]
