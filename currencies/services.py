from django.db import transaction

from currencies.models import Rating, Currency


@transaction.atomic
def create_rating(data: dict) -> None:
    base = Currency.objects.get(title=data.pop('base'))
    rate = Currency.objects.get(title=data.pop('rate'))
    Rating.objects.create(base=base, rate=rate, **data)
