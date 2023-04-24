from django.contrib import admin
from .models import Highlight, About, Event, StudentReview, TeamLead, ContactInfo


class HighlightAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_date', 'time')
    list_filter = ('event_date',)

class StudentReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'classification', 'comments')
    list_filter = ('classification',)

class TeamLeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')

class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('headquarter', 'university', 'copyright', 'designer', 'phone_number', 'email', 'careers_link', 'investor_link', 'terms_conditions_link')


admin.site.register(ContactInfo, ContactInfoAdmin)
admin.site.register(Highlight, HighlightAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(StudentReview, StudentReviewAdmin)
admin.site.register(TeamLead, TeamLeadAdmin)
admin.site.register(About, AboutUsAdmin)