from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from Cfrooms_reservation.models import Conferenceroom, Reservation
from datetime import date


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
        for room in cfrooms:
            reservation_dates = [reservation.reservation_date for reservation in room.reservation_set.all()]

            room.reserved = date.today() in reservation_dates
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

    def post(self, request,  id):
        cfroom= Conferenceroom.objects.get(id=id)
        name = request.POST.get('name')
        places = (request.POST.get('places'))
        places = int(places) if places else 0
        projector = request.POST.get('projector')
        if places <= 0:
            return HttpResponse(f"Places must be higher than 0")

        elif Conferenceroom.objects.filter(name=name).first():
            return HttpResponse(f"Error:Conference room exists")

        elif not name:
            return HttpResponse(f"Error: No conference room name")
        else:
            cfroom.name = name
            cfroom.places = places
            cfroom.projector = projector
            cfroom.save()
            return redirect("list_room")


class ReserveRoom(View):
    def get(self, request,  room_id):
        room = Conferenceroom.objects.get(id=room_id)
        return render(request, 'reserve_room.html', context={"room": room})

    def post(self, request, room_id):
        room = Conferenceroom.objects.get(id=room_id)
        comment = request.POST.get('comment')
        reservation_date = request.POST.get('reservation_date')
        if reservation_date < str(date.today()):
            return HttpResponse(f"Date must be future date!")
        elif Reservation.objects.filter(reservation_date=reservation_date).first():
            return HttpResponse(f"Error: Sala jest już zarezerwowana!")
        else:
            Reservation.objects.create(cfroom_id=room, reservation_date=reservation_date, comment=comment )
            return redirect("reservationlist")

class RoomDetailsView(View):

    def get(self, request, room_id):
        room = Conferenceroom.objects.get(id=room_id)

        reservations = room.reservation_set.filter(reservation_date__gte=str(date.today())).order_by('reservation_date')

        return render(request, "reservationlist.html", context={"room": room, "reservations": reservations})