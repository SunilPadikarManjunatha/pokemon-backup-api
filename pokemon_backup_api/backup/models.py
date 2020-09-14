from django.db import models
from django.contrib.postgres.fields import JSONField
from rest_framework import serializers

class Backups(models.Model):
    
    name = models.CharField(max_length=50, null=False)
    backup_on = models.DateTimeField(auto_now=True)
    # data = JSONField()

class BackupItems(models.Model):

    backup = models.ForeignKey(Backups, on_delete=models.CASCADE)
    card_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    # national_pokedex_number =models.IntegerField(null=True)
    image_url = models.URLField()
    image_url_hi_res = models.URLField()
    subtype = models.CharField(max_length=100)
    supertype = models.CharField(max_length=100)
    ability = JSONField(blank=True, null=True)
    # ancient_trait = models.CharField(max_length=100)
    hp = models.CharField(max_length=5, null=True)
    number = models.IntegerField(null=True)
    artist = models.CharField(max_length=100)
    rarity =models.CharField(max_length=15)
    series = models.CharField(max_length=10)
    set =  models.CharField(max_length=10)
    set_code = models.CharField(max_length=10)
    retreat_cost = JSONField(blank=True,null=True)
    converted_retreat_cost = models.IntegerField(null=True)
    text=JSONField(blank=True,null=True)
    types = JSONField(blank=True, null=True)
    attacks = JSONField(blank=True, null=True)
    weaknesses = JSONField(blank=True, null=True)
    resistances = JSONField(blank=True, null=True)
    evolves_from = models.CharField(max_length=20, null=True)

class CardsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= BackupItems
        fields = '__all__'
