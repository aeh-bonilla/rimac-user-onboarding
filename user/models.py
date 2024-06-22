from django.db import models


# Definición del modelo User para representar las películas
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField()
    age = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    born_gender = models.CharField(max_length=12)


class Physical_health_background(models.Model):
    diabetes = models.BooleanField()
    hypertension = models.BooleanField()
    cancer = models.BooleanField()
    obesity   = models.BooleanField()
    heart_disease = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Mental_health_background(models.Model):
    sleep_disorder = models.BooleanField()
    major_depression = models.BooleanField()
    bipolar_disorder = models.BooleanField()
    anxiety = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class User_health_scores(models.Model):
    meassure_date = models.DateField()
    feeling = models.IntegerField()
    lifestyle = models.IntegerField()
    body = models.IntegerField()
    movement = models.IntegerField()
    nutrition = models.IntegerField()
    smoking = models.IntegerField()
    alcohol = models.IntegerField()
    obesity = models.IntegerField()
    wellnes = models.IntegerField()
    stress = models.IntegerField()
    depression = models.IntegerField()
    confidence_lower = models.IntegerField()
    confidence_upper = models.IntegerField()
    uncertainty = models.IntegerField()
    indulgence = models.IntegerField()
    mindfulness = models.IntegerField()
    averge_score = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Journal(models.Model):
    comment = models.TextField()
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

