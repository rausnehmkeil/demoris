from django.contrib import admin
from .models import AgendaItem, Location, Meeting, Membership, Organization, Paper, Person, System, Body

admin.site.register(System)
admin.site.register(Body)
admin.site.register(Organization)
admin.site.register(Person)
admin.site.register(Membership)
admin.site.register(Meeting)
admin.site.register(AgendaItem)
admin.site.register(Location)
admin.site.register(Paper)


