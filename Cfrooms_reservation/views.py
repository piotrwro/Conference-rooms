from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from Cfrooms_reservation.models import Conferenceroom


class MainPage(View):
    def get(self, request):
        return render(request, "main_page.html")


class AddRoom(View):
    def get(self, request):
        return render(request, "add_conference_room.html")

    def post(self, request):

        name = request.POST.get('name')
        places = int(request.POST.get('places', ))
        projector = request.POST.get('projector')
        if not name:
            return HttpResponse(f"Error: No conference room name")
        elif Conferenceroom.objects.filter(name=name).first():
            return HttpResponse(f"Error:Conference room exists")
        if places <= 0:
            return HttpResponse(f"Error:Value for Places must be higher then 0")
        Conferenceroom.objects.create(name=name, places=places, projector=projector)
        return render(request, 'add_conference_room.html', context={'name': name})


class ListRooms(View):
    def get(self, request):
        cfrooms = Conferenceroom.objects.all()
        return render(request, 'list_room.html', context={'cfrooms': cfrooms})


class DeleteRoom(View):
    def get(self, request, id):
        cfroom_id = Conferenceroom.objects.get(id=id)
        cfroom_id.delete()
        return redirect("list_room")


class ModifyRoom(View):
    def get(self, request, id):
        Conferenceroom.objects.get(id=id)
        return render(request, "set_conference_room.html")

    def post(self, request, ):
        cfroom= Conferenceroom.objects.get(id=id)
        name = request.POST.get('name')
        places = int(request.POST.get('places'))
        projector = request.POST.get('projector')
        if not name:
            return HttpResponse(f"Error: No conference room name")
        elif Conferenceroom.objects.filter(name=name).first():
            return HttpResponse(f"Error:Conference room exists")
        if places <= 0:
            return HttpResponse(f"Error:Value for Places must be higher then 0")
        cfroom.name = name
        cfroom.places = places
        cfroom.projector = projector
        cfroom.save()
        return redirect("list_room")



# Create your views here.
