# Develop: vmgabriel

"""Models of APP: Transaction"""

from django.db import models


class Repeter(models.Model):
    """Repeter Model for datein control data"""
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    hourly = models.IntegerField(default=0)
    each_day = models.IntegerField(default=0)
    weekly = models.IntegerField(default=0)
    each_month = models.IntegerField(default=0)
    each_year = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        data = 'name: {}, hourly: {}, each day: {}, weekly: {}, each month: {}'
        return data.format(
            self.name,
            self.hourly,
            self.each_day,
            self.weekly,
            self.each_month
        )


class Priority(models.Model):
    """Priority Model for Data Based in Priority"""
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        data = 'name: {}, is deleted: {}'
        return data.format(self.name, self.is_delete)


class Category(models.Model):
    """Category Model for data Based in Consume"""
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    is_delete = models.BooleanField(default=False)
    priority = models.ForeignKey(
        Priority,
        on_delete=models.CASCADE
    )

    def __str__(self):
        data = 'name: {}, is deleted: {}'
        return data.format(self.name, self.is_delete)


class TypeConsume(models.Model):
    """Type Consume Data for Module"""
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        data = 'name: {}, is deleted: {}'
        return data.format(self.name, self.is_delete)


class Consume(models.Model):
    """Product Class That Input or Output Data"""
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    is_delete = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    type_consume = models.ForeignKey(
        TypeConsume,
        on_delete=models.CASCADE
    )

    def __str__(self):
        data = 'name: {}, is deleted: {}'
        return data.format(self.name, self.is_delete)


class TypeBill(models.Model):
    """Type Transaction Model, This Data Get Entrance/Exit en Data"""
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        data = 'name: {}, is deleted: {}'
        return data.format(self.name, self.is_delete)


class Bill(models.Model):
    """Transaction Model, this show Input/Output"""
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    date = models.DateTimeField()
    is_delete = models.BooleanField(default=False)
    is_repeter = models.BooleanField()
    repeter = models.ForeignKey(
        Repeter,
        on_delete=models.CASCADE
    )
    type_bill = models.ForeignKey(
        TypeBill,
        on_delete=models.CASCADE
    )

    def __str__(self):
        data = 'name: {}, date: {}, is_repeter: {}'
        return data.format(self.name, self.date, self.is_repeter)


class Transaction(models.Model):
    """Transaction Connection"""
    description = models.CharField(max_length=250)
    date_payed = models.DateTimeField()
    is_delete = models.BooleanField(default=False)
    consume = models.ForeignKey(
        Consume,
        on_delete=models.CASCADE
    )
    bill = models.ForeignKey(
        Bill,
        on_delete=models.CASCADE
    )

    def __str__(self):
        data = 'date payed: {}, is deleted: {}'
        return data.format(self.date_payed, self.is_delete)
