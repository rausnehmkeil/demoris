"""demoris URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.admin.options import IS_POPUP_VAR
from ris.views import redirect_view, view_all, view_one
from django.urls import path
from demoris.settings import OPARL_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_view),
    #path('', oparl_system),
    #path(OPARL_URL + 'system/', oparl_system),
    #path(OPARL_URL + 'body/', oparl_bodies),
    #path(OPARL_URL + 'body/<int:id>/', oparl_body),
    #path(OPARL_URL + 'organization/', oparl_organizations),
    #path(OPARL_URL + 'organization/<int:id>/', oparl_organization),
    #path(OPARL_URL + 'person/', oparl_persons),
    #path(OPARL_URL + 'person/<int:id>/', oparl_person),
    #path(OPARL_URL + 'membership/', oparl_memberships),
    #path(OPARL_URL + 'membership/<int:id>/', oparl_membership),
    #path(OPARL_URL + 'meeting/', oparl_meetings),
    #path(OPARL_URL + 'meeting/<int:id>/', oparl_meeting),
    #path(OPARL_URL + 'location/', oparl_locations),
    #path(OPARL_URL + 'location/<int:id>/', oparl_location),
    path(OPARL_URL + '<str:obj>/', view_all),
    path(OPARL_URL + '<str:obj>/<int:id>/', view_one),
]
