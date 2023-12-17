from django.contrib import admin
from .models import CustomerPermissions, StaffPermissions, SupplierPermissions, accountantPermissions

# Register your models here.
admin.site.register(CustomerPermissions)
admin.site.register(StaffPermissions)
admin.site.register(SupplierPermissions)
admin.site.register(accountantPermissions)