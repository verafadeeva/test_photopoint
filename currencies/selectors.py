from django.db.models import QuerySet

from currencies.models import Rating


def get_exchange_rates(*, base='USD', rate='RUB', limit=10) -> QuerySet:
    queryset = Rating.objects.select_related('base', 'rate').\
        filter(base__title=base, rate__title=rate).\
        order_by('-created_at')[:limit]
    return queryset
