from django.db.models.fields import DateTimeField
from django.shortcuts import render
from django.http import HttpResponse

from demoris.settings import HOSTNAME, OPARL_URL

from .models import AgendaItem, Location, Meeting, Membership, Paper, Person, System, Body, Organization
from .serializers import AgendaItemSerializer, BodySerializer, LocationSerializer, MeetingSerializer, MembershipSerializer, OrganizationSerializer, PaperSerializer, PersonSerializer, SystemSerializer
import json

def all_meetings_json(request, id):
    meeting = Meeting.objects.filter(id=id)
    data = MeetingSerializer(meeting, many=True).data
    response = json.dumps(data)
    return HttpResponse(response, content_type='application/json')

def view_one(request, obj, id):
    if obj == 'system':
        model = System
        object = model.objects.filter(id=id)
        data = SystemSerializer(object, many=True).data
    elif obj == 'body':
        model = Body
        object = model.objects.filter(id=id)
        data = BodySerializer(object, many=True).data
    elif obj == 'organization':
        model = Organization
        object = model.objects.filter(id=id)
        data = OrganizationSerializer(object, many=True).data
    elif obj == 'person':
        model = Person
        object = model.objects.filter(id=id)
        data = PersonSerializer(object, many=True).data
    elif obj == 'membership':
        model = Membership
        object = model.objects.filter(id=id)
        data = MembershipSerializer(object, many=True).data
    elif obj == 'meeting':
        model = Meeting
        object = model.objects.filter(id=id)
        data = MeetingSerializer(object, many=True).data
    elif obj == 'agendaitem':
        model = AgendaItem
        object = model.objects.filter(id=id)
        data = AgendaItemSerializer(object, many=True).data
    elif obj == 'location':
        model = Location
        object = model.objects.filter(id=id)
        data = LocationSerializer(object, many=True).data
    elif obj == 'paper':
        model = Paper
        object = model.objects.filter(id=id)
        data = PaperSerializer(object, many=True).data
    response = json.dumps(data)
    return HttpResponse(response, content_type='application/json')

def view_all(request, obj):
    if obj == 'system':
        model = System
        object = model.objects.all()
        data = SystemSerializer(object, many=True).data
    elif obj == 'body':
        model = Body
        object = model.objects.all()
        data = BodySerializer(object, many=True).data
    elif obj == 'organization':
        model = Organization
        object = model.objects.all()
        data = OrganizationSerializer(object, many=True).data
    elif obj == 'person':
        model = Person
        object = model.objects.all()
        data = PersonSerializer(object, many=True).data
    elif obj == 'membership':
        model = Membership
        object = model.objects.all()
        data = MembershipSerializer(object, many=True).data
    elif obj == 'meeting':
        model = Meeting
        object = model.objects.all()
        data = MeetingSerializer(object, many=True).data
    elif obj == 'agendaitem':
        model = AgendaItem
        object = model.objects.all()
        data = AgendaItemSerializer(object, many=True).data
    elif obj == 'location':
        model = Location
        object = model.objects.all()
        data = LocationSerializer(object, many=True).data
    elif obj == 'paper':
        model = Paper
        object = model.objects.all()
        data = PaperSerializer(object, many=True).data
    response = json.dumps(data)
    #response = json.dumps(data).replace("\\","")
    return HttpResponse(response, content_type='application/json')
