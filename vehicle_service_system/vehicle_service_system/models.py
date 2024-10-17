from django.db import models

class Component(models.Model):
    TYPE_CHOICES = [
        ('new', 'New'),
        ('repair', 'Repair'),
    ]
    
    name = models.CharField(max_length=100)
    # Provide a default value for the component_type field to avoid migration issues
    component_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='new')  # Default set to 'new'
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):  # Fixed method name from _str_ to __str__
        return f"{self.name} ({self.component_type}) - ${self.price}"

class Vehicle(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):  # Fixed method name from _str_ to __str__
        return f"{self.make} {self.model} ({self.year})"

class Issue(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    issue_type = models.CharField(max_length=10, choices=Component.TYPE_CHOICES)

    def __str__(self):  # Fixed method name from _str_ to __str__
        return f"Issue for {self.vehicle} - {self.component.name} ({self.issue_type})"

class Transaction(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    final_price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # Fixed method name from _str_ to __str__
        return f"Transaction for {self.vehicle} - ${self.final_price} on {self.date}"
