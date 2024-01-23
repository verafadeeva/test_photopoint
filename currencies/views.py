import time
import threading
import os
from datetime import datetime

import requests
from rest_framework import status, views
from rest_framework.response import Response

from currencies.selectors import get_exchange_rates
from currencies.serializers import RatingSerializer, RatingInputSerializer
from currencies.services import create_rating


def get_currency():
    params = {
        'app_id': os.getenv('APP_ID'),
        'base': 'USD',
        'symbols': 'RUB'
    }
    while True:
        print("Pinging ...")
        response = requests.get(os.getenv('URL'), params=params, timeout=3.05).json()
        data = {
            'date': datetime.fromtimestamp(response.get('timestamp')).isoformat(),
            'base': response.get('base'),
            'rate': 'RUB',
            'rate_value': response.get('rates').get('RUB'),
        }
        ser = RatingInputSerializer(data=data)
        ser.is_valid()
        create_rating(ser.validated_data)
        time.sleep(30)


class ListRatingView(views.APIView):
    """Отображает список актуального курса доллара к рублю"""

    def get(self, request):
        rates = get_exchange_rates()
        return Response(
            RatingSerializer(rates, many=True).data,
            status=status.HTTP_200_OK,
        )


t = threading.Thread(target=get_currency)
t.start()
