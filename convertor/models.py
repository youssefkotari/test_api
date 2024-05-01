from django.db import models

class Currency(models.Model):
    code = models.CharField(max_length=5, unique=True)
    rate = models.DecimalField(max_digits=20, decimal_places=10)

    def __str__(self):
        return self.code
