from django.db import models 

class Reading(models.Model):
    UNIT_CHOICES = [
        ('pH', 'pH'),
        ('C', 'Temperature (C)'),
        ('mg/L', 'Concentration (mg/L)'),
        ('%', 'Percentage (%)'),
    ]

    sensor_name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=6, decimal_places=2)
    unit = models.CharField(max_length=20, choices=UNIT_CHOICES)
    recorded_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.sensor_name} - {self.value}{self.unit}"
    