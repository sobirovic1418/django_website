from django.urls import path

from orbit.views import index

urlpatterns=[
    path('',index)
]