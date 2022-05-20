from django.contrib import admin

from .models import Location, Meetup, Participant

# Register your models here.

class MeetupAdmin(admin.ModelAdmin):
    # Case sensitive to the field which is already defined.
    list_display = ('title', 'slug', 'location')
    list_filter = ('location', 'date')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Location)
admin.site.register(Participant)