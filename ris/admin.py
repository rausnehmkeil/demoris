from django.contrib import admin
from .models import AgendaItem, Location, Meeting, Membership, Organization, Paper, Person, System, Body

admin.site.register(System)
admin.site.register(Body)
admin.site.register(Location)
#admin.site.register(Paper)


admin.site.site_header = 'Pfaffhack-Ratsinformationssystem'

@admin.register(Organization)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "organizationType")

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("familyName", "givenName")


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ("id", "person", "organization")

@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "organization", "start")

@admin.register(AgendaItem)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "number", "location")



