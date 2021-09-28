from django.db import models


class Conferenceroom(models.Model):
    name = models.CharField(max_length=255)
    places = models.IntegerField()
    projector = models.BooleanField(default=False)


class Reservation(models.Model):
    reservation_date = models.DateField()
    cfroom_id = models.ForeignKey(Conferenceroom, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
