from django.db import models
from django.urls import reverse

# Create your models here.
class Analysis(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    analysis_code = models.CharField(max_length=10, null=False, blank=False)
    completion_date = models.PositiveSmallIntegerField(null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
    consumables = models.ForeignKey('Consumables', on_delete=models.CASCADE)
    rater = models.ManyToManyField('Gobmp')
    how_prepare = models.ForeignKey('Preparation', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('analysis_detail', args=[str(self.id)])

    class Meta:
        ordering = ['title']

class Gobmp(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    analysis_Gcode = models.CharField(max_length=15, null=False, blank=False)
    price = models.FloatField(null=False, blank=False)

    def __str__(self):
        return str(self.analysis_Gcode) + ' ' + str(self.title)

class Consumables(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    volume = models.FloatField(null=True)
    taking = models.ForeignKey('TakingTechnique', on_delete=models.CASCADE)
    method_transportation = models.ForeignKey('HowTransportation', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title) + ' ' + str(self.volume) + ' ml'

class TakingTechnique(models.Model):
    taking_technique = models.TextField(null=False, blank=False)

    def __str__(self):
        return str(self.taking_technique)

class HowTransportation(models.Model):
    transportation = models.TextField(null=False, blank=False)

    def __str__(self):
        return str(self.transportation)

class Preparation(models.Model):
    method_preparation = models.TextField(null=False, blank=False)

    def __str__(self):
        return str(self.method_preparation)