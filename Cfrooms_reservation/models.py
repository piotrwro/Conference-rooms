from django.db import models


class Conferenceroom(models.Model):
    name = models.CharField(max_length=255)
    places = models.IntegerField(default=0)
    projector = models.BooleanField(default=False)


class Reservation(models.Model):
    reservation_date = models.DateField()
    cfroom_id = models.ForeignKey(Conferenceroom, null=True, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)

