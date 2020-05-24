from django.db import models
from django.utils import timezone


class Entry(models.Model):
    entryID = models.CharField(max_length=1000, )
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True, null=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return (self.entryID)


class Food(models.Model):
    entryID = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name='Food')
    food_name = models.CharField(max_length=1000, )
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    fiber = models.DecimalField(max_digits=10, decimal_places=2)
    vitamin_a = models.DecimalField(max_digits=10, decimal_places=2)
    vitamin_b6 = models.DecimalField(max_digits=10, decimal_places=2)
    vitamin_b9 = models.DecimalField(max_digits=10, decimal_places=2)
    vitamin_b12 = models.DecimalField(max_digits=10, decimal_places=2)
    vitamin_c = models.DecimalField(max_digits=10, decimal_places=2)
    vitamin_d = models.DecimalField(max_digits=10, decimal_places=2)
    vitamin_e = models.DecimalField(max_digits=10, decimal_places=2)
    calcium = models.DecimalField(max_digits=10, decimal_places=2)
    omega_3 = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True, null=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return (self.entryID)




# Create your models here.
