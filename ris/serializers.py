from rest_framework import serializers
from .models import AgendaItem, Body, Location, Membership, Organization, Paper, Person, Meeting, System

class SystemSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='id_url') 
    class Meta:
        fields = ['id', 'name', 'type', 'oparlVersion', 'body', 'contactName', 'contactEmail', 'website']
        model = System

class LocationSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='id_url')
    geojson = serializers.JSONField()

    class Meta:
        fields = ['id', 'name', 'type', 'geojson' ]
        model = Location

class BodySerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='id_url')

    class Meta:
        fields = ['id', 'name', 'type', 'system', 'website', 'contactEmail', 'contactName', 'organization', 'person', 'meeting', 'paper']
        model = Body

class OrganizationSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='id_url') 
    #locationSerializer
    #membership

    class Meta:
        fields = ['id', 'name', 'type', 'body', 'website', 'organizationType', 'location']
        model = Organization

class OrganizationIdSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='id_url') 

    class Meta:
        fields = ['id']
        model = Organization


class PersonSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='id_url') 
    #membershipSerializer
    #body

    class Meta:
        fields = ['id', 'type', 'familyName', 'givenName', 'formOfAddress', 'gender']
        model = Person

class AgendaItemSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='id_url') 
    location = LocationSerializer(read_only=True, many=False)
    # meeting = MeetingSerializer(read_only=True, many=True)

    class Meta:
        fields = ['id', 'type', 'name', 'number', 'location', 'created', 'modified']
        model = AgendaItem

class MeetingSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='id_url') 
    person = PersonSerializer(read_only=True, many=True)
    organization = OrganizationIdSerializer(read_only=True, many=False)
    location = LocationSerializer(read_only=True, many=False)
    agendaItem = AgendaItemSerializer(read_only=True, many=True)

    class Meta:
        fields = ['id', 'type', 'name', 'start', 'end', 'location', 'organization', 'person', 'agendaItem']
        model = Meeting

class MembershipSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='id_url') 
    #person = serializers.CharField(source='person_url') 
    person = PersonSerializer(read_only=True, many=False)

    class Meta:
        fields = ['id', 'type', 'organization', 'person', 'role', 'votingRight']
        model = Membership


class PaperSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Paper


