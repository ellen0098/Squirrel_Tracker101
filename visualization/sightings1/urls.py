from django.urls import path
from . import views
from django.conf.urls import url
from .views import Totalsquirrels,squirreladd
urlpatterns=[
        path('sightings1/',views.Totalsquirrels),
        path('sightings/add/',views.squirreladd,name='add'),
        path('map/',views.showmap,name='showmap'),
        path('sightings/stats/',views.statistics,name='statistics'),
        path('sightings/<squirrel_id>/', views.squirrelupdate,name='update'),
        path('sightings/<squirrel_id>/delete/',views.squirreldelete,name='delete'),
        ]
