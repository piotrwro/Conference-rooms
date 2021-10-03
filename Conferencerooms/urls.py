"""Conferencerooms URL Configuration

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
from django.urls import path
from Cfrooms_reservation.views import MainPage, AddRoom, ListRooms, DeleteRoom, ModifyRoom

urlpatterns = [
    path('admin/', admin.site.urls),
    path('CFrooms/main-page', MainPage.as_view()),
    path('CFrooms/add_room', AddRoom.as_view()),
    path('CFrooms/list_room', ListRooms.as_view(), name="list_room"),
    path('CFrooms/delete_room/<int:id>', DeleteRoom.as_view()),
    path('CFrooms/set_room/<int:id>', ModifyRoom.as_view())
    ]
