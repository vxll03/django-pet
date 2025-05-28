from django.contrib import admin
from .models import Category, Event, Location, Ticket

# admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Ticket)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "capacity", "start_time", "end_time")
    list_filter = ("location__city", "categories__name")
    search_fields = ("title",)
