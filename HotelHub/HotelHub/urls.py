"""
URL configuration for HotelHub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path
from rest_framework import routers
from django.contrib.auth.views import LogoutView
from rest_framework.authtoken.views import obtain_auth_token
from hotels.views import registration_view

from hotels.viewsets import RoomViewSet,GuestViewSet,ReservationViewSet,EventViewSet,EventAttendeesViewSet,FolioPostingViewSet,FolioViewSet,PaymentViewSet

router = routers.DefaultRouter()
router.register('rooms', RoomViewSet)
router.register('guests',GuestViewSet)
router.register('reservations',ReservationViewSet)
router.register('event',EventViewSet)
router.register('event_attendees',EventAttendeesViewSet)
router.register('folio',FolioViewSet)
router.register('folio_posting',FolioPostingViewSet)
router.register('payments',PaymentViewSet)
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/',obtain_auth_token),
    path('api/',include(router.urls)),
    path("api/register/", registration_view),
    path("logout", LogoutView.as_view()),
]
