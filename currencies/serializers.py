from rest_framework import serializers

from currencies.models import Rating


class RatingSerializer(serializers.ModelSerializer):
    base = serializers.SlugRelatedField(read_only=True, slug_field='title')
    rate = serializers.SlugRelatedField(read_only=True, slug_field='title')
    date = serializers.DateTimeField(read_only=True, format="%d.%m.%Y %H:%M")

    class Meta:
        model = Rating
        fields = (
            'id',
            'date',
            'base',
            'rate',
            'rate_value',
        )


class RatingInputSerializer(serializers.Serializer):
    date = serializers.DateTimeField()
    base = serializers.CharField(max_length=10)
    rate = serializers.CharField(max_length=10)
    rate_value = serializers.DecimalField(max_digits=12, decimal_places=6)
