from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Category, Event, Location, Ticket


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location

        fields = "__all__"
        read_only_fields = ("id",)


class EventSerializer(serializers.ModelSerializer):
    tickets_count = serializers.IntegerField(source="tickets.count", read_only=True)

    class Meta:
        model = Event

        fields = "__all__"
        read_only_fields = ("id", "tickets_count")

        extra_kwargs = {
            "start_time": {
                "format": "%Y.%m.%d %H:%M",
                "input_formats": ["%Y.%m.%d %H:%M"],
            },
            "end_time": {
                "format": "%Y.%m.%d %H:%M",
                "input_formats": ["%Y.%m.%d %H:%M"],
            },
        }

    def validate(self, attrs):
        if attrs["end_time"] <= attrs["start_time"]:
            raise serializers.ValidationError(
                "Время окончания не может быть позже начала"
            )
        return attrs


class TicketSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    event_title = serializers.CharField(source="event.title", read_only=True)

    class Meta:
        model = Ticket

        fields = "__all__"
        read_only_fields = ("id",)

    def validate(self, attrs):
        event = attrs.get("event")
        if event.tickets.count() >= event.capacity:
            raise serializers.ValidationError("Билеты закончились")
        return attrs


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category

        fields = "__all__"
        read_only_fields = ("id",)

        extra_kwargs = {
            "name": {
                "validators": [
                    UniqueValidator(
                        queryset=Category.objects.all(),
                        lookup="iexact",
                        message="Категория с таким названием уже существует",
                    )
                ]
            }
        }
