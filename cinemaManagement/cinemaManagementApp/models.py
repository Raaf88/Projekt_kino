from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# class CinemaDb(models.Model):
#     task = models.CharField(max_length=30)
#     priority = models.CharField(max_length=30)
#     completed = models.BooleanField(default=False)
#     time_date = models.DateTimeField(default=timezone.now)
#
#     def __str__(self):
#         return "%s %s" % (self.task, self.completed)


class Film(models.Model):
    tytul = models.CharField(max_length=25, null=False)
    rezyser = models.CharField(max_length=30, null=True)
    opis = models.TextField(max_length=300, null=True)
    ranking = models.FloatField()
    plakat = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return "{} -> {} -> {}".format(self.tytul, self.rezyser, self.ranking)

    def clean(self):
        if self.tytul == "":
            raise ValidationError("Podaj tytul")

    def save(self, *args, **kwargs):
        self.clean()
        super(Film, self).save(*args, **kwargs)


class Sala(models.Model):
    numerSali = models.IntegerField(primary_key=True)
    liczbaRzedow = models.IntegerField(null=False, default=7)
    numerMiejscaWrzedzie = models.IntegerField(null=False, default=7)


class Seans(models.Model):
    idFilmu = models.ForeignKey(Film, on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    dataSeansu = models.DateField()
    godzinaSeansu = models.DateTimeField()

    def __str__(self):
        return "{} -> {} -> {}".format(self.idFilmu, self.dataSeansu,  self.godzinaSeansu, )

class Rezerwacja(models.Model):
    seans = models.ForeignKey(Seans, on_delete=models.CASCADE)
    widz = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    rzad = models.IntegerField()
    miejsceWRzedzie = models.IntegerField

    def __str__(self):
        "{} -> {} -> rząd:{} -> miejsce:{}".format(self.seans, self.widz, self.rzad, self.miejsceWRzedzie)

    def save(self, *args, **kwargs):
        super(Rezerwacja, self).save(*args, **kwargs)

class Bilet(models.Model):
    reservation = models.ForeignKey(Rezerwacja, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateTimeField(Seans)

