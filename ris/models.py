from os import name
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import AutoField
#from django.utils.dateparse import parse_datetime
from demoris.settings import HOSTNAME, OPARL_URL, OPARL_VERSION

class System(models.Model):
    id  = models.BigAutoField(primary_key=True, editable=False)
    id_url = models.CharField(max_length=256, default = HOSTNAME + OPARL_URL + "system/")
    type = "https://schema.oparl.org/" + OPARL_VERSION + "/System"
    oparlVersion = "https://schema.oparl.org/" + OPARL_VERSION
    body = HOSTNAME  + OPARL_URL + "body"
    name = models.CharField(max_length=256)
    contactEmail = models.EmailField(max_length=256, null=True, blank=True)
    contactName = models.CharField(max_length=256, null=True, blank=True)
    website = models.URLField(max_length=256, null=True, blank=True)
    product = "https://oparl.org"
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the "real" save() method.
        self.id_url = HOSTNAME + OPARL_URL + "system/" + str(self.id)
        super().save(*args, **kwargs) 
        #print("id_url : " + str(self.id_url))

    def __str__(self):
        return "{0}".format(self.name)

class Body(models.Model):
    id  = models.BigAutoField(primary_key=True, editable=False)
    id_url = models.CharField(max_length=256, default = HOSTNAME + OPARL_URL + "body/")
    type = "https://schema.oparl.org/" + OPARL_VERSION +"/Body"
    name = models.CharField(max_length=256)
    system = models.ForeignKey(to='System', on_delete=models.CASCADE)
    website = models.URLField(max_length=256, null=True, blank=True)
    ags = models.CharField(max_length=256, null=True, blank=True)
    rgs = models.CharField(max_length=256, null=True, blank=True)
    contactEmail = models.EmailField(max_length=256, null=True, blank=True)
    contactName = models.CharField(max_length=256, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    organization = HOSTNAME + OPARL_URL + "organization/"
    person = HOSTNAME + OPARL_URL + "person/"
    meeting = HOSTNAME + OPARL_URL + "meeting/"
    paper = HOSTNAME + OPARL_URL + "paper/"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the "real" save() method.
        self.id_url = HOSTNAME + OPARL_URL + "body/" + str(self.id)
        super().save(*args, **kwargs) 
        #print("id_url : " + str(self.id_url))
    

    def __str__(self):
        return "{0}".format(self.name)


class Organization(models.Model):
    id  = models.BigAutoField(primary_key=True, editable=False)
    id_url = models.CharField(max_length=256, default = HOSTNAME + OPARL_URL + "organization/")
    type = "https://schema.oparl.org/" + OPARL_VERSION +"/Organization"
    name = models.CharField(max_length=256)
    body = models.ForeignKey(to='Body', on_delete=models.CASCADE)
    website = models.URLField(max_length=256, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    #membership
    #meeting
    organizationType = models.CharField(max_length=256, null=True, blank=True)
    location = models.ForeignKey(to='Location', on_delete=models.PROTECT, null=True, blank=True)
    #classification

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the "real" save() method.
        self.id_url = HOSTNAME + OPARL_URL + "organization/" + str(self.id)
        super().save(*args, **kwargs) 
        #print("id_url : " + str(self.id_url))

    def __str__(self):
        return "{0}".format(self.name)

class Person(models.Model):
    id  = models.BigAutoField(primary_key=True, editable=False)
    id_url = models.CharField(max_length=256, default = HOSTNAME + OPARL_URL + "person/")
    type = "https://schema.oparl.org/" + OPARL_VERSION +"/Person"
    #body = models.ForeignKey(to='Body', on_delete=models.CASCADE)
    familyName = models.CharField(max_length=256)
    givenName = models.CharField(max_length=256)
    formOfAddress = models.CharField(max_length=256, null=True, blank=True)
    gender = models.CharField(max_length=256, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    #membership
    #status

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the "real" save() method.
        self.id_url = HOSTNAME + OPARL_URL + "person/" + str(self.id)
        super().save(*args, **kwargs) 
        print("id_url : " + str(self.id_url))

    def __str__(self):
        return "{0} {1}".format(self.givenName, self.familyName)

class Membership(models.Model):
    id  = models.BigAutoField(primary_key=True, editable=False)
    id_url = models.CharField(max_length=256, default = HOSTNAME + OPARL_URL + "membership/")
    type = "https://schema.oparl.org/" + OPARL_VERSION +"/Membership"
    person = models.ForeignKey(to='Person', on_delete=models.PROTECT)
    person_url = models.CharField(max_length=256, default = HOSTNAME + OPARL_URL + "person/")
    organization = models.ForeignKey(to='Organization', on_delete=models.PROTECT)
    role = models.CharField(max_length=256)
    votingRight = models.BooleanField()
    #startDate
    #endDate

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the "real" save() method.
        self.id_url = HOSTNAME + OPARL_URL + "membership/" + str(self.id)
        self.person_url = HOSTNAME + OPARL_URL + "person/" + str(self.person)
        super().save(*args, **kwargs) 
        print("id_url : " + str(self.id_url) + "   person_url : " + str(self.person_url))

    def __str__(self):
        return "{0} - {1} - {2}".format(self.id, self.person, self.organization)


class AgendaItem(models.Model):
    id  = models.BigAutoField(primary_key=True, editable=False)
    id_url = models.CharField(max_length=256, default = HOSTNAME + OPARL_URL + "agendaitem/")
    type = "https://schema.oparl.org/" + OPARL_VERSION +"/agendaItem"
    name = models.CharField(max_length=256)
    number = models.IntegerField()
    location = models.ForeignKey(to='Location', on_delete=models.PROTECT, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the "real" save() method.
        self.id_url = HOSTNAME + OPARL_URL + "agendaitem/" + str(self.id)
        super().save(*args, **kwargs) 
        #print("id_url : " + str(self.id_url))

    def __str__(self):
        return "{0}".format(self.name)


class Meeting(models.Model):
    id  = models.BigAutoField(primary_key=True, editable=False)
    id_url = models.CharField(max_length=256, default = HOSTNAME + OPARL_URL + "meeting/")
    type = "https://schema.oparl.org/" + OPARL_VERSION +"/Meeting"
    organization = models.ForeignKey(to='Organization', on_delete=models.PROTECT)
    location = models.ForeignKey(to='Location', on_delete=models.PROTECT, null=True, blank=True)
    name = models.CharField(max_length=256)
    person = models.ManyToManyField(Person)
    agendaItem = models.ManyToManyField(AgendaItem)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the "real" save() method.
        self.id_url = HOSTNAME + OPARL_URL + "meeting/" + str(self.id)
        super().save(*args, **kwargs) 
        #print("id_url : " + str(self.id_url))

    def __str__(self):
        return "{0}".format(self.name)


class Location(models.Model):
    id  = models.BigAutoField(primary_key=True, editable=False)
    id_url = models.CharField(max_length=256, default = HOSTNAME + OPARL_URL + "location/")
    type = "https://schema.oparl.org/" + OPARL_VERSION +"/Location"
    name = models.CharField(max_length=256)
    geojson = models.TextField(null=True, blank=True)
    #gejson

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the "real" save() method.
        self.id_url = HOSTNAME + OPARL_URL + "location/" + str(self.id)
        super().save(*args, **kwargs) 
        #print("id_url : " + str(self.id_url))

    def __str__(self):
        return "{0}".format(self.name)

class Paper(models.Model):
    id  = models.BigAutoField(primary_key=True, editable=False)
    id_url = models.CharField(max_length=256, default = HOSTNAME + OPARL_URL + "paper/")
    type = "https://schema.oparl.org/" + OPARL_VERSION +"/Paper"
    name = models.CharField(max_length=256)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the "real" save() method.
        self.id_url = HOSTNAME + OPARL_URL + "paper/" + str(self.id)
        super().save(*args, **kwargs) 
        #print("id_url : " + str(self.id_url))

    def __str__(self):
        return "{0}".format(self.name)




