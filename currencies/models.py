from django.db import models
from django.utils import timezone


class Rating(models.Model):
    date = models.DateTimeField()
    base = models.ForeignKey(
        'Currency',
        on_delete=models.CASCADE,
        related_name='bases'
    )
    rate = models.ForeignKey(
        'Currency',
        on_delete=models.CASCADE,
        related_name='rates'
    )
    rate_value = models.DecimalField(max_digits=12, decimal_places=6)
    created_at = models.DateTimeField(db_index=True, default=timezone.now)

    def __str__(self):
        return f"{self.base}-{self.rate}: {self.rate_value}"


class Currency(models.Model):
    title = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.title
