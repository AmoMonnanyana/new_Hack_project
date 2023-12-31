# Generated by Django 5.0 on 2023-12-17 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_staffpermissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='accountantPermissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': (('view_records', 'Manage records'), ('add_record', 'Add record'), ('update_record', 'Update records')),
            },
        ),
        migrations.CreateModel(
            name='SupplierPermissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': (('view_inventory', 'Manage inventory'), ('add_products', 'Add products to inventory')),
            },
        ),
    ]
