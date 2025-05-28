from rest_framework import serializers

from .models import Category, Event, Location, Ticket

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location

        fields = ('__all__')
        read_only_fields = ('id',)

class EventSerializer(serializers.ModelSerializer):
    tickets_count = serializers.IntegerField(source='tickets.count', read_only=True)

    class Meta:
        model = Event

        fields = '__all__'
        read_only_fields = ('id', 'tickets_count')

        extra_kwargs = {
            'start_time': {'format': '%Y.%m.%d %H:%M', 'input_formats': ['%Y.%m.%d %H:%M']},
            'end_time': {'format': '%Y.%m.%d %H:%M', 'input_formats': ['%Y.%m.%d %H:%M']}
        }

    def validate(self, attrs):
        if attrs['end_time'] <= attrs['start_time']:
            raise serializers.ValidationError('Время окончания не может быть позже начала')
        return attrs

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket

        fields = '__all__'
        read_only_fields = ('id',)

    def validate(self, attrs):
        event: Event = attrs.get('event')
        if event.tickets.count() >= event.capacity:
            raise serializers.ValidationError("Билеты закончились")
        return attrs
    

class  CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category

        fields = '__all__'
        read_only_fields = ('id',)