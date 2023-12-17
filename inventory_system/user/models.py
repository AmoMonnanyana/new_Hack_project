from django.db import models
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


# Create your models here.
class CustomerPermissions(models.Model):
    class Meta:
        permissions = (
            ("view_cart", "Can view cart"),
            ("add_to_cart", "Can add items to cart"),
            ("remove_from_cart", "Can remove items from cart"),
            ("update_cart", "Can update cart"),
            ("clear_cart", "Can clear cart"),
            ("checkout", "Can proceed to checkout"),
            ("view_order_history", "Can view order history"),
            ("view_product_details", "Can view product details"),
        )

class StaffPermissions(models.Model):
    class Meta:
        permissions = (
            ("view_dashboard", "Can view dashboard"),
            ("manage_orders", "Can manage orders"),
            ("manage_products", "Can manage products"),
            ("view_products", "Manage products"),
            ("view_inventory", "Manage inventory")
            # Add more permissions as needed
        )

class SupplierPermissions(models.Model):
    class Meta:
        permissions = (
            ("view_inventory", "Manage inventory"),
            ("add_products", "Add products to inventory")
            # Add more permissions as needed
        )

class accountantPermissions(models.Model):
  
    class Meta:
        permissions = (
            ("view_records", "Manage records"),
            ("add_record", "Add record"),
            ("update_record", "Update records"),
            # Add more permissions as needed
        )