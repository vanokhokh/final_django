from django.db import models

class Curses(models.Model):
    title=models.CharField(max_length=20)
    length=models.IntegerField(null=True)
    class Meta:
        db_table = 'curses'

class Lectors(models.Model):
    name=models.CharField(max_length=20)
    surname=models.CharField(max_length=30)
    curses=models.ForeignKey(Curses, on_delete=models.CASCADE)
    class Meta:
        db_table = 'Lectors'

class Students(models.Model):
    name=models.CharField(max_length=20)
    surname=models.CharField(max_length=30)
    is_active=models.BooleanField(default=True)
    curses=models.ManyToManyField(Curses)
    lectors=models.ManyToManyField(Lectors)
    class Meta:
        db_table = 'students'
