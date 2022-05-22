from django.urls import path

from . import views

# All the URLs which belong to the app "meetups"
# Also tells which view functions are to be executed when requests reach those URLs

urlpatterns = [
    path('meetups/', views.index, name="all-meetups"),
    path('meetups/<slug:meetup_slug>/success', views.confirm_registration, name='confirm-registration'),
    path('meetups/<slug:meetup_slug>', views.meetup_details, name="meetup-details"),
]