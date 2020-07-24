# Develop: vmgabriel

"""Admininistrator Content for Transaction"""

from django.contrib import admin

from . import models


admin.site.register(models.Repeter)
admin.site.register(models.Priority)
admin.site.register(models.Category)
admin.site.register(models.TypeConsume)
admin.site.register(models.Consume)
admin.site.register(models.TypeBill)
admin.site.register(models.Bill)
admin.site.register(models.Transaction)
