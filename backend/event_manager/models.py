from django.core.validators import MinValueValidator
from django.db import models


class Location(models.Model):
    def __str__(self) -> str:
        return f"г. {self.city}, ул. {self.street}, д. {self.building}"

    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    building = models.CharField(max_length=50)
    appartment = models.CharField(
        max_length=50, null=True, blank=True, help_text="Необязательное поле"
    )


class Event(models.Model):
    def __str__(self) -> str:
        return self.title

    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    categories = models.ManyToManyField("Category", related_name="events")

    location = models.ForeignKey(
        "Location", on_delete=models.CASCADE, related_name="events"
    )
    capacity = models.IntegerField(
        validators=[MinValueValidator(0)], help_text="Вместимость (больше 0)"
    )

    start_time = models.DateTimeField(help_text='Начало события (Формат = гггг.мм.дд ЧЧ:ММ)')
    end_time = models.DateTimeField(help_text='Конец события (Формат = гггг.мм.дд ЧЧ:ММ)')


class Ticket(models.Model):
    class TicketStatus(models.TextChoices):
        ACTIVE = ("Active",)
        PASSED = ("Passed",)
        CANCELLED = "Cancelled"

    class Meta:
        unique_together = [["user", "event"]]

    def __str__(self) -> str:
        return f"Билет {self.user.username} на {self.event.title}"

    user = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="tickets"
    )
    event = models.ForeignKey("Event", on_delete=models.CASCADE, related_name="tickets")
    status = models.TextField(choices=TicketStatus.choices, default=TicketStatus.ACTIVE)


class Category(models.Model):
    class Meta:
        db_table = "categories"

    def __str__(self) -> str:
        return self.name

    name = models.CharField(max_length=50, unique=True)
